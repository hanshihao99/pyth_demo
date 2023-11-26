import random
import datetime

start_date = datetime.date(2021, 1, 1)
end_date = datetime.date(2021, 10, 31)
province_list = ['江苏省', '浙江省', '北京市', '上海市', '广东省', '陕西省', '山西省', '山东省', '河北省', '河南省', '甘肃省']  # 你可以根据需要修改省份列表

output_file = '/Users/hanshihao/Downloads/2021全国订单数据.csv'

with open(output_file, 'w') as file:
    file.write('日期,订单id,金额,省份\n')  # 写入CSV文件的标题行

    for single_date in (start_date + datetime.timedelta(n) for n in range((end_date - start_date).days + 1)):
        for _ in range(10):  # 每天生成10条数据
            order_id = ''.join(
                random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(16))  # 随机生成订单ID
            amount = random.randint(1, 100)  # 随机生成金额
            province = random.choice(province_list)  # 随机选择省份

            data = f"{single_date.strftime('%Y-%m-%d')},{order_id},{amount},{province}\n"
            file.write(data)

print("数据已成功保存到文件:", output_file)