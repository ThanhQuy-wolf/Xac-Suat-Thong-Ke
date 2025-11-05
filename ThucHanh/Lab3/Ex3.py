from fractions import Fraction
import itertools as itt
import math

def P(event, space):
    return Fraction(len(event), len(space))

# Câu a
suits_symbols = {'spades': '♠', 'clubs': '♣', 'diamonds': '♦', 'hearts': '♥'}
suits = list(suits_symbols.keys())
ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

deck = [f"{r}{suits_symbols[s]}" for r in ranks for s in suits]

# Câu b
S = set(itt.combinations(deck, 3))
space_size = len(S)

# Câu c
def count_kings(hand):
    return sum(1 for card in hand if card[:-1] == 'K')
A1 = {hand for hand in S if count_kings(hand) in (1, 2)}

# Câu d
A2 = {hand for hand in S if count_kings(hand) >= 1}

# Câu e
P_A1 = P(A1, S)
P_A2 = P(A2, S)

# A1: exactly 1 K => C(4,1)*C(48,2); exactly 2 K => C(4,2)*C(48,1)
calc_A1 = math.comb(4,1) * math.comb(48,2) + math.comb(4,2) * math.comb(48,1)
# A2: at least 1 K = total - no K = C(52,3) - C(48,3)
calc_A2 = space_size - math.comb(48, 3)

# In kết quả
print(f"|S| = {space_size}")
print(f"|A1| = {len(A1)}  => P(A1) = {P_A1} ≈ {float(P_A1):.4f}")
print(f"|A2| = {len(A2)}  => P(A2) = {P_A2} ≈ {float(P_A2):.4f}")