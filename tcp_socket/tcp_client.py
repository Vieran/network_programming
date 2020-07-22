import socket

def main():
    # 1.创建tcp套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    # 2.链接服务器
    server_ip = input("please input server_ip:")
    server_port = int(input("please input server_port:"))
    server_addr = (server_ip, server_port)
    tcp_socket.connect(server_addr)


    # 3.发送数据
    while True:
        send_data = input("please input what to send:")
        tcp_socket.send(send_data.encode("utf-8"))
        if send_data == "exit":
            break
    tcp_socket.recv(1024)


    # 4.关闭服务器
    tcp_socket.close()



if __name__ == "__main__":
    main()
