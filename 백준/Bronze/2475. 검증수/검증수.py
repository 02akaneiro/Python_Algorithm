result = 0

num = list(map(int, input().split()))

for i in range(len(num)):
  a = num[i]
  result += a**2
print(result % 10)