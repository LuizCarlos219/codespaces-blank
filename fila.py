N=int(input())

A = list(map(int, input().split()))
print(A)
B = list(reversed(A))
print(B)

C = 0
maior = B[0]
for i in range(1, N):
    if maior >= [i]:
      C += 1
    else:
       maior = B[i]
print(C)