n = int(input()) # 숫자의 개수를 입력받음
num = input() # 더할 숫자를 공백없이 문자열로 입력받음
nums = [int(ch) for ch in num] # 문자열에서 한 글자씩 꺼내 숫자로 변환 후 리스트로 저장
print(sum(nums)) # 리스트에 저장된 숫자를 모두 더하여 출력