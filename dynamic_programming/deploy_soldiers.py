n = int(input())
array = list(map(int, input().split()))
# 순서를 뒤집어 'Logest Increasing Subsequence(LIS)'문제로 변환
array.reverse()

# 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
dp = [1] * n

# LIS 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
