import socket
import os

# Below defined function are part and modes of Crypto Layer
def plaintext(s):
    s = s
    return s

def substitute_decrypt(s):
    decrypt_msg = ""
    for i in range(len(s)):
        a = ord(s[i])
        # print(a)
        if(a >= ord('a') and a <= ord('z')):
            dj = chr((a - ord('a') - 2)%26 + ord('a'))
            decrypt_msg += dj
        elif(a >= ord('A') and a <= ord('Z')):
            dj = chr((a - ord('A') - 2)%26 + ord('A'))
            decrypt_msg += dj
        elif(a >= ord('0') and a <= ord('9')):
            dj = chr((a - ord('0') - 2)%10 + ord('0'))
            decrypt_msg += dj
    return decrypt_msg

def transpose_decrypt(s):
    ans = s.split(" ")

    for idx in range(0,len(ans)):
       ans[idx] = ans[idx][:: -1]

    return " ".join(ans)

def substitute_encrypt(s):
    encrypt_msg = ""
    for i in range(len(s)):
        a = ord(s[i])
        # print(a)
        if(a >= ord('a') and a <= ord('z')):
            dj = chr((a - ord('a') + 2)%26 + ord('a'))
            encrypt_msg += dj
        elif(a >= ord('A') and a <= ord('Z')):
            dj = chr((a - ord('A') + 2)%26 + ord('A'))
            encrypt_msg += dj
        elif(a >= ord('0') and a <= ord('9')):
            dj = chr((a - ord('0') + 2)%10 + ord('0'))
            encrypt_msg += dj
    return encrypt_msg

def transpose_encrypt(s):
    ans = s.split(" ")

    for idx in range(0,len(ans)):
       ans[idx] = ans[idx][:: -1]

    return " ".join(ans)


def current_directory():
    path = os.getcwd()
    # print(path)
    c.send(bytes(path,'utf-8'))

def list_of_files():
    all_files = os.listdir()
    a = " ".join(all_files)
    # print(all_files)
    c.send(a.encode('utf-8'))


    
IP = 'localhost'
port = 5005
adrress = (IP,port)

s = socket.socket()
print('Socket created')

s.bind(adrress)
s.listen(5)
print('server is listing and waiting for connection')

# while True:
c, addr = s.accept()
print("Connnected with ", addr)
c.send(bytes('Welcome my dear client,which command would you like to use','utf-8'))

command = transpose_decrypt(c.recv(1024).decode('utf-8'))
# command = transpose_decrypt(command)
if(command == "CWD"):
    current_directory()

elif(command == "LS"):
    list_of_files()

elif(command == "CD"):
    c.send("dir??".encode('utf-8'))
    dirC = c.recv(1024).decode('utf-8')
    print("current directory -",dirC)
    # temp = transpose_decrypt(dir)
    os.chdir(dirC)
    # print(os.getcwd())

    c.send(os.getcwd().encode('utf-8'))
    # directory_change(dir)

elif(command == "DWD"): 

    file_name = input('which file ??',)

    file = open("server/" + file_name,'r')
    data = file.read()
    file.close()

    c.send(file_name.encode('utf-8'))
    msg = c.recv(1024).decode('utf-8')
    print("msg by client: ",msg)
    c.send(data.encode('utf-8'))
    # print("msg by client: ",c.recv(1024).decode('utf-8')) 

elif(command == "UPD"):
    c.send("what is the file name".encode())
    filename = c.recv(1024).decode('utf-8')
    print("filename is- ",filename)
    c.send(bytes('Filename received.','utf-8'))
    data = c.recv(1024).decode('utf-8')
    data=substitute_decrypt(data)
    print('file data is received')
    file = open("server/" + filename ,'w')
    file.write(data)
    file.close()

c.close()
print("connection disconnected")

# import os
# os.chdir("C:\CN\server\\asd")
# print(os.getcwd())
