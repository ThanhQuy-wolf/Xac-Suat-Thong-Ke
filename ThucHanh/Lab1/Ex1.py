import itertools as itt

def permutationsWithoutRepetition(E, k):
    P = list(itt.permutations(E, k))
    return P

def printPermutation(E, k, num_code):
    print("%i-permutations of %s: " %(k,E))
    for i in num_code:
        print (i)

# Main
E = list(range(0, 10))
k = 4
n = len(E)

num_code = permutationsWithoutRepetition(E, k)
code_length = len(num_code)
printPermutation(E, k, num_code)
print("Size = ", "%i!/(%i-%i)! = " %(n,n,k), code_length)