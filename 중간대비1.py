# 사용자로부터 첫번째 실수, 두번째 실수, 연산자, 결과값 자료형 입력받음
num1 = str(input("첫 번째 값을 입력하세요.: "))
if "." in num1:
    num1 = float(num1)
else:
    num1 = int(num1)
num2 = str(input("두 번째 값을 입력하세요.: "))
if "." in num2:
    num2 = float(num2)
else:
    num2 = int(num2)
Arithmetic = input("연산자를 선택하세요. (+, -, *, / 중 하나 입력): ")
s_type = input("결과값 자료형(integer, float, string 중 하나 입력): ")

# 연산방법 정의
plus = num1 + num2
minus = num1 - num2 
mulp = num1 * num2
div = num1 / num2

# 입력받은 자료형에 따라 결과값 변환 및 연산
if s_type == "integer":
    if Arithmetic == "+":
        result = int(plus)
    elif Arithmetic == "-":
        result = int(minus)
    elif Arithmetic == "*":
        result = int(mulp)
    else:
        result = int(div)
    print(f"{num1} {Arithmetic} {num2} = {result}")

elif s_type == "float":
    if Arithmetic == "+":
        result = float(plus)
    elif Arithmetic == "-":
        result = float(minus)
    elif Arithmetic == "*":
        result = float(mulp)
    else:
        result = float(div)
    print(f"{num1} {Arithmetic} {num2} = {result}")

elif s_type == "string":
    if Arithmetic == "+":
        result = str(plus)
    elif Arithmetic == "-":
        result = str(minus)
    elif Arithmetic == "*":
        result = str(mulp)
    else:
        result = str(div)
    print(f"{num1} {Arithmetic} {num2} = {result}")