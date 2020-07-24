import threading
import time

# 使用线程来执行类的成员函数，则类必须定义run方法，并且必须继承threading类
# 调用start的时候，自动调用run方法，run方法结束了，那么线程也结束了
class MyThread(threading.Thread):
    def run(seft):
        for i in range(3):
            time.sleep(1)
            msg = "I'm " + seft.name + ' @ ' + str(i)
            print(msg)


if __name__ == "__main__":
    t = MyThread()
    t.start()
