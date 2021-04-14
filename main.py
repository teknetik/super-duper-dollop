import requests
import json

api_host = "10.0.0.4"
api_port = "9015"
rbac_enable = False
tls = False
super_admin = ""
super_passwd = ""


if tls:
    proto = "https://"
else:
    proto = "http://"


class Service:

    @staticmethod
    def create():
        c = requests.post(proto + api_host + ":" + api_port + "/services",
                          data={'name': 'httpbin',
                                'protocol': 'http',
                                'host': 'httpbin.org',
                                'port': '80',
                                'path': '/anything'})
        r = json.loads(c.content.decode("UTF-8"))
        return r

    @staticmethod
    def delete(srv_name):
        c = requests.delete(proto + api_host + ":" + api_port + "/services/" + srv_name)
        return c.status_code


class Route:

    @staticmethod
    def add(srv_name):
        c = requests.post(proto + api_host + ":" + api_port + "/services/" + srv_name + "/routes/",
                          data={'name': 'anything',
                                'paths': '/anything',
                                'methods': 'GET'})

class Rbac:

    def __init__(self):
        pass

    class Role:
        @staticmethod
        def add():
            print("adding role")
            return None

    class Users:
        @staticmethod
        def add():
            return 'adding rbac user...'

print(Service.delete("httpbin"))
print(Service.create())
