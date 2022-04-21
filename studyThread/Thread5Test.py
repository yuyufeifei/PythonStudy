from queue import Queue

# 创建队列，最多存放5个数据
q = Queue(5)

for i in range(4):
    q.put(i)
print('队列中的实际数据：', q.qsize())

for _ in range(5):
    try:
        print(q.get(block=False))
    except:
        print('数据已经取完')
        break

if q.full():
    print('队列已满')
else:
    print('队列当前数据的个数为：', q.qsize(), '，队列不满')
