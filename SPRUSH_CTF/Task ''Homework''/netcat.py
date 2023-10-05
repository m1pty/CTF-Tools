import socket, re
import numexpr as ne

def solve(example: str):
    # уравнение из операндов и операторов
    example = example.replace(" =", "").replace(" ", "")
    tmp = ne.evaluate(example)
    return int(tmp)

def netcat(hostname, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    while 1:
        data = s.recv(1024)
        if len(data) == 0:
            break
        str_data = data.decode("utf-8")
        str_data = str_data[str_data.find(")") + 1:]
        print("Received:", repr(data))
        if ("need you to help me" not in str_data):
            answer = str(solve(str_data))
            s.sendall(str(answer).encode())
            print("Sent: ", answer)

    print("Connection closed.")
    s.close()

netcat("5.35.100.119", 8001)