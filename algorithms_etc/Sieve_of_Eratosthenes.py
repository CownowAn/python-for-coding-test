import math

n = 10000
array = [True for _ in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False

for i in range(2, n + 1):
    if array[i]:
        print(i, end=" ")
