import socket

def main():
    # 1.创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    # 2.绑定本地相关信息，如果网络程序不稳定，则系统随机分配
    local_port = 8677
    local_addr = ('', local_port)  # ip地址一般不用写，表示本机的任何一个ip
    udp_socket.bind(local_addr)  # 必须绑定本地的ip和port


    # 3.接收并打印数据
    while True:
        recv_data = udp_socket.recvfrom(1024)  # 括号里面的数字表示接收的最大字符数
        
        # 此处的recv_data是一个元组（接收到的信息，（发送方的ip，发送方的端口））
        recv_msg = recv_data[0]  # 存储接收到的信息
        send_addr = recv_data[1]  # 存储发送方的地址信息
        print("%s:%s" %(str(send_addr), recv_msg.decode("utf-8")))
        if recv_msg.decode("utf-8") == "exit":
            break

    # 4.关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
