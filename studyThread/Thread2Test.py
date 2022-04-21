import threading
import time

ticket = 100
# 创建锁
lock = threading.Lock()


def sale_ticket():
    global ticket
    for i in range(100):
        # 上锁
        lock.acquire()
        if ticket > 0:
            print(threading.current_thread().getName() + '正在出售第{}张票'.format(ticket))
            ticket -= 1
        time.sleep(1)
        # 释放锁
        lock.release()


def start():
    for i in range(2):
        threading.Thread(target=sale_ticket).start()


if __name__ == '__main__':
    start()
