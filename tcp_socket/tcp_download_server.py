import socket

def send_file_2_client(new_client_socket, client_addr):
    # 1.接收客户端发送过来的文件名
    file_name = new_client_socket.recv(1024).decode("utf-8")
    print("%s needs %s" %(str(client_addr), file_name))

    # 2.打开文件读取数据
    file_content = None
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("%s not exit!" %file_name)

    # 3.发送文件给客户端
    if file_content:
        new_client_socket.send(file_content)


def main():
    # 1.创建套接字（买手机
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    # 2.绑定本地信息（插入手机卡
    local_port = 8677
    tcp_server_socket.bind(("", local_port))


    # 3.让默认的套接字由主动变被动（将手机设置为正常响铃状态
    tcp_server_socket.listen(128)

    
    while True:
        # 4.等待客户端连接（等别人打电话
        new_client_socket, client_addr = tcp_server_socket.accept()


        # 5.收发数据
        send_file_2_client(new_client_socket, client_addr)
        

        # 关闭服务完毕的客户端套接字
        new_client_socket.close()
        print("serving end...")


    # 6.关闭套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
