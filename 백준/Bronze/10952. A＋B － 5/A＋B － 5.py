while True : # 조건이 참일 시 반복 (무한 반복)
  a, b = map(int,input().split()) # 공백을 구분하여 정수 입력받음.
  if (a == 0 and b == 0) : # 입력한 a와 b가 모두 0일 시
    break # 종료함.
  print(a + b)