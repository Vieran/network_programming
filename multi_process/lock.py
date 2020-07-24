import threading
import time

g_nums = [11, 22]

def test1(g_nums):
    # 上锁，如果之前没有锁，则上锁成功；如果上锁之前被上锁了，则会堵塞，直至解锁
    #mutex.acquire()
    
    for i in range(5):
        mutex.acquire()
        print("---test1---%d---" %i)
        #time.sleep(1)
        # 解锁
        mutex.release()
    print(str(g_nums))



def test2():
    for i in range(10):
        mutex.acquire()
        print("---test2---%d---" %i)
        #time.sleep(1)
        mutex.release()



# 创建一个互斥锁，默认默认是没有上锁的
mutex = threading.Lock()



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

