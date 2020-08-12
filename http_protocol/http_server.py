import socket

def service_client(new_socket):
    """为客户端返回数据"""
    # 1.接收浏览器发过来的请求
    # GET / HTTP/1.1
    # ...
    request = new_socket.recv(1024)
    print(request.decode("utf-8"))

    # 2.返回http格式的数据
    # 准备返回的header
    response = "HTTP/1.1 200 OK\r\n"
    response += "\r\n"
    
    # 准备返回的body
    response += "<h1>welcome to a new world!</h1>"

    # 发送数据
    new_socket.send(response.encode("utf-8"))
    
    # 3.关闭套接字
    new_socket.close()



def main():
    # 1.创建套接字
    tcp_sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.绑定
    tcp_sever_socket.bind(("", 8677))

    # 3.变为监听套接字
    tcp_sever_socket.listen(128)

    while True:
        # 4.等待新客户端连接
        new_socket, client_addr = tcp_sever_socket.accept()

        # 5.为用户服务
        service_client(new_socket)
    
    # 6.关闭监听套接字
    tcp_sever_socket.close()



if __name__ == "__main__":
    main()
