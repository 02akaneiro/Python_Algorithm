#정수 N개로 이루어진 수열 A와 정수 X가 주어지며, 이때 A에서 X보다 작은 수를 모두 출력하는 프로그램
n, x = map(int,input().split()) #n과 x값의 공백을 구분하여 입력받음.
a = list(map(int,input().split())) #수열 a를 리스트로 입력받으며, 공백을 구분함.

for i in a : #수열 a를 순회하며
  if i < x : #x보다 작은 수를
    print(i,end=" ") #공백으로 출력함.