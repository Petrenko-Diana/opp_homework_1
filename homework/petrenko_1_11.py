a, b, c, d, f = [float(n) for n in input().split()]

P1 = a + b + f
P2 = d + c + f
p1 = P1 / 2
p2 = P2 / 2
S1 = (p1*(p1-a)*(p1-b)*(p1-f))**0.5
S2 = (p2*(p2-d)*(p2-c)*(p2-f))**0.5
S = S1 + S2
print(f"{S:.4f}")