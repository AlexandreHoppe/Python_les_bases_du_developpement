# Considérons : A = 13 / B = 5 / C = True / D = not(C). Donnez le résultat pour chacune de ces instructions :
# A > 10) and (B < 20)
# (C != 40) or (D >= 100)
# (A == 2) and (not (B > 15))
# (C > 50) or (not (D < 200))
# ((A < B) and (C > 30)) or (D == 270)
# not ((A * B) > 100)
# ((B == 15) or ((C > 60) and (A < 5)))
# (((B == 15) or ((C > 60) and (A < 5))) and (A < B)) or (not (B == 9)) 

# True
# True
# False
# True | False
# False
# True
# False
# True

a = 13 
b = 5 
c = True 
d = not(c)

print((a > 10) and (b < 20))
print((c != 40) or (d >= 100))
print((a == 2) and (not (b > 15)))
print((c > 50) or (not (d < 200)))
print(((a < b) and (c > 30)) or (d == 270))
print(not ((a * b) > 100))
print(((b == 15) or ((c > 60) and (a < 5))))
print((((b == 15) or ((c > 60) and (a < 5))) and (a < b)) or (not (b == 9)))