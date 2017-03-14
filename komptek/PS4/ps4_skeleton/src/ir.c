#include <vslc.h>

tlhash_t *global_names;
char **string_list;
size_t n_string_list = 8, stringc = 0;

symbol_t *
make_symbol ( node_t *node, int counter, symtype_t type )
{
    symbol_t *symbol = malloc ( sizeof ( symbol_t ) );
    // ???
    if (type != FUNCTION) {
      char *name = strdup ( node->data );

      // Allocate some memory for our aymbol

      // Cast the struct to be the type symbol_t and store it where the pointer points
      *symbol = ( symbol_t ) {
          .name = name,
          .type = type,
          .seq = counter,
          .nparms = 0,
          .node = node,
          .locals = NULL,
      };
    }
    else
    {
        char *name = strdup(node->children[0]->data);
        int nparms = 0;
        tlhash_t *hash_table;
        hash_table = malloc( sizeof( tlhash_t ) );
        tlhash_init(hash_table, 1);

        if( node->children[1] != NULL ) // are there parameter nodes?
          //???
        {
            node_t *block_node = node->children[1];
            for (; nparms < block_node->n_children; nparms++ )
            {
                symbol_t *parameter_symbol = make_symbol(block_node->children[nparms], nparms, SYM_PARAMETER);
                tlhash_insert(hash_table, parameter_symbol->name, strlen(parameter_symbol->name), parameter_symbol);
            }
        }
        *symbol = ( symbol_t )
        {
            .name   = name,
            .type   = SYM_FUNCTION,
            .seq    = counter,
            .nparms = nparms,
            .node   = node,
            .locals = hash_table
        };

    }
    return symbol;
}

void
traverse_subtree ( node_t *node, int counter ) {
    // If the node type equals IDENTIFIER_DATA, insert it into the global_names hash
    if ( node->type == IDENTIFIER_DATA ) {
        // tlhash_insert( tlhash_t *tab, void *key, size_t key_length, void *value );
        symbol_t *symbol = make_symbol(node, counter, SYM_GLOBAL_VAR);
        tlhash_insert(global_names, symbol->name, strlen(symbol->name), symbol);
    }
    else if ( node->type == FUNCTION )
    {
        symbol_t *symbol = make_symbol(node, counter, FUNCTION);
        tlhash_insert(global_names, symbol->name, strlen(symbol->name), symbol);
    }
    else
    {
        for ( int i = 0; i < node->n_children; i++ )
        {
            if(node->children[i] != NULL)
            {
                traverse_subtree(node->children[i], counter);
                if ( node->children[i]->type == FUNCTION )
                {
                    counter++;
                }
            }
        }
    }
}

void
find_globals ( void )
{
    global_names = malloc ( sizeof(tlhash_t) );
    tlhash_init ( global_names, 32 );
    traverse_subtree( root, 0 );
}

int traverseBlockDFS(node_t *currentNode, tlhash_t *rootTable, tlhash_t *stack, int counter,
        bool nodeIsDeclaration, int nesting)
{
    if(currentNode->type == BLOCK)
    {
        nesting++;
        // printf("Inserting table at nest level %d\n", nesting);
        insertHashBlock(nesting, stack);
        for ( size_t i=0; i<currentNode->n_children; i++ )
        {
            if(currentNode->children[i] != NULL)
            {
                counter = traverseBlockDFS(currentNode->children[i], rootTable, stack,  counter, currentNode->type == VARIABLE_LIST , nesting);
            }
        }

        removeHashBlock(nesting, stack);
        // printf("Removing table at nest level %d\n", nesting);
        nesting--;
    }
    else if(currentNode->type == IDENTIFIER_DATA)
    {
        counter = processVariableNode(currentNode, rootTable, stack,  counter, nodeIsDeclaration, nesting);
    }
    else if(currentNode->type == STRING_DATA)
    {
        processStringNode(currentNode);
    }
    else
    {
        for ( size_t i=0; i<currentNode->n_children; i++ )
        {
            if(currentNode->children[i] != NULL)
            {
                counter = traverseBlockDFS(currentNode->children[i], rootTable, stack, counter, currentNode->type == VARIABLE_LIST , nesting);
            }
        }
    }
    return counter;
}

void
bind_names ( symbol_t *function, node_t *root )
{
    tlhash_t *hash_table;
    hash_table = malloc(sizeof(tlhash_t*));
    tlhash_init(hash_table, 1);
    if(string_list == NULL)
    {
        string_list = malloc(0);
    }
    for ( size_t i=0; i<root->n_children; i++ )
    {
        if(root->children[i] != NULL && root->children[i]->type == BLOCK)
        {
            traverseBlockDFS(root->children[i], function->locals, hash_table, 0, false, 0);
        }
    }
    //TODO: recursively
    free(hash_table);
}


void
destroy_symtab ( void )
{
    tlhash_finalize ( global_names );
    free ( global_names );
}


void
print_symbols ( void )
{
    printf ( "String table:\n" );
    for ( size_t s=0; s<stringc; s++ )
        printf  ( "%zu: %s\n", s, string_list[s] );
    printf ( "-- \n" );

    printf ( "Globals:\n" );
    size_t n_globals = tlhash_size(global_names);
    symbol_t *global_list[n_globals];
    tlhash_values ( global_names, (void **)&global_list );
    for ( size_t g=0; g<n_globals; g++ )
    {
        switch ( global_list[g]->type )
        {
            case SYM_FUNCTION:
                printf (
                    "%s: function %zu:\n",
                    global_list[g]->name, global_list[g]->seq
                );
                if ( global_list[g]->locals != NULL )
                {
                    size_t localsize = tlhash_size( global_list[g]->locals );
                    printf (
                        "\t%zu local variables, %zu are parameters:\n",
                        localsize, global_list[g]->nparms
                    );
                    symbol_t *locals[localsize];
                    tlhash_values(global_list[g]->locals, (void **)locals );
                    for ( size_t i=0; i<localsize; i++ )
                    {
                        printf ( "\t%s: ", locals[i]->name );
                        switch ( locals[i]->type )
                        {
                            case SYM_PARAMETER:
                                printf ( "parameter %zu\n", locals[i]->seq );
                                break;
                            case SYM_LOCAL_VAR:
                                printf ( "local var %zu\n", locals[i]->seq );
                                break;
                        }
                    }
                }
                break;
            case SYM_GLOBAL_VAR:
                printf ( "%s: global variable\n", global_list[g]->name );
                break;
        }
    }
    printf ( "-- \n" );
}


void
print_bindings ( node_t *root )
{
    if ( root == NULL )
        return;
    else if ( root->entry != NULL )
    {
        switch ( root->entry->type )
        {
            case SYM_GLOBAL_VAR: 
                printf ( "Linked global var '%s'\n", root->entry->name );
                break;
            case SYM_FUNCTION:
                printf ( "Linked function %zu ('%s')\n",
                    root->entry->seq, root->entry->name
                );
                break; 
            case SYM_PARAMETER:
                printf ( "Linked parameter %zu ('%s')\n",
                    root->entry->seq, root->entry->name
                );
                break;
            case SYM_LOCAL_VAR:
                printf ( "Linked local var %zu ('%s')\n",
                    root->entry->seq, root->entry->name
                );
                break;
        }
    } else if ( root->type == STRING_DATA ) {
        size_t string_index = *((size_t *)root->data);
        if ( string_index < stringc )
            printf ( "Linked string %zu\n", *((size_t *)root->data) );
        else
            printf ( "(Not an indexed string)\n" );
    }
    for ( size_t c=0; c<root->n_children; c++ )
        print_bindings ( root->children[c] );
}
