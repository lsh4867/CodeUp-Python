d = [[0] * 11 for _ in range(11)]

for i in range(1, 11):
  a = list(map(int, input().split()))
  for j in range(1, 11):
    d[i][j] = a[j - 1]

x, y = 2, 2
while True:
  if d[x][y] == 0:
    d[x][y] = 9
  elif d[x][y] == 2:
    d[x][y] = 9
    break
  if (d[x][y + 1] == 1 and d[x + 1][y] == 1) or (x == 9 and y == 9):
    break
  if d[x][y + 1] != 1:
    y += 1
  elif d[x + 1][y] != 1:
    x += 1

for i in range(1, 11):
  print(' '.join(map(str, d[i][1:11])))
