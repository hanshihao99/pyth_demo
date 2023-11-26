from data_define import Record


class FileReader:

    def read_data(self) -> list[Record]:
        """读取文件的数据，读到的每一条数据都转换为Record 对象，将他们分装到list内返回"""
        pass


class TextFileReader(FileReader):

    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, "r", encoding="UTF-8")

        record_list = []
        line_number = 0
        for line in f.readlines():
            line_number += 1
            if line_number == 1:
                continue
            line = line.strip()  # 消除每一行的换行符
            data_list = line.split(',')
            if len(data_list) != 4:
                print(f"Invalid data at line {line_number}: {line}")
                continue
            try:
                record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
                record_list.append(record)
            except ValueError as e:
                print(f"Error at line {line_number}: {line}")
                print(e)

        f.close()
        return record_list


if __name__ == '__main__':
    textFile = TextFileReader('/Users/hanshihao/Downloads/2021全国订单数据.csv')
    textFile.read_data()
