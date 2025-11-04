import itertools as itt

def permutationsWithoutRepetition(E, k):
    P = list(itt.permutations(E, k))
    return P

def printPermutation(E, k, num_code):
    print("%i-permutations of %s: " %(k,E))
    for i in num_code:
        print (i)

# Main
A = list(range(1, 6))
k = 3
n = len(A)

num_3_digit = permutationsWithoutRepetition(A, k)
num_length = len(num_3_digit)

printPermutation(A, k, num_3_digit)
print("Size = ", "%i!/(%i-%i)! = " %(n,n,k), num_length)