#include <vslc.h>
#include <inttypes.h>

void
node_print ( node_t *root, int nesting )
{
    if ( root != NULL )
    {
        printf ( "%*c%s", nesting, ' ', node_string[root->type] );
        if ( root->type == IDENTIFIER_DATA ||
             root->type == STRING_DATA ||
             root->type == RELATION ||
             root->type == EXPRESSION ) 
            printf ( "(%s)", (char *) root->data );
        else if ( root->type == NUMBER_DATA )
            printf ( "(%ld)", *((int64_t *)root->data) );
        putchar ( '\n' );
        for ( int64_t i=0; i<root->n_children; i++ )
            node_print ( root->children[i], nesting+1 );
    }
    else
        printf ( "%*c%p\n", nesting, ' ', root );
}


void
node_init (node_t *nd, node_index_t type, void *data, uint64_t n_children, ...)
{
    va_list child_list;
    *nd = (node_t) {
        .type = type,
        .data = data,
        .entry = NULL,
        .n_children = n_children,
        .children = (node_t **) malloc ( n_children * sizeof(node_t *) )
    };
    va_start ( child_list, n_children );
    for ( uint64_t i=0; i<n_children; i++ )
        nd->children[i] = va_arg ( child_list, node_t * );
    va_end ( child_list );
}


void
node_finalize ( node_t *discard )
{
    if ( discard != NULL )
    {
        free ( discard->data );
        free ( discard->children );
        free ( discard );
    }
}


void
destroy_subtree ( node_t *discard )
{
    if ( discard != NULL )
    {
        for ( uint64_t i=0; i<discard->n_children; i++ )
            destroy_subtree ( discard->children[i] );
        node_finalize ( discard );
    }
}

bool
list_type ( node_t *node )
{
    switch( node->type )
    {
        case GLOBAL_LIST:
            return true;
            break;
        case STATEMENT_LIST:
            return true;
            break;
        case PRINT_LIST:
            return true;
            break;
        case EXPRESSION_LIST:
            return true;
            break;
        case VARIABLE_LIST:
            return true;
            break;
        case ARGUMENT_LIST:
            return true;
            break;
        case PARAMETER_LIST:
            return true;
            break;
        case DECLARATION_LIST:
            return true;
            breas, STATEMENTs and ARGUMENT_LISTs
            return false;
            break;
    }
}

void
simplify_tree ( node_t **simplified, node_t *node )
{
    /* Loop over children of the node */
    for ( int i = 0; i < node->n_children; i++ ) {
        if ( node->children[i] != NULL) {
          simplify_tree( &node->children[i], node->children[i] );
        }
    }

    // Remove NULL EXPRESSION nodes
    if ( node->type == EXPRESSION || node->type == RELATION || node->type == RETURN_STATEMENT ) {
        for (int i = 0; i < node->n_children; i++) {
            if ( node->children[i]->type == EXPRESSION && node->children[i]->data == NULL && node->children[i]->n_children <= 1) {
                // This node can have multiple children
                node_t *to_finalize = node->children[i];
                node->children[i] = node->children[i]->children[0];
                node_finalize(to_finalize);
            }
        }
    }

    /* Fixing nested lists of same types */
    // We may have to check if the node has any children here
    if ( list_type( node ) && node->children[0]->type == node->type ) {
        node_t *child_node = node->children[0];
        node_t **children_array = (node_t **) realloc ( child_node->children, (child_node->n_children+1)*sizeof(node_t*) );

        /* If we have successfully reallocated the children */
        if ( children_array != NULL ) {

          child_node->children = NULL; // Children has been reallocated, so we can set this one to NULL
          children_array[child_node->n_children] = node->children[1]; // Set the the last element of the children array to point to the next child of the parent
          node->n_children = child_node->n_children+1; // The parent now has one more child, duh
          node->children = children_array; // Assign the new children_array to the parent
          node_finalize(child_node); // The current node doesnt have anything more to give, so we kill it
        }
        else {
          printf("Could not reallocate children");
        }
    }

    // Remove GLOBALs
    if ( node->type == GLOBAL_LIST ) {
        for (int i = 0; i < node->n_children; i++) {
            if (node->children[i]->type == GLOBAL) {
                // Need to finalize stuff
                node->children[i] = node->children[i]->children[0];
            }
        }
    }


    // Remove PARAMETER_LISTs, STATEMENTs and ARGUMENT_LISTs
    if ( node->type == PARAMETER_LIST || node->type == STATEMENT || node->type == ARGUMENT_LIST ) {
        node_t *to_finalize = node;
        node = node->children[0];
        node_finalize(to_finalize);
    }

    if (node->type == PRINT_STATEMENT) {
        node_t *child = node->children[0];
        if (child->type == PRINT_LIST) {
            node->n_children = child->n_children;
            free(node->children);
            node->children = child->children;
            child->children = NULL;
            node_finalize(child);

            // Remove items
            for (int i = 0; i < node->n_children; i++) {
                  node_t *child = node->children[i];
                  node->children[i] = child->children[0];
                  node_finalize(child);
            }
        }
    }

    *simplified = node;
}
