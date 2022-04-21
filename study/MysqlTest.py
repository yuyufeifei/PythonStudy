import mysql.connector

conn = mysql.connector.connect(host='localhost', user='root', passwd='123456', database='webtest')
# print(conn)
cursor = conn.cursor()
sql = 'insert into users (name, passwd, email) values (%s, %s, %s)'
param = ('郭郭', '122', 'aaa@qq.com')
cursor.execute(sql, param)
# 插入多行
params = [
    ('郭郭1', '1224', 'aaa1@qq.com'),
    ('郭郭2', '1225', 'aaa2@qq.com'),
    ('郭郭3', '1226', 'aaa3@qq.com')
]
cursor.executemany(params)
conn.commit()
# 插入了多少数据
print(cursor.rowcount)