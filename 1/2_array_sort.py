from random import randint
import time

# array에 1~100 사이의 랜덤한 정수 10000개 삽입
array = []

for _ in range(10000):
  array.append(randint(1, 100))
  
# 선택 정렬 프로그램 성능 측정 시작
start_time = time.time()

# 선택 정렬 프로그램 소스코드
for i in range(len(array)):
  min_index = i
  for j in range(i+1, len(array)):
    if array[j] < array[min_index]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i] # swap
  
end_time = time.time() # 측정 종료
print("선택 정렬 성능 측정: " end_time - start_time)

# 배열 재초기화
array = []
for _ in range(10000):
  array.append(randint(1, 100))
  
# 기본 정렬 라이브러리 성능 측정 시작
start_time = time.time()

# 기본 정렬 라이브러리 사용
array.sort()

end_time = time.time()
print("기본 정렬 성능 측정: ", end_time - start_time)
