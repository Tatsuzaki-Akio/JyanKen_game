import random
import customtkinter as ctk

ctk.set_appearance_mode("light")


def rd():
    im = random.randint(0, 2)
    return im


root = ctk.CTk()
root.title("じゃんけんゲーム")
root.geometry("500x300")

label = ctk.CTkLabel(root, text="じゃんけんゲーム", font=("Arial", 20))
label.pack(pady=20)

result_label = ctk.CTkLabel(root, text="", font=("Arial", 18))
result_label.pack(pady=10)


def play(user_hands):
    hands = ["グー", "チョキ", "パー"]
    cpu = rd()
    cpu_hands = hands[cpu]

    if user_hands == cpu:
        result = "あいこ"
    elif (
        (user_hands == 0 and cpu == 1)
        or (user_hands == 1 and cpu == 2)
        or (user_hands == 2 and cpu == 0)
    ):
        result = "あなたの勝ち"
    else:
        result = "あなたの負け"

    result_label.configure(text=f"CPU:\n{cpu_hands}\n{result}")


frame = ctk.CTkFrame(root)
frame.pack()
btn_goo = ctk.CTkButton(frame, text="グー", command=lambda: play(0))
btn_goo.pack(side="left", pady=10)
btn_cyoki = ctk.CTkButton(frame, text="チョキ", command=lambda: play(1))
btn_cyoki.pack(side="left", pady=10)
btn_paa = ctk.CTkButton(frame, text="パー", command=lambda: play(2))
btn_paa.pack(side="left", pady=10)

root.mainloop()

# hands = int(input("1.グー\n2.チョキ\n3.パー\nあなたの出す手は？:"))

# cpu = rd()

# if hands == 1:
#     print("グー")
#     if cpu == 1:
#         print("あいこ")
#     elif cpu == 2:
#         print("あなたの勝ち")
#     else:
#         print("あなたの負け")

# elif hands == 2:
#     print("チョキ")
#     if cpu == 1:
#         print("あなたの負け")
#     elif cpu == 2:
#         print("あいこ")
#     else:
#         print("あなたの勝ち")

# elif hands == 3:
#     print("パー")
#     if cpu == 1:
#         print("あなたの勝ち")
#     elif cpu == 2:
#         print("あなたの負け")
#     else:
#         print("あいこ")

# else:
#     print("有効な数字を入力してください")

# hands_list = ["グー", "チョキ", "パー"]
# if hands in [1, 2, 3]:
#     print(f"CPUは{hands_list[cpu - 1]}を出しました")
