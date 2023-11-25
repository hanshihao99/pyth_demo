# def user_info(name,age,wegit):
#     print(f"用户的姓名是:{name} ,年龄是:{age} ,体重是:{wegit}")

# user_info('小红',13,wegit=13)


# user_info('小白',13,wegit=14)

def add(x,y):
    return x + y


def test_fuc(fun,x,y):
    result = add(x,y)
    return result

re = test_fuc(add,1,11)
print(re)