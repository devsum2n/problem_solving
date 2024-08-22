#백준>N과M(1)
def dfs(n, lst):
    if n ==M:
        ans.append(lst)
        return
    
    for j in range(1, N+1):
        if v[j] == 0:
            v[j] =1
            dfs(n+1, lst+[j])
            v[j] = 0
            
N, M = map(int, input().split())
ans = [] #정답 리스트를 저장할 리스트
v = [0]*(N+1) #중복 확인용

dfs(0, [])
for lst in ans:
    print(*lst)
