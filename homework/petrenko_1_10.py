import math
S, R1 = [float(n) for n in input().split()]

S1 = math.pi*R1**2
S2 =  S1 - S
R2 = math.sqrt(S2/math.pi)

print(f"{R2:.2f}")