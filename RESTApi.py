import socket, sys, os

def main():
    #temp port, change later
    PORT = 11111
    HOST = ""
    socket.setdefaulttimeout(60)
    debug = False

    try:
        #open our listen socket - wait for requests
        listenSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listenSock.bind(('', PORT))
        print("listening")
        listenSock.listen()

        while True:
            print("listening")
            conn, clientAddress = listenSock.accept()
            #only supports IPv4
            connectingIP = str(clientAddress[0])
            handleRequest(conn,connectingIP,debug)
            listenSock.listen()
        listenSock.close()

    except socket.error:
        print("Socket error.")
        print("Common issues include: bad port number, port number is busy, socket time out")
        if listenSock:
            listenSock.close()
        sys.exit(1)
    except KeyboardInterrupt:
        sys.exit(1)

def handleRequest(conn,connectingIP,debug):
    #setting up some variables that will be used later
    myIP = socket.gethostbyname(socket.gethostname())
    proxyName = "Paul's Proxy"
    proxyVersion = "1.0"
    maxRequestSize = 4096
    server = ""
    port = -1
    HTTPrequest = ""

    #accounting for very, very big requests (shouldn't happen but can't hurt!)
    try:
        while True:
            HTTPrequestB = conn.recv(8192)
            temp = HTTPrequestB.decode("utf-8")
            HTTPrequest = HTTPrequest + temp
            if (HTTPrequest.find("\r\n\r\n")!=-1):
                break
    except:
        print("bad request - please retry")
        sys.exit(1)

    print("\ninitial http request:")
    print (HTTPrequest)

    #magic happens here!
    conn.send(jsonData)

if __name__ == '__main__':
  main()
