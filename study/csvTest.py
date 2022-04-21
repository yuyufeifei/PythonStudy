import csv


# newline参数设置为空可防止两倍行距
def writecsv():
    with open('student.csv', 'a+', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        # 一次写一行数据
        writer.writerow(['小郭', 30, 99])
        # 一次写多行
        lists = [
            ['小赵', 33, 89],
            ['小钱', 31, 88],
            ['小孙', 35, 85],
            ['小李', 29, 96]
        ]
        writer.writerows(lists)


def readcsv():
    print()
    with open('student.csv', 'r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


if __name__ == '__main__':
    # writecsv()
    readcsv()
