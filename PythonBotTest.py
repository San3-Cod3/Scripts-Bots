import sys                # 1
import os                 # 2
import time               # 3
from datetime import date # 4
import random             # 5
import uuid               # 6
import http.client        # 7
import re                 # 8
import socket             # 9

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def ircwrite(message):
    global irc
    irc.send(str(message).encode('utf-8'))


def sendm(msg): 
    irc.send(('PRIVMSG '+ channel + ' :' + (msg) + '\r\n').encode())


def quitting():
  ircwrite("PRIVMSG "+ channel +" :Okay boss, leaving now.\n")

botnick = "test__bot"

ident = "testident"

channel = "#youkay"

owner = "you"

irc.connect((server, port)) # Connects to the server | change 'server', 'port' to your stuff

ircwrite("USER "+ ident +" "+ botnick +" "+ botnick +" :Real_Name-LAME \r\n")
ircwrite("NICK "+ botnick +"\r\n")

while 1:
    text = irc.recv(2048).decode('utf-8') # Receive data from the server
    if not text:
        break

    svrtext = text.split()

    print(text) # Prints out all info coming from the IRC Network

    if "PING :" in text:
        print("Got a PING")
        print("")

    if text.find("PING :") != -1:
        irc.send(("PONG " + text.split() [1] + "\r\n").encode())
        print("PONG has successfully been sent back to: network")
        print("")

    if "376" in svrtext:
        ircwrite("JOIN "+ channel +"\r\n")

# ########### #
# My commands #
# ########### #

    if text.find(':!date') != -1:
        sendm('[+] Date: '+ time.strftime("%A, %d %B [month #%m], %Y", time.localtime()))

    if text.find(':!time') != -1:
        sendm('[+] Time: '+ time.strftime("%H:%M:%S", time.localtime()))

### owner string quit section (START) ###

    Quit_Stuff = text.strip('\n\r') # Removing any unnecessary linebreaks.

    name = Quit_Stuff.split('!',1)[0][1:] # We split out the name

    if name.lower() == owner.lower() and Quit_Stuff.find(":quit " + botnick) != -1:
        quitting()
        irc.send(bytes("QUIT \n", "UTF-8"))
    else:
        if name.lower() != owner.lower() and Quit_Stuff.find(":quit " + botnick) != -1:
            ircwrite("PRIVMSG "+ channel +" :You do NOT match owner string! \r\n")

### owner string quit section (END) ###