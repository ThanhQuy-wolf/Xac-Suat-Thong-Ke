import itertools as itt
import math

M = list(range(1, 5))
P = list(range(1, 4))
C = list(range(1, 3))
L = list(range(1, 2))

def permutationsWithoutRepetition(E, k):
    return list(itt.permutations(E, k))

def factorialE(num):
    return math.factorial(num)



# Main
A = {'M', 'P', 'C', 'L'}
pos = factorialE(4)
pos_code = permutationsWithoutRepetition(A, 4)
book_code_math = permutationsWithoutRepetition(M, len(M))
book_code_physic = permutationsWithoutRepetition(P, len(P))
book_code_chesmit = permutationsWithoutRepetition(C, len(C))
book_code_language = permutationsWithoutRepetition(L, len(L))

for i in pos_code:
    print("Order of subjects:", i)
    for m, p, c, l in itt.product(book_code_math, book_code_physic, book_code_chesmit, book_code_language):
        book_map = dict(zip(i, [m, p, c, l]))
        for subject in i:
            print(f"{subject}: {book_map[subject]}")
        print("----")

    
print("Have %i different arrangements are possible for type of book" %pos)

total_arrangements = pos * len(book_code_math) * len(book_code_physic) * len(book_code_chesmit) * len(book_code_language)
print("Total number of different arrangements possible:", total_arrangements)
