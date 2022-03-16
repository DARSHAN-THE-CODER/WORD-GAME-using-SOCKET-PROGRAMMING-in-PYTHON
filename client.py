from socket import *
from words import word_list
import os
import sys
serverName='127.0.0.1'
serverPort=1220

i=0
print("before prgm")

l=input("ARE YOU READY TO ENTER GAME ? Y/N :")

if(l=="Y"):
    while i<len(word_list):
        clientSocket=socket(AF_INET,SOCK_STREAM)
        clientSocket.connect((serverName,serverPort))

        word1=input("ENTER THE WORD :")
        clientSocket.send(word1.encode())
        recBack = clientSocket.recv(1024).decode()
        print(recBack)
        m=clientSocket.recv(1024).decode()

        print(" ")
        if(m=="wrong"):
            i=100
        clientSocket.close()
        i=i+1

