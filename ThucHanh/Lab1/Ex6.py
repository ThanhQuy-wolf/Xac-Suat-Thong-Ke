import itertools as itt

suits = ["spades", "clubs", "diamonds", "hearts"]
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# Câu a
poker_5 = list(itt.product(cards, suits))
len_poker_5 = len(poker_5)
poker_5_str = [f"{rank} of {suit}" for rank, suit in poker_5]


print("Total cards:", len_poker_5)
for c in poker_5_str[:8]:
    print(c)

# Câu b
three_kind_any = []
for rank in cards:
    for suit_combo_3 in itt.combinations(suits, 3):
        triple = [(rank, s) for s in suit_combo_3]
        available = [(r, s) for (r, s) in poker_5 if r != rank]
        for k1, k2 in itt.combinations(available, 2):
            hand = tuple(triple + [k1, k2])
            three_kind_any.append(hand)

len_three_kind_any = len(three_kind_any)
print("Total three-of-a-kind:", len_three_kind_any)
for h in three_kind_any[:8]:
    print(h)
    
