# list comprehension: 2차원 리스트 초기화 form
d = [[0] * 20 for _ in range(20)]

# 2차원 리스트 값 입력 form
for i in range(1,20):
  a = list(map(int, input().split()))
  for j in range(1,20):
    d[i][j] = a[j-1]

# 핵심!: 바둑알 뒤집기 method
n = int(input())
for _ in range(n):
  x, y = map(int, input().split())
  for j in range(1,20):
    d[x][j] = 1 - d[x][j]
    d[j][y] = 1 - d[j][y]

# 2차원 리스트 출력 form(1)
for i in range(1, 20):
  print(' '.join(map(str, d[i][1:20])))

# 2차원 리스트 출력 form(2-정석)
for i in range(1, 20) :
  for j in range(1, 20) :
    print(d[i][j], end=' ')
  print()
