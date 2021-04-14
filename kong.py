import requests
import json

api_host = "10.0.0.4"
api_port = "9015"
rbac_enable = False
tls = False
super_admin = ""
super_passwd = ""


if tls:
    api_proto = "https://"
else:
    api_proto = "http://"


class Service:

    def __init__(self, name):
        self.name = name
        c = requests.get(api_proto + api_host + ":" + api_port + "/services/" + self.name)
        if c.status_code == 404:
            self.exists = False
        else:
            self.exists = True
            self.service_json = json.loads(c.content)
            for k, v in self.service_json.items():
                setattr(self, k, v)
        pass



    def create(self, proto, host, port, path):
        port = str(port)
        c = requests.post(api_proto + api_host + ":" + api_port + "/services",
                          data={'name': self.name,
                                'protocol': proto,
                                'host': host,
                                'port': port,
                                'path': path})
        r = json.loads(c.content.decode("UTF-8"))
        self.service_json = json.loads(c.content)
        for k, v in self.service_json.items():
            setattr(self, k, v)
        return r


    def delete(self):
        c = requests.delete(api_proto + api_host + ":" + api_port + "/services/" + self.name)
        if c.status_code == 204:
            return c.status_code
        else:
            return c.content

    class Route:
        def __init__(self, name):
            self.name = name
            pass

        def add(self, **kwargs):

            request_data = {}
            for k, v in kwargs.items():
                if k == 'service_name':
                    pass
                else:
                    request_data[k] = v

            c = requests.post(
                api_proto + api_host + ":" + api_port + "/services/" + self.name + "/routes/",
                data=request_data)

            r = json.loads(c.content.decode("UTF-8"))
            return r


        def delete(rt_name):
            c = requests.delete(api_proto + api_host + ":" + api_port + "/routes/" + rt_name)
            return c.status_code

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