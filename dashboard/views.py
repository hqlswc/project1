# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import json
from django.shortcuts import render, render_to_response
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from scripts.ZabbixAPI import ZabbixAPI


# Create your views here.
def index(request):
    print "Do Index."
    return render(request, 'dashboard/index.html')

def asset(request):
    print "Do asset."
    z = ZabbixAPI()
    assets = z.HostGet()
    return render(request, 'dashboard/asset.html', locals())

def asset_ztree(request):
    print "Do asset_ztree."
    zNodes = []
    z = ZabbixAPI()
    HostGroupTree = z.HostGroupTreeGet()
    for i in HostGroupTree:
        zNode = {
            "name": i["name"],
            "id": i["groupid"],
        }
        zNodes.append(zNode)
    return HttpResponse(json.dumps(zNodes))

def asset_ztree_children(req):
    print "*****children zNode*****"
    groupid = req.POST.get('groupids')
    print "view: groupid is ",groupid
    zNodes = []
    z = ZabbixAPI()
    HostTree = z.HostTreeGet(groupid)
    for i in HostTree:
        zNode = {
            "name": i["name"],
            "pId": groupid
        }
        zNodes.append(zNode)
    print "view: zNode is ",json.dumps(zNodes)
    return HttpResponse(json.dumps(zNodes))

def asset_item(request):
    print "Do asset item." 
    hostid = request.GET.get("hostid", None)
    z = ZabbixAPI()
    items = z.ItemGet(hostid)
    return render(request, 'dashboard/item.html', locals())

def asset_graph(request):
    print "Do asset graph."
    hostid = request.GET.get("hostid")
    period = request.GET.get("period", 3600)
    if hostid is None:
        return HttpResponseNotFound("Error: Could not found this page !")
    else:
        z = ZabbixAPI()
        data = z.GraphGet(hostid)
        zbx_sessionid = data["zbx_sessionid"]
        response = render(request, 'dashboard/graph.html', locals())
        response.set_cookie('zbx_sessionid', zbx_sessionid)
        return response
