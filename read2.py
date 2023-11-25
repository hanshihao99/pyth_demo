# 将 file文件中的内容写到另一份名字为 readBack.txt 的文件，并且将带有测试的数据剔除掉

# 打开文件得到文件对象，准备获取
fr =  open('/Users/hanshihao/Desktop/fileDemo.txt','r')

# 打开准备写入的文件
fw = open('/Users/hanshihao/Desktop/fileDemoBack.txt','w')

# for循环读取文件
for line in fr:
    line = line.strip()
    # 判断内容，将满足的内容写出
    if line.split(',')[1] == '测试':
        continue

    # 将内容写出去
    fw.write(line)
    # 由于内容进行了 strip() 的操作，所以要手动的写出换行符
    fw.write('\n')

# close 两个文件对象
fr.close()
fw.close()