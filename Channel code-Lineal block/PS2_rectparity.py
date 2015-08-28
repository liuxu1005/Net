# template for 6.02 rectangular parity decoding using error triangulation
import PS2_tests
import numpy

def rect_parity(codeword,nrows,ncols): 
    ## YOUR CODE HERE
    ## return the corrected data
    erro = []
    errty = []
    rlt = codeword[0:nrows * ncols]
    #calculate E_row
    for row in range(nrows):
        E = 0
        for col in range(ncols):
            E = (E + codeword[row * ncols + col])% 2
        E = (E + codeword[nrows * ncols + row]) %2
        erro.append(E)
    #calculate E_col
    for col in range(ncols):
        E = 0
        for row in range(nrows):
            E = (E + codeword[row * ncols + col])%2
        E = (E + codeword[nrows * ncols + nrows + col])%2
        erro.append(E)
    #detemine erro type
    for e in range(nrows):
        if erro[e] == 1 :
            errty.append(e)
    if len(errty) != 1 :
        return rlt
    e = e + 1
    while e < (nrows + ncols):
        if erro[e] == 1 :
            errty.append(e - nrows)
        e = e + 1
    if len(errty) > 2 :
        return rlt
    #correct result according to erro type
    if len(errty) == 0:
        return rlt
     
    for i in range(nrows + ncols) :
        if cmp(errty, [i]) == 0:
            return rlt
         
    for j in range(nrows) :
        for k in range(ncols) :
            if cmp(errty, [j, k]) == 0:
                rlt[j * ncols + k] = 1 - rlt[j * ncols + k]
                return rlt
    return rlt
                

if __name__ == '__main__':
    PS2_tests.test_correct_errors(rect_parity)
