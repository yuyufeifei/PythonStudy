import threading
import random
import time

g_money = 0
lock = threading.Lock()


class Producer(threading.Thread):
    def run(self):
        global g_money
        for _ in range(10):
            lock.acquire()
            money = random.randint(1000, 10000)
            g_money += money
            print(threading.current_thread().getName(), '挣了{}，当前余额为：{}'.format(money, g_money))
            time.sleep(1)
            lock.release()


class Customer(threading.Thread):
    def run(self):
        global g_money
        for _ in range(10):
            lock.acquire()
            money = random.randint(1000, 10000)
            if money <= g_money:
                g_money -= money
                print(threading.current_thread().getName(), '花了{}，当前余额为：{}'.format(money, g_money))
            else:
                print(threading.current_thread().getName(), '想花{}，但余额不足，当前余额为：{}'.format(money, g_money))
            time.sleep(1)
            lock.release()


def start():
    for i in range(5):
        prod = Producer(name='生产者{}'.format(i))
        prod.start()
    for i in range(5):
        cust = Customer(name='--消费者{}'.format(i))
        cust.start()


if __name__ == '__main__':
    start()