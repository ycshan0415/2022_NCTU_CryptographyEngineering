def Berlekamp_Massey_algorithm(sequence):
    length = len(sequence)
    seq = sequence[:]

    for i in range(length):
        if seq[i] == 1:
            break
    C = set([i + 1, 0])  # use a set to denote polynomial
    l = i + 1

    B = set([0])
    b = i
    m = 0

    for n in range(i + 1, length):
        d = 0
        for e in C:
            d ^= seq[e + n - l]

        if d == 0:
            m += 1
        elif 2 * l <= n:
            temp = C.copy()
            C = set([m - b + e for e in C]) ^ B
            l = n + 1 - l
            B = temp
            b = m
            m = n - l + 1
        else:
            C ^= set([b - m + e for e in B])
            m += 1
            

    # output the polynomial
    def print_poly(polynomial):
        result = ''
        lis = sorted(polynomial, reverse=True)
        for i in lis:
            if i == 0:
                result += '1'
            else:
                result += 'x^%s' % str(i)

            if i != lis[-1]:
                result += ' + '

        return result

    return print_poly(C), l

def dec2bin(seq):
    lis = []
    for e in seq:
        e %= 2
        lis.append(e)
    return lis

if __name__ == '__main__':
    # q1
    seq = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0,\
        1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1,\
        1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1,\
        1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0,\
        1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1] # b(x)
    poly = Berlekamp_Massey_algorithm(seq)[0]
    span = Berlekamp_Massey_algorithm(seq)[1]
    print('question 1')
    print ('characteristic polynomial:', poly) # c(x)
    print ('linear span:', span)
    
    #q3
    seq = [1, 1, 2, 3, 5, 8, 13, 21, 34] # b(x)
    seq = dec2bin(seq)
    poly = Berlekamp_Massey_algorithm(seq)[0]
    span = Berlekamp_Massey_algorithm(seq)[1]
    print('question 3')
    print ('characteristic polynomial:', poly) # c(x)
    print ('linear span:', span)
    
    