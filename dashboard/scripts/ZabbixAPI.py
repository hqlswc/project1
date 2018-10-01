#!/usr/bin/env python
# coding=utf-8
import json
import urllib2


class ZabbixAPI:
    def __init__(self):
        self.url = "http://1.85.33.61:8000/api_jsonrpc.php"
        self.user = ""
        self.password = ""
        self.header = {"Content-Type": "application/json"}
        self.tokenID = self.UserLogin()

    def UserLogin(self):
        data = {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": self.user,
                "password": self.password
            },
            "id": 0,
        }
        return self.PostRequest(data)

    # 推送请求
    def PostRequest(self, data):
        request = urllib2.Request(self.url, json.dumps(data), self.header)
        result = urllib2.urlopen(request)
        response = json.loads(result.read())
        try:
            return response['result']

        except KeyError:
            raise KeyError

    def HostGet(self):
        data = {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": ["name","status"],
#                "limit": 10,
#                "selectGroups": "extend",
#                "selectParentTemplates": ["templateid", "name"],
                "selectInterfaces": ["ip"],
#                "selectInventory": ["os"],
#                "selectItems": ["itemid", "name"],
#                "selectGraphs": ["graphid", "name"],
#                "selectApplications": ["applicationid", "name"],
#                "selectTriggers": ["triggerid", "name"],
#                "selectScreens": ["screenid", "name"]
            },
            "id": 1,
            "auth": self.tokenID,
        }
        return self.PostRequest(data)

    def HostGroupTreeGet(self):
        data = {
            "jsonrpc": "2.0",
            "method": "hostgroup.get",
            "params": {
                "output": ["name", "groupids"],
#                "limit": 1,
                "monitored_hosts": True,
                "sortfield": "groupid"
            },
            "id": 1,
            "auth": self.tokenID,
        }
        return self.PostRequest(data)

    def HostTreeGet(self, groupid=None):
        data = {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "groupids": groupid,
                "output": ["name"],
        },
            "id": 1,
            "auth": self.tokenID,
        }
        return self.PostRequest(data)

    def ItemGet(self, hostid=None, itemid=None):
        data = {
            "jsonrpc": "2.0",
            "method": "item.get",
            "params": {
                "output": "extend",
                "hostids": hostid,
                "sortfield": "name",
            },
            "id": 1,
            "auth": self.tokenID,
        }
        return self.PostRequest(data)

    def GraphGet(self, hostid=None, graphid=None):
        data = { 
            "jsonrpc": "2.0",
            "method": "graph.get",
            "params": {
                "output": "extend",
                "hostids": hostid,
                "graphids": graphid,
                "sortfield": "name"
            },  
            "id": 1,
            "auth": self.tokenID,
        }   
        request = urllib2.Request(self.url, json.dumps(data), self.header)
        result = urllib2.urlopen(request)
        response = json.loads(result.read())
        response["zbx_sessionid"] = self.tokenID
        try:
            return response
        except KeyError:
            raise KeyError

