# 무한 입력
while True: # 조건이 True이면 반복
    try: # 실행 할 코드
        a, b = map(int, input().split())
        print(a + b)
    except: # 에러가 났을 시(예외 발생)
        break # 종료