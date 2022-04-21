import threading
import time


class CodingThread(threading.Thread):
    def run(self):
        # 获取当前的线程对象
        thread = threading.current_thread()
        print(thread)
        # 线程的名称
        print(thread.getName())
        # 设置线程名称
        thread.setName("新的线程名称")
        print(thread.getName())
        for i in range(5):
            print('i的值为：', i)
            time.sleep(1)


class CodingThread2(threading.Thread):
    def run(self):
        thread = threading.current_thread()
        print(thread)
        for i in range(5):
            print('2--i的值为：', i)
            time.sleep(1)


def mult():
    t1 = CodingThread()
    t2 = CodingThread2()
    t1.start()
    t2.start()
    # 查看所有线程
    print(threading.enumerate())


if __name__ == '__main__':
    mult()
