# 생성할 랜덤 정수의 개수N을 입력. (N은 1이상 100이하의 정수여야 한다.)
# 입력받은 N에 따라, 1부터 100까지의 숫자 중 중복되지 않은 N개의 랜덤 숫자를 생성합니다.
# 생성된 랜덤 숫자들은 리스트에 저장됩니다.
# 사용자에게 리스트에서 원하는 원소의 인덱스를 입력받습니다. (인덱스는 0부터 N-1까지의 값이어야 합니다.)
# 프로그램은 사용자가 선택한 인덱스에 해당하는 리스트의 원소를 출력합니다.

import random # random 모듈 활성화

while True:
    N = int(input("1이상 100이하의 정수를 입력: ")) # 사용자로부터 1이상 100이하의 정수를 입력받기
    if 0 < N < 101: # 입력받은 값이 1이상 100이하의 정수라면 반복 멈춤
        break
    print("1이상 100이하의 숫자를 입력하세요.") # 1이상 100이하의 정수가 아니라면 오류메시지 출력 후 다시 받기

random_nums = [] # 랜덤 숫자들이 저장될 리스트 생성
while len(random_nums) < N: # 리스트 크기가 입력받은 정수 N이하일때 계속 반복
    random_num = random.randint(1, 100) # 1부터 100사이의 정수를 무작위 호출
    for num in random_nums: # 호출받은 숫자 num이 리스트 안에서
        if num == random_num: # 호출받은 숫자와 같으면 정수를 다시 호출
            break
    random_nums.append(random_num) # 리스트안에 있는 정수와 다른 정수라면 리스트에 추가
print(f"생성된 리스트: {random_nums}")

while True:
    index = int(input(f"원하는 원소의 인덱스를 입력해 주세요 (0-{N-1}): "))
    if 0 <= index < N:
        break
    print("에러: 유효한 인덱스 범위를 벗어났습니다.")
print(f"선택한 인덱스의 원소: {random_nums[index]}")