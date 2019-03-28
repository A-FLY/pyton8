import socket


def main():
	# 1.创建套接字
	tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	# 2. 绑定端口
	tcp_socket.bind(("192.168.28.92",8890))

	# 3. 监听端口
	tcp_socket.listen(128)
	while True:
		print("等待客户连线中.....")
		# 4.等待链接并创建新的服务套接字
		new_tcp_socket,new_adder = tcp_socket.accept()
		print("开始服务一名客户端...")
		while True:
			try:
				# 5.打印接收到的信息
				receive_info = new_tcp_socket.recv(1024)
			except Exception as e:
				print("对方单方强制下线...")
				break
			if receive_info:
				# if receive_info.decode("utf-8") == "bye":
				# 	print("对方说bye.....")
				# 	break
				# else:
				# 打印客户端消息发送的信息
				print(receive_info.decode("utf-8"))
				receive_input = input("请输入需要回传的信息：")
				# 6.回复客户端信息
				new_tcp_socket.send(receive_input.encode("utf-8"))
			else:
				print("服务项目正常完成，对方下线.........")
				break
		# 7.关闭套接字
		new_tcp_socket.close()
	tcp_socket.close()



if __name__ == '__main__':
	main()
