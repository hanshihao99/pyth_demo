from data_define import Record
from file_define import FileReader, TextFileReader
from collections import defaultdict
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

textFile = TextFileReader('/Users/hanshihao/Downloads/2021全国订单数据.csv')
text_list: list[Record] = textFile.read_data()
#
# # 创建一个字典，用于存储每个日期的累计金额
# date_amount_dict = defaultdict(int)
#
# # 累加每个日期的金额
# for record in text_list:
#     date_amount_dict[record.date] += record.money
#
# # 提取日期和金额数据，用于绘制柱状图
# dates = list(date_amount_dict.keys())
# amounts = list(date_amount_dict.values())
#
# bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
# bar.add_xaxis(dates)
# bar.add_yaxis("销售额", amounts, label_opts=LabelOpts(is_show=False))
# bar.set_global_opts(title_opts=TitleOpts(title="每日销售额"))
#
# bar.render("每日销售额柱状图.html")


# 创建一个字典，用于存储每个日期下每个省市的累计金额
date_province_amount_dict = defaultdict(lambda: defaultdict(int))

# 累加每个日期下每个省市的金额
for record in text_list:
    date = record.date
    province = record.province
    amount = record.money
    date_province_amount_dict[date][province] += amount

# 提取日期和各个省市金额数据，用于绘制柱状图
dates = list(date_province_amount_dict.keys())
provinces = list(date_province_amount_dict[dates[0]].keys())  # 假设所有日期的省份数据一致
amounts_by_province = [[] for _ in provinces]

for date in dates:
    amounts = [date_province_amount_dict[date][province] for province in provinces]
    for i, amount in enumerate(amounts):
        amounts_by_province[i].append(amount)

# 绘制柱状图
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(dates)
for i, province in enumerate(provinces):
    bar.add_yaxis(province, amounts_by_province[i], label_opts=LabelOpts(is_show=False))

bar.set_global_opts(title_opts=TitleOpts(title="每日销售额-省份分布"))

bar.render("每日销售额-省份分布柱状图.html")