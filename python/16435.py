#백준/스네이크버드
N, L = map(int,input().split())
fruits = list(map(int, input().split()))

fruits.sort()

for i in range(N):
    if L >= fruits[i]:
        L += 1
    else:
        break

print(L)
