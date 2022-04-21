import openpyxl
# 创建工作簿
wb = openpyxl.Workbook()
# 获取工作表
sheet = wb.active
# 获取指定的单元格
cell = sheet['A1']
# 向单元格中写入数据
cell.value = '美丽中国'

list = ['姓名', '年龄', '分数']
# 写入一行数据
sheet.append(list)

wb.save('我的excel文件.xlsx')

# 加载excle文件
wb = openpyxl.load_workbook('我的excel文件.xlsx')

sheet = wb.active['Sheet']
# 获取一列格子
columns = sheet['A']
for col in columns:
    print(col.value)
# 获取一行
row = sheet[2]
# 获取两列
cols = sheet['B:C']