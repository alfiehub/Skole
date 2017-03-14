import numpy as np

observation_model = np.matrix('0.9 0.1; 0.2 0.8')
transition_model = np.matrix('0.7 0.3; 0.3 0.7')

#print(transition_model)
#print(observation_model)


def forward(evidence, previous_message):
    if evidence:
        observation_column = observation_model[:,evidence[-1]]

        # Convert the column to a 2d array, flatten it and convert it to a diagonal matrix
        O = np.diag(np.asarray(observation_column).flatten())

        # 15.12 from the book. Call recursively to get the previous message
        # Chop one off the start of evidence until it is empty
        next_message = O * np.transpose(transition_model) * forward(evidence[1:], previous_message)

        # Normalize and return the message!
        normalized = normalize(next_message)
        #print("Day: %d - %s" % (len(evidence), normalized.flatten()))
        return normalized
    else:

        # No more evidence, just return the original message
        # No need to normalize it either, as it should have been when originally passed in
        return previous_message

def normalize(matrix):
    return matrix / matrix.sum()

def backward(evidence, next_message):
    #print(evidence, next_message.flatten())
    if evidence:
        # Depending on whether or not an umbrella was observed, select a row from the observation model
        observation_column = observation_model[:,evidence[-1]]

        # Convert the column to a 2d array, flatten it and convert it to a diagonal matrix
        O = np.diag(np.asarray(observation_column).flatten())

        # 15.13 from the book. Call recursively to get the next message
        # Chop one off the end off evidence until evidence is empty
        return transition_model * O * backward(evidence[:-1], next_message)
    else:
        return next_message




def forward_backward(evidence, start_message):
    fw = [None]*(len(evidence)+1)
    bw = np.matrix('1.0; 1.0')
    sv = [None]*(len(evidence)+1)

    fw[0] = start_message
    # Use a for loop to generate all the forward messsages
    for i in range(1, len(evidence)+1):
        # Pass evidence[i-1:i] to prevent the rewriting the forward function
        # Also pass in the previous message, f[i-1], so that we can generate the next
        fw[i] = forward(evidence[i-1:i], fw[i-1])

    print('\nForward messages:')
    for i, f in enumerate(fw):
        print("f 1:%d - %s" %(i,f.flatten()))

    #print('This should be the same as the last fw msg')
    #print(fw[-1])
    #print(np.multiply(fw[-1], bw))
    #print(normalize(np.multiply(fw[-1], bw)))

    print('\nBackward messages:')
    for i in range(len(evidence), -1, -1):
        sv[i] = normalize(np.multiply(fw[i], bw))
        #print('Test')
        #print(fw[i].flatten(), bw.flatten(), np.multiply(fw[i], bw).flatten())
        bw = backward(evidence[i:i+1], bw)
        print("b %d:%d - %s" % (i+1, len(evidence)+1, bw.flatten()))

    return sv

def viterbi(evidence, rain_probability):
    # Start with finding probabilities for it being rain or not, depending on whether or not an umbrella has been observed
    # Multiply the probability for rain with the probability for observ

    # Get the observation column based on whether an umbrellas was observed or not
    # This column contains the probabilities for an umbrella being present, given that it is raining.
    # Multiply it by the probabilities for actually raining.
    probs = np.multiply(observation_model[:, evidence[0]], start_message)

    seq = []

    # Iterate over the rest of the evidence
    for ev in evidence[1:]:
        # Multiply the 
        trans_prob = transition_model * probs
        max_col_ixs = np.argmax(trans_prob)
        probs = observation_model[:, ev] * trans_prob.item(max_col_ixs)

        seq.append(max_col_ixs)

    seq.append(np.argmax(probs))
    seq.reverse()

    return seq

def viterbi2(evidence, inital_rain_prob):
    if evidence:
        observation_column = observation_model[:,evidence[-1]]

        # Convert the column to a 2d array, flatten it and convert it to a diagonal matrix
        O = np.diag(np.asarray(observation_column).flatten())

        # 15.12 from the book. Call recursively to get the previous message
        # Chop one off the start of evidence until it is empty
        next_message = O * np.transpose(transition_model) * forward(evidence[1:], previous_message)
    else:
        return initial_rain_prob




start_message = np.matrix('0.5; 0.5')


# Just for practical reasons, 0 means an umbrellas was observed, 1 means not.
evidence_1 = [0,0]
evidence_2 = [0,0,1,0,0]

print(viterbi(evidence_2, start_message))

#print(forward(evidence_1, start_message))
#smoothed_estimates = forward_backward(evidence_1, start_message)
#
#print('\nSmoothed estimates:')
#for i, e in enumerate(smoothed_estimates):
#    print("Day: %d %s" %(i, e.flatten()))
#
#
##for i in range(len(evidence_2), -1, -1):
##    print(backward(evidence_2[i:], np.matrix('1.0; 1.0')).flatten())
#
#smoothed_estimates = forward_backward(evidence_2, start_message)
#
#print('\nSmoothed estimates:')
#for i, e in enumerate(smoothed_estimates):
#    print("Day: %d %s" %(i, e.flatten()))
#
#
