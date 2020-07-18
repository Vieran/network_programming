import socket

def main():
    # 1.创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


    # 2.准备对方的ip和端口，也就是目的地
    dest = input("please input dest_ip(0 for default):")
    if dest == '0':
        dest_ip = "47.101.45.86"
        dest_port = 8677
    else:
        dest_ip = dest
        dest_port = int(input("please input dest_port:"))
    dest_ip_f = "121.199.34.25"
    dest_port_f = 8214
    dest_addr = (dest_ip, dest_port)  # 目标地址是个元组

    # 绑定端口（如果不绑定，则每次随机分配
    #udp_socket.bind(("",7890))

    # 3.发送信息
    # 需要注意，sendto的第一个参数是byte类型的（直接在字符串前面加个b可以解决
    #udp_socket.sendto(b"what to send", dest_addr)
    #udp_socket.sendto(send_msg.encode("utf-8"), dest_addr)
    
    # 不断地发送
    while True:
        send_msg = input("please input what you want to send:")    
        udp_socket.sendto(send_msg.encode("utf-8"), dest_addr)
        if send_msg == "exit":
            break;


    # 4.关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
