#백준/ N과 M(2)
def dfs(n, lst):
    if n>N:
        if len(lst) == M:
            ans.append(lst)
        return 
    
    dfs(n+1, lst+[n])
    dfs(n+1, lst)


N, M = map(int, input().split())
ans = []
dfs(1, [])
for lst in ans:
    print(*lst)

# 멀티 트리 구현
# def dfs(n, s, lst):
#     if n == M:
#         ans.append(lst)
#         return
#     for j in range(s, N+1):
#         dfs(n+1, j+1, lst+[j])
# N, M = map(int, input().split())
# ans = []
# dfs(0, 1, [])
# for lst in ans:
#     print(*lst)
