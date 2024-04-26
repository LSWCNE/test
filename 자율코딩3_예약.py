# 사용자로부터 기본정보 입력받기 

# 나이
age = int(input("나이를 입력하세요: "))

# 이벤트 코드
event_code = input("이벤트 코드를 입력하세요 (E1, E2, E3 중 하나): ")
if event_code != "E1" or event_code != "E2" or event_code != "E3":
    print("잘못된 입력입니다. 프로그램을 종료합니다")
else:
        
    # 날짜
    reservation_date = int(input("예약을 원하는 날짜를 입력하세요 (1~30): "))
    if reservation_date < 1 or reservation_date > 30:
        print("잘못된 입력입니다. 프로그램을 종료합니다")
    else:


        # E1 규칙 적용
        if event_code == 'E1':
            if age < 18:
                print("나이 제한으로 인해 예약할 수 없습니다.")
            else:
                print("예약이 완료되었습니다!")

        # E2 규칙 적용
        elif event_code == 'E2':
            if reservation_date % 2 == 0:
                print("예약이 완료되었습니다!")
            else:
                print("선택하신 날짜에는 예약할 수 없습니다.")

        # E3 규칙 적용
        elif event_code == 'E3':
            if age < 16:
                print("나이 제한으로 인해 예약할 수 없습니다.")
            elif reservation_date % 7 == 0:
                print("예약이 완료되었습니다!")
            else:
                print("선택하신 날짜에는 예약할 수 없습니다.")
# import tkinter as tk
# from tkinter import messagebox

# def make_reservation():
#     age = int(age_entry.get())
#     event_code = event_code_entry.get()
#     reservation_date = int(date_entry.get())

#     if event_code not in ["E1", "E2", "E3"]:
#         messagebox.showerror("Error", "잘못된 이벤트 코드입니다.")
#         return

#     if reservation_date < 1 or reservation_date > 30:
#         messagebox.showerror("Error", "잘못된 날짜입니다.")
#         return

#     if event_code == 'E1':
#         if age < 18:
#             messagebox.showinfo("안내", "나이 제한으로 인해 예약할 수 없습니다.")
#         else:
#             messagebox.showinfo("안내", "예약이 완료되었습니다!")

#     elif event_code == 'E2':
#         if reservation_date % 2 == 0:
#             messagebox.showinfo("안내", "예약이 완료되었습니다!")
#         else:
#             messagebox.showinfo("안내", "선택하신 날짜에는 예약할 수 없습니다.")

#     elif event_code == 'E3':
#         if age < 16:
#             messagebox.showinfo("안내", "나이 제한으로 인해 예약할 수 없습니다.")
#         elif reservation_date % 7 == 0:
#             messagebox.showinfo("안내", "예약이 완료되었습니다!")
#         else:
#             messagebox.showinfo("안내", "선택하신 날짜에는 예약할 수 없습니다.")

# # GUI 생성
# root = tk.Tk()
# root.title("이벤트 예약 시스템")

# # 나이 입력
# age_label = tk.Label(root, text="나이를 입력하세요:")
# age_label.pack()
# age_entry = tk.Entry(root)
# age_entry.pack()

# # 이벤트 코드 입력
# event_code_label = tk.Label(root, text="이벤트 코드를 입력하세요 (E1, E2, E3 중 하나):")
# event_code_label.pack()
# event_code_entry = tk.Entry(root)
# event_code_entry.pack()

# # 날짜 입력
# date_label = tk.Label(root, text="예약을 원하는 날짜를 입력하세요 (1~30):")
# date_label.pack()
# date_entry = tk.Entry(root)
# date_entry.pack()

# # 예약 버튼
# reserve_button = tk.Button(root, text="예약하기", command=make_reservation)
# reserve_button.pack()

# root.mainloop()