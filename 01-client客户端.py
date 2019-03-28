import socket


def send_date(x):
    # 要发送的信息
    op_date = input("请输入你要说的话：").encode("utf-8")
    x.send(op_date)
    if op_date.decode("utf-8") == "bye":
        return True
    return None


def receive_date(x):
    # 服务器回传的信息
    receive_date = x.recv(1024)
    print(receive_date.decode("utf-8"))


def main():
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 跟服务端确认链路是否正常
    receive_adder = ("192.168.28.92", 8890)
    tcp_socket.connect(receive_adder)
    # 跟服务器通信
    while True:
        # 调用发送函数
        a = send_date(tcp_socket)
        # 调用接收函数
        receive_date(tcp_socket)
        print("结束聊天")
        if a:
            break
    # 关闭套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()
