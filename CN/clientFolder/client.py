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

    for idx in range(len(ans)):
       ans[idx] = ans[idx][::-1]

    return " ".join(ans)
# print(transpose_encrypt("as sdfsd"))


IP = 'localhost'
port = 5005
adrress = (IP,port)

c = socket.socket() 
c.connect(adrress) 
print(c.recv(1024).decode('utf-8'))

command = input("write the command here, ",)


if(command == "CD"):
    # command = substitute_encrypt(command)
    c.send(substitute_encrypt(command).encode('utf-8'))
    print(c.recv(1024).decode('utf-8'))
    dir = input("dir?? ",)
    c.send(dir.encode('utf-8'))
    print(c.recv(1024).decode('utf-8'))


elif(command == "UPD"):
    c.send(transpose_encrypt(command).encode('utf-8'))
    print(c.recv(1024).decode('utf-8'))
    file_name = input("write the file name here, ",)
    c.send(file_name.encode('utf-8'))
    print(c.recv(1024).decode('utf-8'))
    file = open(file_name,'r')
    data = file.read()
    file.close()
    data=substitute_encrypt(data)
    c.send(data.encode('utf-8'))


elif(command == "DWD"):
    c.send(transpose_decrypt(command).encode('utf-8'))

    filename = c.recv(1024).decode('utf-8')
    c.send("filename is received".encode('utf-8'))

    data = c.recv(1024).decode('utf-8')
    # filename = c.recv(1024).decode('utf-8')  
    file = open("clientFolde/"+filename ,'w')
    file.write(data)
    file.close() 

    # c.send(bytes('ok, filename received','utf-8'))
    # c.send(bytes('file data is received and file is uploaded','utf-8'))

elif(command == "CWD" or command == "LS"):
    # command = transpose_encrypt(command)
    c.send(transpose_encrypt(command).encode('utf-8'))


if(command == "CWD" or command == "LS"):
    print(c.recv(1024).decode('utf-8'))








