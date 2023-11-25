import random

num = random.randint(1,18)
print(num)
guess_num = int(input("请输入你猜测的数字: "))

if guess_num == num:
    print("恭喜你，第一次就猜中了")
else:
    if(guess_num > num):
        print("您猜的数字有点大哦～")
    else:
        print("您猜的数字有点小哦~")

    guess_num = int(input("请再次输入: "))

    if guess_num == num:
        print("恭喜你，第二次就猜中了")
    else:
        if(guess_num > num):
            print("您猜的数字有点大")
        else:
            print("您猜的数字有点小")

        guess_num = int(input("请最后输入一次: "))

        if guess_num == num:
            print("恭喜你，第三次猜中了")
        else:
            print("三次机会用完了，没有猜中")