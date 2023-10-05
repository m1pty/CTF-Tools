import hashlib
import random
import string
import socket, re

# flag{c4lcul4t1ng_hash3s_l1k3_a_pr0}
alphabet = string.ascii_letters + "0123456789"
def brute_hash(hash_start):
    for elem1 in alphabet:
        for elem2 in alphabet:
            for elem3 in alphabet:
                for elem4 in alphabet:
                    word = elem1 + elem2 + elem3 + elem4
                    h = hash(word)
                    if (hash_start == h[0: 4]):
                        return word

def hash (example: str):
    hash_example = hashlib.md5(example.encode("utf-8")).hexdigest()
    return hash_example

def netcat(hostname, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    while 1:
        data = s.recv(1024)
        if len(data) == 0:
            break
        str_data = data.decode("utf-8")
        print("Received:", repr(str_data))

        hash_start = str_data[str_data.rfind("с ") + 2: str_data.rfind("!")]
        print("Hash start: ", hash_start)
        
        string_to_hash = brute_hash(hash_start)
        s.sendall(string_to_hash.encode())
        print("Sent: ", string_to_hash)

    print("Connection closed.")
    s.close()

netcat("5.35.100.119", 8000)