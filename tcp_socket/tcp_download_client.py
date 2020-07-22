import socket

def main():
    # 1.创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    # 2.获取服务器ip
    dest_ip = input("please input server ip:")
    dest_port = int(input("please input server port:"))


    # 3.链接服务器
    tcp_socket.connect((dest_ip,dest_port))


    # 4.获取下载文件名字
    download_file_name = input("please input file_name:")


    # 5.将文件名发送到服务器
    tcp_socket.send(download_file_name.encode("utf-8"))


    # 6.接收文件中的数据（此数据为二进制数据
    recv_data = tcp_socket.recv(1024)


    # 7.保存收到的信息到一个文件中（以二进制写方式打开
    if recv_data:
        with open("[receive]" + download_file_name, "wb") as f:
            f.write(recv_data)


    # 8.关闭套接字
    tcp_socket.close()


if __name__ == "__main__":
    main()
