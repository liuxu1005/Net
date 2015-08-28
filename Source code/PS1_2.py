# template file for 6.02 PS1, Python Task 2
import numpy,random
import PS1_tests
from PS1_1 import huffman

# arguments:
#   encoding_dict -- dictionary mapping characters to binary encodings,
#                    as provided by your huffman procedure from PS1_1
#   encoded_message -- a numpy array of 0's and 1's representing the encoded message
# return:
#   a list of decoded symbols
def decode(encoding_dict,encoded_message):
    """
    Example:
    encoding_dict: {'A': [1, 1], 'C': [1, 0, 0], 'B': [0], 'D': [1, 0, 1]}
    encoded_msg: [1, 1, 0, 1, 0, 0, 1, 0, 1]
    returns 'ABCD'
    """
    # Your code here
    rlt = []
    length = len(encoded_message)
    symbol = []
    index = 0
    while length > index :
        symbol.append(encoded_message[index])
        count = 0
        for k in encoding_dict :
            if compare(encoding_dict[k], symbol) :
                rlt.append(k)
                symbol = []
                index = index + 1
                break
            else :
                count = count + 1
        if count == len(encoding_dict) :
            index = index + 1
            
    return rlt
def compare(a, b) :
    if len(a) != len(b) :
        return False
    for i in range(len(a)) :
        if a[i] != b[i] :
            return False
    return True

if __name__ == '__main__':
    # start by building Huffman tree from probabilities
    plist = ((0.34,'A'),(0.5,'B'),(0.08,'C'),(0.08,'D'))
    cdict = huffman(plist)

    # test case 1: decode a simple message
    message = ['A', 'B', 'C', 'D']
    encoded_message = PS1_tests.encode(cdict,message)
    decoded_message = decode(cdict,encoded_message)
    assert message == decoded_message, \
           "Decoding failed: expected %s, got %s" % \
           (message,decoded_message)

    # test case 2: construct a random message and encode it
    message = [random.choice('ABCD') for i in xrange(100)]
    encoded_message = PS1_tests.encode(cdict,message)
    decoded_message = decode(cdict,encoded_message)
    assert message == decoded_message, \
           "Decoding failed: expected %s, got %s" % \
           (message,decoded_message)

    print "Tests passed!"
