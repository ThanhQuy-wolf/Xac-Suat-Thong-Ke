from fractions import Fraction

def P(event, space):
    return Fraction(len(event & space), len(space))

S = {('Thanh', 'Nữ'), ('Hồng', 'Nữ'), ('Thương', 'Nữ'), ('Đào', 'Nữ'), ('My', 'Nữ'), ('Yến', 'Nữ'), ('Hạnh', 'Nữ'),
 ('My', 'Nữ'), ('Vy', 'Nữ'), ('Tiên', 'Nữ'), ('Thanh', 'Nam'), ('Thanh', 'Nam'), ('Bình', 'Nam'), ('Nhật', 'Nam')
 , ('Hào', 'Nam'), ('Đạt', 'Nam'), ('Minh', 'Nam')}

# Câu a
A = {s for s in S if 'Thanh' in s}

# Câu b
B = {s for s in S if 'Nữ' in s}

# Câu c
A_B = A & B

# Câu d
P_A = P(A, S)
P_B = P(B,S)
P_A_B = P(A_B, S)

# Câu e
P_A_with_B = P_A_B / P_B
print(P_A_with_B)