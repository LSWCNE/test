# 3개의 정수를 입력받는다
num1 = int(input("1번째 정수를 입력하세요: "))
num2 = int(input("2번째 정수를 입력하세요: "))
num3 = int(input("3번째 정수를 입력하세요: "))
# 입력 값이 모두 같으면, "모든 수가 같습니다." 출력
if num1 == num2 == num3:
    print("모든 수가 같습니다.")
    # 입력 값이 두 개가 같으면,
elif num1 == num2 or num1 == num3 or num2 == num3:   
# 1) "두 수가 같습니다." 출력
    print("두 수가 같습니다.")
# 2) 두 수도 출력    
    if num1 == num2:
        print(num1, num2)
    elif num1 == num3:
        print(num1, num3)
    else:
        print(num2, num3)

# 입력 값이 모두 다르면,
# 1) "모든 수가 다릅니다."
else:
    print("모든 수가 다릅니다.")
# 2) 가장 큰 값을 출력.
    print("가장 큰 값은",max(num1, num2, num3))