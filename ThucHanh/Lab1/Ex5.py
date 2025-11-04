import itertools as itt

man = list(range(1, 7))
woman = list(range(1, 10))

def combinationsE(E, k):
    return list(itt.combinations(E, k))

# Main
M = combinationsE(man, 3)
woM = combinationsE(woman, 2)
for idx, (m, wo_m) in enumerate(itt.product(M, woM), start=1):
    print("Order of subjects:", idx)
    
    people_map = {"man": m, "woman": wo_m}
    for role, group in people_map.items():
        print(f"{role}: {group}")
    print("----")
