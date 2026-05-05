# Devinez les résultats des calculs sur les valeurs des variables A, B, C, D, E, F et G à partir des expressions suivantes :

# A = 12
# B = 3 * A + 8
# C = B - 2 * A
# D = (C + 25) * B
# E = (A + B) % 10
# F = (C * D) // (B + 6)
# G = (D + E) // (F - 9)

# a = 12
# b = 44
# c = 20
# d = 45 * 44 = 1980
# e = 56 % 10 = 6
# f = 39600 // 50 = 792
# g = 1986 // 783 = 2

a = 12
b = 3 * a + 8
c = b - 2 * a
d = (c + 25) * b
e = (a + b) % 10
f = (c*d) // (b+6)
g = (d+e) // (f-9)

print(a, b, c, d, e, f, g, sep='\n')