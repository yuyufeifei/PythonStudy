import threading
import random
import time

g_money = 0
g_time = 0
condition = threading.Condition()


class Producer(threading.Thread):
    def run(self):
        global g_money, g_time
        for _ in range(10):
            condition.acquire()
            money = random.randint(1000, 5000)
            g_money += money
            g_time += 1
            print(threading.current_thread().getName(), '挣了{}，当前余额为：{}'.format(money, g_money))
            # time.sleep(1)
            # 通知所有进程
            condition.notify_all()
            condition.release()


class Customer(threading.Thread):
    def run(self):
        global g_money, g_time
        for _ in range(10):
            condition.acquire()
            money = random.randint(5000, 10000)
            while g_money < money:
                if g_time >= 50:
                    print('赚不了钱了')
                    condition.release()
                    return
                print(threading.current_thread().getName(), '想花{}，但余额不足，当前余额为：{}'.format(money, g_money))
                # 等待
                condition.wait()
            g_money -= money
            print(threading.current_thread().getName(), '花了{}，当前余额为：{}'.format(money, g_money))
            # time.sleep(1)
            condition.release()


def start():
    for i in range(5):
        prod = Producer(name='生产者{}'.format(i))
        prod.start()
    for i in range(5):
        cust = Customer(name='--消费者{}'.format(i))
        cust.start()


if __name__ == '__main__':
    start()