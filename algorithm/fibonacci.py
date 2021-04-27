import sys
import collections
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
dp = collections.defaultdict(int)

# Tabulate
def fib(n):
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(fib(N))
