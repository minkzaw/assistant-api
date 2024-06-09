from socket import socket, AF_INET, SOCK_STREAM, error as SocketError

class Checkport:
    def __init__(self, ip=None, port=None):
        self.ip = ip
        self.port = port

    def portChecker(self):
        session = None  # Initialize session outside the try block
        try:
            if self.ip is not None and self.port is not None:
                session = socket(AF_INET, SOCK_STREAM)
                session.settimeout(2)
                session.connect((self.ip, self.port))
                return {"message": f"Port {self.port} is open on IP {self.ip}"}
            else:
                return {"error": "Please specify IP and Port."}
        except SocketError as error:
            return {"message": f"Port {self.port} is not open on IP {self.ip}"}
        finally:
            if session is not None:
                session.close()  # Close session if it's not None
    
