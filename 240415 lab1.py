# shopping_list 라는 이름의 빈 리스트를 생성합니다.
shopping_list = []
# 다음 품목들을 쇼핑리스트에 추가 'milk', 'bread', eggs', 'apple'.
shopping_list.append('milk')
shopping_list.append('bread')
shopping_list.append('eggs')
shopping_list.append('apple')
# print 함수를 사용하여 현재 쇼핑 리스트의 내용을 출력
print(f"현재 쇼핑 리스트: {shopping_list}")
# 쇼핑을 시작하기 전에 'toilet paper'가 빠져 있는 것을 발견하고 리스트의 맨 앞에 추가
shopping_list.insert(0, 'toilet paper')
# 이번에는 'orange juice'를 리스트의 두 번째 위치에 추가
shopping_list.insert(1, 'orange juice')
# 마지막으로 'chicken', 'rice'를 리스트에 추가하는데 이 두 품목을 한 번의 연산으로 리스트에 추가
shopping_list +=['chicken', 'rice']
# 각 단계 후에 쇼핑 리스트를 출력하여, 추가된 품목들을 확인
print (f"최종 쇼핑 리스트: {shopping_list}")