import socket
import re

def service_client(new_socket):
    """为客户端返回数据"""
    # 1.接收浏览器发过来的请求
    # GET / HTTP/1.1
    # ...
    request = new_socket.recv(1024).decode("utf-8")
    print(request)
    
    if request == "":
        new_socket.close()
        return

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
        new_socket.send(html_content.encode("utf-8"))
    else:
        # 准备返回的header
        header = "HTTP/1.1 200 OK\r\n"
        header += "\r\n"

        # 准备返回的body
        html_content = f.read()
        f.close()

        # 发送header和body
        new_socket.send(header.encode("utf-8"))
        new_socket.send(html_content)
        
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

#实践过程中发现，浏览器过一段时间会重新发送请求？而且请求是空的，如果不设置对空的请求的处理，就会在正则匹配那里出错
#在ip后面仅仅加一个/和不加/，发过来的请求的第一行都是/
#浏览器会自动请求favicon.ico，根据查到的信息，这是网站的图标
