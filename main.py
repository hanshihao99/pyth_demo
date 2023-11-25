print("欢迎你来到黑马儿童游乐场，儿童免费，成人收费")
age = input("请输入你的年龄: ")
if int(age) >= 18:
    print("您已成年，游玩需要补票10元")
else:
    print("儿童免费")
print("祝您游玩愉快")