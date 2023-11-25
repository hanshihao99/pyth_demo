import time
with open('/Users/hanshihao/Downloads/test.txt','r') as f:
    content = f.read()


count = content.count('helloo')
print(f"hello的统计字数为:{count} , 读取的文件内容为:{content}")

