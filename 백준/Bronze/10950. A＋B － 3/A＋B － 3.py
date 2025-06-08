t = int(input()) #테스트 케이스를 정수로 입력

for i in range(t) : # t번 째 반복문 실행 후 종료
  a, b = map(int,input().split()) #정수 a, b를 공백 구분하여 입력
  print(a + b)