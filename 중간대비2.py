while True:
    # 메뉴 문구 만들기
    print("--------------------------")
    print("1. 홀수 짝수 구분 프로그램")
    print("2. 3의 배수 확인 프로그램")
    print("--------------------------")
    # 메뉴 입력 받기
    select = input("메뉴를 선택해 주십시오.: ")
    # 1번 홀짝 구분 선택
    if select == "1":
        print("홀수 짝수 구분 프로그램을 선택 하셨습니다.")
        num = int(input("정수 값을 입력 하세요.: "))
        if num % 2 == 0:
            print(f"입력하신 값 {num} 짝수입니다.")
            break
        else:
            print(f"입력하신 값 {num} 홀수입니다.")
            break
    # 2번 3의 배수 확인 선택
    elif select  == '2':
        print("3의 배수 확인 프로그램을 선택 하셨습니다.")
        num = int(input("정수 값을 입력 하세요.: "))
        if num % 3 == 0:
            print(f"입력하신 값 {num}, 3의 배수입니다.")
            break
        else:
            print(f"입력하신 값 {num}, 3의 배수가 아닙니다.")
            break
    # 잘못된 입력
    else:
        print("입력하신 값 3은 유효하지 않은 메뉴 선택 값입니다. 메뉴 선택은 1과 2만 가능합니다.")

    
