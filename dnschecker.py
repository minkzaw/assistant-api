import socket
class DNSChecker:
    def __init__(self, dnsName):
         self.dnsName = dnsName

    def dnslookUp(self):
        try:
            ip_address = socket.gethostbyname(self.dnsName)
            return f"DNS lookup result for {self.dnsName}: {ip_address}"
        except Exception as error:
            return str(error)