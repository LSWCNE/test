# 사용자로부터 정보 입력받기
# 초기 자본금
jaborn = int(input("초기 자본금을 입력하세요: "))

# 주식 구매 가격
jusick = int(input("주식 가격을 입력하세요: "))  

# 구매할 주식 수
buy_jusick = int(input("구매할 주식 수를 입력하세요: "))  

# 판매할때 주식 가격
sell_jusick = int(input("판매할 때의 주식가격을 입력하세요: ")) 

# 주식 구매 비용 계산식
total_buy_jusick = jusick * buy_jusick

# 남은 자본금 계산
nam_is_jaborn = float(jaborn - total_buy_jusick)
print("구매 후 남은 자본금:", nam_is_jaborn)

# 예상 이익 계산
salddae = float(jusick * buy_jusick)
palddae = float(sell_jusick * buy_jusick)
dducksang_gazua = palddae - salddae 
print("예상 이익:", dducksang_gazua)

# 결과 출력
if jusick > sell_jusick:
    print("예상되는 이익입니다.")
else:
    print("예상되는 손실입니다.")
# import tkinter as tk

# # GUI 생성
# root = tk.Tk()
# root.title("주식 이익 계산기")

# # 레이블 및 입력 위젯 생성
# label_jaborn = tk.Label(root, text="초기 자본금을 입력하세요:")
# label_jaborn.pack()

# entry_jaborn = tk.Entry(root)
# entry_jaborn.pack()

# label_jusick = tk.Label(root, text="주식 가격을 입력하세요:")
# label_jusick.pack()

# entry_jusick = tk.Entry(root)
# entry_jusick.pack()

# label_buy_jusick = tk.Label(root, text="구매할 주식 수를 입력하세요:")
# label_buy_jusick.pack()

# entry_buy_jusick = tk.Entry(root)
# entry_buy_jusick.pack()

# label_sell_jusick = tk.Label(root, text="판매할 때의 주식가격을 입력하세요:")
# label_sell_jusick.pack()

# entry_sell_jusick = tk.Entry(root)
# entry_sell_jusick.pack()

# def calculate_profit():
#     # 사용자 입력 값 가져오기
#     jaborn = int(entry_jaborn.get())
#     jusick = int(entry_jusick.get())
#     buy_jusick = int(entry_buy_jusick.get())
#     sell_jusick = int(entry_sell_jusick.get())
    
#     # 주식 구매 비용 계산
#     total_buy_jusick = jusick * buy_jusick
    
#     # 남은 자본금 계산
#     nam_is_jaborn = jaborn - total_buy_jusick
#     label_nam_is_jaborn.config(text=f"구매 후 남은 자본금: {nam_is_jaborn}")
    
#     # 예상 이익 계산
#     salddae = jusick * buy_jusick
#     palddae = sell_jusick * buy_jusick
#     dducksang_gazua = palddae - salddae 
#     label_dducksang_gazua.config(text=f"예상 이익: {dducksang_gazua}")

# # 계산 버튼 생성
# calculate_button = tk.Button(root, text="계산하기", command=calculate_profit)
# calculate_button.pack()

# # 결과 출력 레이블
# label_nam_is_jaborn = tk.Label(root, text="")
# label_nam_is_jaborn.pack()

# label_dducksang_gazua = tk.Label(root, text="")
# label_dducksang_gazua.pack()

# root.mainloop()