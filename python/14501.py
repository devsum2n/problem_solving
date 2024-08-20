#백준/퇴사

# def dfs(n, sm):
#     global ans
#     #종료조건
#     if n>= N:
#         ans = max(ans, sm)
#         return
#     #하부호출
#     if n+T[n] <= N: #상담하는 경우(퇴사일 전)
#         dfs(n+T[n], sm+P[n])
#     dfs(n+1, sm) #상담을 못하는 경우    

N = int(input())
T = [0]*N
P = [0]*N
for i in range(N):
    T[i], P[i] = map(int, input().split())
# ans = 0 #최대 수익

# dfs(0, 0)

dp = [0]*(N+1)
for n in range(N-1, -1, -1): #뒤에서 앞으로(완료기준)
    if n+T[n] <=N:
        dp[n] = max(dp[n+1],dp[n+T[n]+P[n]])
    else:
        dp[n]= dp[n+1]
print(dp[0])
