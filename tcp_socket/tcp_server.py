import socket

def main():
    # 1.创建套接字（买手机
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    # 2.绑定本地信息（插入手机卡
    local_port = 8677
    tcp_server_socket.bind(("", local_port))


    # 3.让默认的套接字由主动变被动（将手机设置为正常响铃状态
    tcp_server_socket.listen(128)


    # 4.等待客户端连接（等别人打电话
    while True:
        print("waiting for a client...")
        # client_socket用来为这个客户端服务，这样tcp_server_socket就可以省下来为其他客户端服务
        # accept的返回值是元组，
        new_client_socket, client_addr = tcp_server_socket.accept()
        print("a new client arrive: %s" %str(client_addr))

        # 5.收发数据
        while True:
            # 此处的recv_data仅仅为数据，因为客户端的信息存储在new_client_socket里面了
            recv_data = new_client_socket.recv(1024)
            print("client request: %s" %recv_data.decode("utf-8"))
            
            # 解堵塞的情况：收到信息/client关闭，如果是关闭，则recv_data是空
            if recv_data:
                # 返回一定的数据给客户端
                send_data = input("please input message you want to send back:")
                new_client_socket.send(send_data.encode("utf-8"))
            else:
                break
            
        # 关闭服务完毕的客户端套接字
        new_client_socket.close()
        print("serving end...")

    # 6.关闭套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
