A = int(input())
B = int(input())
C = int(input())
D = int(input())

E = C - A
F = C - B
E = E//D
F = F//D
if E == 0: E = 1
if F == 0: F = 1
E = (C - (A+E*D)) >= 0
F = (C - (A+F*D)) >= 0
if E or F:
    print('S')
else:
    print('N')