import socket
import threading

def recv_msg(udp_socket):
    """接收数据"""
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)

def send_msg(udp_socket, dest_ip, dest_port):
    """发送数据"""
    while True:
        send_data = input("please input what to send:")
        udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def main():
    """完成udp聊天器的整体控制"""

    # 1.创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2.绑定本地信息和获取对方信息
    udp_socket.bind(("", 8677))
    dest_ip = input("please input dest_ip:")
    dest_port = int(input("please input dest_port:"))

    # 3.创建两个线程，执行相应的功能
    t_recv = threading.Thread(target=recv_msg, args=(udp_socket,))
    t_send = threading.Thread(target=send_msg, args=(udp_socket, dest_ip, dest_port,))

    t_recv.start()
    t_send.start()

if __name__ == "__main__":
    main()
