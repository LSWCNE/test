# 생성할 랜덤 정수의 개수N을 입력. (N은 1이상 100이하의 정수여야 한다.)
# 입력받은 N에 따라, 1부터 100까지의 숫자 중 중복되지 않은 N개의 랜덤 숫자를 생성합니다.
# 생성된 랜덤 숫자들은 리스트에 저장됩니다.
# 사용자에게 리스트에서 원하는 원소의 인덱스를 입력받습니다. (인덱스는 0부터 N-1까지의 값이어야 합니다.)
# 프로그램은 사용자가 선택한 인덱스에 해당하는 리스트의 원소를 출력합니다.

import random

# 생성할 랜덤 정수의 개수N을 입력. (N은 1이상 100이하의 정수여야 한다.)
while True:
    N = int(input("N값을 입력하세요 (1-100): "))
    if 0 < N < 101:
        break
    else:
        print("에러: N은 1 이상 100 이하의 정수여야 합니다.")

# # 입력받은 N에 따라, 1부터 100까지의 숫자 중 중복되지 않은 N개의 랜덤 숫자를 생성합니다
# random_numbers = []

# for _ in range(N): 
#     random_number = random.randint(1, 100)
#     # 생성된 랜덤 숫자들은 리스트에 저장됩니다. 
#     random_numbers.append(random_number)
#     # 생성된 랜덤 숫자 리스트 출력
# print("생성된 리스트:", random_numbers)

random_numbers = []
while len(random_numbers) < N:
    random_number = random.randint(1, 100)
    for num in random_numbers:
        if num == random_number:
            break
    else:
        random_numbers.append(random_number)
# 생성된 랜덤 숫자 리스트 출력
print("생성된 리스트:", random_numbers)

# 사용자로부터 원하는 원소의 인덱스 입력받기
while True:
    index = int(input("원하는 원소의 인덱스를 입력해 주세요 (0-" + str(N-1) + ") : "))
    if 0 <= index < N:
        break
    else:
        print("에러: 유효한 인덱스 범위를 벗어났습니다.")

# 선택한 인덱스의 원소 출력
print("선택한 인덱스의 원소:", random_numbers[index])

# random_numbers = []
# while len(random_numbers) < N:
#     random_number = random.randint(1, 100)
#     for num in random_numbers:
#         if num == random_number:
#             break
#     else:
#         random_numbers.append(random_number)