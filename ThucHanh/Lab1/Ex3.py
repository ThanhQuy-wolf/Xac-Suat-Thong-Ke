import itertools as itt

A = {'W', 'B', 'R'}
k = 3
W = list(range(1, 9)) #White
B = list(range(1, 7)) #Black
R = list(range(1, 10)) #Red

def permutationsWithRepetition(E, k):
    return list(i for i in itt.product(E, repeat=k))
    

def permutationsWithoutRepetition(E, k):
    return list(itt.permutations(E, k))

        
def combinationsE(E, k):
    return list(itt.combinations(E, k))

def printPermutation(E, k, num_code):
    print("%i-permutations of %s: " %(k,E))
    for i in num_code:
        print (i)
        
# 3a
def Ex3_a():
    print("3A")
    U3 = permutationsWithRepetition(A, k)
    print(U3)
    len_U3 = len(U3)
    print("There are", len_U3, "codes.")


# 3b
def Ex3_b():
    print("3B")
    n = len(A)

    U3 = permutationsWithoutRepetition(A, k)
    len_U3 = len(U3)
    printPermutation(A, k, U3)
    print("Size = ", "%i!/(%i-%i)! = " %(n,n,k), len_U3)
    
# 3c
def Ex3_c():
    print("3C")
    totalDenominator = list(range(len(W) + len(B) + len(R)))
    denoSpace = combinationsE(totalDenominator, k)
    
    firstBall = len(W)
    secondBall = len(R)
    lastBall = len(totalDenominator) - 2
    numSpace = firstBall * secondBall * lastBall
    
    result = numSpace / len(denoSpace)
    print(result)

# Main
Ex3_a()
Ex3_b()
Ex3_c()