N = int(input())
A = []
for i in range(0, N):
    try:
        a = int(input())
        A.append(a)
    finally:
        pass

B = []
for i in A:
    if i % 2 == 0:
        B.append(i)
C = []
for i in B:
    C.append(i * 2)
for i in C:
    print(i, end=" ")
