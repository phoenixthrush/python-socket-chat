import sys
import socket
from urllib import response
import colorama
import datetime
import threading
from os import system, name

def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def currentTime():
    # Retrieves local time formatted as HH:MM:SS
    now = datetime.datetime.now()
    formattedTime = now.strftime("%H:%M:%S")
    return formattedTime

def deleteLastLine():
    # Writes ANSI codes to perform cursor movement and current line clear
    cursorUp = "\x1b[1A"
    eraseLine = "\x1b[2K"
    sys.stdout.write(cursorUp)
    sys.stdout.write(eraseLine)

def send(sock):
    # Handles sending messages to the server
    while threadFlag:
        try:
            message = input()
            deleteLastLine()
            sock.send(message.encode("utf8"))
        except:
            print("An error occured while trying to send a message!")
            break

def receive(sock):
    # Handles receiving messages from the server
    while threadFlag:
        try:
            message = sock.recv(2048).decode()
            if message:
                print("[{}] {}".format(currentTime(), message))
            else:
                # When the server closes the socket, messages received are empty
                break
        except:
            print("An error occured while trying to reach the server!")
            break

def main():
    system("title Phoenixthrush's Furry Chat")
    clear()
    # main() will refer to threadFlag as to the global variable defined globally
    global threadFlag
    # Colorama handles the ANSI escape codes to work also on Windows
    colorama.init()
    # The host and port of the chat server
    host = input("Host: ")
    port = int(input("Port: "))
    clear()
    # Creates the socket for a TCP application
    socketFamily = socket.AF_INET
    socketType = socket.SOCK_STREAM
    clientSocket = socket.socket(socketFamily, socketType)
    # Connects to the server
    clientSocket.connect((host, port))
    # Creates two threads for sending and receiving messages from the server
    sendingThread = threading.Thread(target=send, args=(clientSocket,))
    receivingThread = threading.Thread(target=receive, args=(clientSocket,))
    # Start those threads
    receivingThread.start()
    sendingThread.start()
    # Checks if both threads are alive for handling their termination
    while receivingThread.is_alive() and sendingThread.is_alive():
        continue
    threadFlag = False
    # Finally closes the socket object connection
    clientSocket.close()
    print("\nYou can now close the application.")

# Flag used for threads termination
threadFlag = True

if __name__ == "__main__":
    try:
        main()
    except Exception:
        input("\nAn error occured!\nPlease try again.\n")
    pass