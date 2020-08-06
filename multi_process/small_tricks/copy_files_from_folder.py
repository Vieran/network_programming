import os
import multiprocessing


def copy_file(queue, file_name, old_folder_name, new_folder_name):
    """完成文件的复制"""
    print("====>复制文件%s" %file_name)
    old_f = open(old_folder_name + "/" + file_name, "rb")
    content = old_f.read()
    old_f.close()

    new_f = open(new_folder_name + "/" + file_name, "wb")
    new_f.write(content)
    new_f.close()

    # 如果拷贝完文件，则向队列中写入一个消息，表示已完成
    queue.put(file_name)

def main():
    # 1.获取用户要copy的文件名
    old_folder_name = input("please input folder's name:")

    # 2.创建一个新的文件夹
    try:
        new_folder_name = "[new]" + old_folder_name
        os.mkdir(new_folder_name)
    except:
        pass

    # 3.获取待复制的文件夹中的所有文件名（使用listdir()
    file_names = os.listdir(old_folder_name)
    print(file_names)

    # 4.创建一个队列
    q = multiprocessing.Manager().Queue()

    # 5.创建进程池并向进程池中添加任务
    po = multiprocessing.Pool(6)
    for file in file_names:
        po.apply_async(copy_file, args=(q, file, old_folder_name, new_folder_name))

    # 6.关闭进程池
    po.close()
    #po.join()
    file_num = len(file_names)
    finish_copy = 0
    while True:
        file_name = q.get()
        finish_copy += 1
        # \r表示回到行首，end表示不换行
        print("\rfinished copy file %.2f%%" %(finish_copy*100/file_num), end="")
        if finish_copy >= file_num:
            break

if __name__ == "__main__":
    main()

