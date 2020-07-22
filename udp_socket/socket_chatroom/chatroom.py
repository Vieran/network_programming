import socket
# 本程序处于半双工状态
# 程序存在bug，如果别人不断地发，但是本地没有一直收，那么系统会不堪重负，甚至导致崩溃
def send_msg(udp_socket):
    """发送信息"""
    # 获取要发送的内容
    dest_ip = input("please input dest_ip:")
    dest_port = int(input("please input dest_port:"))
    send_data = input("please input the message you want to send:")
    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def recv_msg(udp_socket):
    """接收数据"""
    recv_data = udp_socket.recvfrom(1024)
    print("%s:%s" %(str(recv_data[1]), recv_data[0].decode("utf-8")))


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 绑定信息
    local_port = int(input("please input local_port:"))
    udp_socket.bind(("", local_port))

    # 循环处理信息
    print("------chatroom------")
    while True:
        print("1:send message")
        print("2:receive message")
        print("3:leave chatroom")
        
        op = input("please input operation:")
        if op == "1":
            # 发送
            send_msg(udp_socket)
        elif op == "2":
            # 接收信息
            recv_msg(udp_socket)
        elif op == "0":
            break
        else:
            print("error input")


if __name__ == "__main__":
    main()
