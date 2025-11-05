from fractions import Fraction;

def P(event, space):
    return Fraction(len(event & space), len(space))

# Câu a
S = {'MMM', 'MMF', 'MFM', 'FMM',
     'MFF', 'FMF', 'FFM', 'FFF'}

# Câu b
sampleSpace = 0
for s in S:
    sampleSpace += 1; 
    
print(f"The number of elements in the probability space 𝑆 is {sampleSpace}")

# Câu c
B = {s for s in S if 'F' in s}

# Câu d
A_B = {s for s in S if s.count('F') == 3}

# Câu e
P_B = P(B,S)
P_A_B = P(A_B, S)

P_A_with_B = P_A_B / P_B
print(P_A_with_B)