from socket import *
import random
from words import word_list
import os
import pyttsx3

engine = pyttsx3.init()

serverPort = 1220
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

# max=1
correct = 0
lives = 0
score=0
nwo=len(word_list)
while (correct==0):
    print('The server is ready to receive')
    def voice(given_word):
        my = given_word
        engine.say(my)
        engine.runAndWait()

    j=0
    f=0  
    print(len(word_list))

    if correct==0 and (j<len(word_list)):    
        while (lives == 0 and correct < nwo):      
            given_word = random.choice(word_list)
            connectionSocket,addr = serverSocket.accept()
            if(f==0):
                engine.say("welcome to the game ")
                engine.runAndWait()  
            f+=1
            voice(given_word)
            w1 = connectionSocket.recv(1024).decode()
            c = len(word_list)
            if str(given_word) == str(w1) :
                lives = 0
                correct = correct + 1
                score=correct
                v="YOUR SCORE:"+" "+str(correct)
                connectionSocket.send(v.encode())
            else:
                lives = 1
                correct = 4
                # print("in else")
                l="YOUR SCORE:"+" "+str(score)
                c="wrong"
                connectionSocket.send(l.encode())
                connectionSocket.send(c.encode())
            word_list.remove(given_word)
            connectionSocket.close()
    if lives == 0:
        engine.say(f"you spelled all {nwo} words corectly and you won the game")
        engine.runAndWait()
    else:
        engine.say(f"you misspelled {given_word} and you are out of the game and your score is {score} out of {nwo}")
        engine.runAndWait()
    


