import multiprocessing
import time

def download_from_web(q):
    """模拟从网上下载数据"""
    data = [11, 22, 33, 44]
    
    # 向队列中写入数据
    for tmp in data:
        q.put(tmp)

    print("---数据下载完毕，并存入队列中---")


def analysis_data(q):
    """数据处理"""
    waiting_analysis_data = list()
    # 从队列中获取数据
    while True:
        data = q.get()
        waiting_analysis_data.append(data)

        if q.empty():
            break

    print(waiting_analysis_data)


def main():
    # 1.创建一个队列（队列括号内有指定数字的时候，就是指定可以放置数据的个数；不指定则根据系统设定
    q = multiprocessing.Queue()

    # 2.创建多个进程，将队列的引用当作实参传递过去
    p1 = multiprocessing.Process(target=download_from_web, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))
    p1.start()
    time.sleep(1)
    p2.start()
    

if __name__ == "__main__":
    main()
