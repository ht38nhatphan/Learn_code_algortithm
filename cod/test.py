n, S = map(int, input().split())
w = list(map(int, input().split()))
dp = [0] * (S + 1)
dp[0] = 0
dp1 = []
dp1.append([0]) 
for P in range(1, S + 1):
    dp[P] = min(dp[P - x] for x in w if x <= P) + 1
    for i in range(len(w)):
        if P == w[i]:
            g = []
            g.append(w[i])
            dp1.append(g)
            break
        elif P!=w[i] and P<=w[i]:
            g = []
            g.append(dp1[P-1])
            g.append(dp1[P-w[i-1]]) 
            dp1.append(g)
            break
print(dp1)
print(dp[S])