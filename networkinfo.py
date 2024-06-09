import requests, json

class Ipinfo:
    def __init__(self, ip=None):
        self.ip = ip

    def getInfo(self):
        if self.ip is not None:  # Check if self.ip is not None
            response = requests.get(f'https://ipinfo.io/{self.ip}')
        else:
            response = requests.get('https://ipinfo.io/')
        try:
            if response.status_code == 200:
                data = response.json()
                ipinfo = {
                "city": data.get('city'),
                "country": data.get('country'),
                "ip": data.get('ip'),
                "loc": data.get('loc'),
                "org": data.get('org'),
                "region": data.get('region'),
                "timezone": data.get('timezone')             
                }
            return ipinfo
        except Exception as error:
            return str(error)