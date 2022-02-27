from imported_sip_library import *

def main():
    print("ej bistu")

    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='proxy.log', level=logging.INFO,
                        datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
    hostname = socket.gethostname()
    logging.info(hostname)
    ipaddress = HOST

    logging.info(ipaddress)
    recordroute = "Record-Route: <sip:%s:%d;lr>" % (HOST, PORT)
    topvia = "Via: SIP/2.0/UDP %s:%d" % (HOST, PORT)
    server = socketserver.UDPServer((HOST, PORT), UDPHandler)
    server.serve_forever()




if __name__ == '__main__':


    main()
