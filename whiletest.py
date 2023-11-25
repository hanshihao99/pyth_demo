import random


num = random.randint(1,100)
print(num)

count = 0

flag = True

while flag:

    address_num = int(input("请输入猜测的数字: "))
    count += 1
    if address_num == num:
        print("恭喜，猜对了 ")
        flag = False
    else:
        if address_num > num :
            print("猜的数字大了")
        else:
            print("猜的数字小了")
    
print(f"您总共猜了{count} 次")