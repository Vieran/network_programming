import threading
import time

g_nums = [11, 22]

def test1(g_nums):
    for i in range(5):
        print("---test1---%d---" %i)
        time.sleep(1)
    print(str(g_nums))

def test2():
    for i in range(10):
        print("---test2---%d---" %i)
        time.sleep(1)

def main():

    # target指定将来这个线程去哪个函数执行代码
    # args指定将来调用函数的时候传递的参数
    t1 = threading.Thread(target = test1, args = (g_nums,))
    t2 = threading.Thread(target = test2)
    t1.start()
    t2.start()
    while True:
        print(threading.enumerate())
        if len(threading.enumerate()) <= 1:
            break
        time.sleep(1)


if __name__ == "__main__":
    main()

