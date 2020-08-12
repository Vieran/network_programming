import socket
import re
import select

def service_client(new_socket, request):
    """为客户端返回数据"""
    # 1.接收浏览器发过来的请求
    # GET / HTTP/1.1
    # ...
    
    # 处理请求的报文
    request_lines = request.splitlines()  #根据行分割
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])  #根据正则匹配出请求报文的第一行的前面内容
    if ret:
        file_name = ret.group(1)  #提取文件名
        if file_name == "/":  #访问主页
            file_name = "/HOME.html"
        print(">>>"*20, file_name)

    # 2.返回http格式的数据
    try:
        # 尝试打开请求的文件
        f = open("./html_files_for_text" + file_name, "rb")  #返回的文件在当前目录下的html文件夹中
    except:
        # 返回报错的信息
        header = "HTTP/1.1 404 NOT FOUND\r\n"
        header += "\r\n"
        html_content = "<h1>What you need is not found, please try again!</h1>"
        new_socket.send(header.encode("utf-8"))
        new_socket.send(html_content)
    else:
        # 准备返回的header
        header = "HTTP/1.1 200 OK\r\n"

        # 准备返回的body
        html_content = f.read()
        f.close()
        body = html_content

        # 发送header和body
        header += "Content-Length:%d\r\n" % len(html_content)
        header += "\r\n"
        response = header.encode("utf-8") + body
        new_socket.send(response)



def main():
    # 1.创建套接字
    tcp_sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_sever_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2.绑定
    tcp_sever_socket.bind(("", 8677))

    # 3.变为监听套接字
    tcp_sever_socket.listen(128)
    tcp_sever_socket.setblocking(False)  #套接字设置为非阻塞

    # 创建一个epoll对象
    epl = select.epoll()

    # 将监听套接字对应的fd注册到epoll中去
    epl.register(tcp_sever_socket.fileno(), select.EPOLLIN)
    fd_event_dic = dict()  #字典，用于根据fd找到套接字

    client_socket_list = list()
    while True:
        fd_event_list = epl.poll()  #默认阻塞，直到os监测到数据到来，通过事件通知此套接字才会解阻塞

        # 处理fe_event_list，这个列表里面是元组（套接字对应的文字描述符，文件描述的是什么事件）
        for fd, event in fd_event_list:
            # 等待新客户端连接
            if fd == tcp_sever_socket.fileno():
                new_socket, client_addr = tcp_sever_socket.accept()
                epl.register(new_socket.fileno(), select.EPOLLIN)
                fd_event_dic[new_socket.fileno()] = new_socket
            elif event == select.EPOLLIN:
                # 判断已经链接的客户端是否有数据发过来
                recv_data = fd_event_dic[fd].recv(1024).decode("utf-8")
                if recv_data:
                    service_client(fd_event_dic[fd], recv_data)
                else:
                    fd_event_dic[fd].close()
                    epl.unregister()
                    del fd_event_dic[fd]

    # 关闭监听套接字
    tcp_sever_socket.close()



if __name__ == "__main__":
    main()

#实践过程中发现，浏览器过一段时间会重新发送请求？而且请求是空的，如果不设置对空的请求的处理，就会在正则匹配那里出错
#在ip后面仅仅加一个/和不加/，发过来的请求的第一行都是/
#浏览器会自动请求favicon.ico，根据查到的信息，这是网站的图标
