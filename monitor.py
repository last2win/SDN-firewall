# -*- coding: utf-8 -*-

from __future__ import print_function
from scapy.all import *
from firewall_judge import judge_payload
import requests
count = 0

#controllerIP = "192.168.32.140"

controllerIP = "10.0.0.4"
controllerPort = 8080
controllerURL = "http://"+controllerIP+":"+str(controllerPort)+"/"
url = controllerURL+"firewall/rules/0000000000000001"
httpPayload = ""
stopCount = 0
iface = 'h3-eth1'


def stop(packet):
    global controllerURL, url, stopCount
    stopCount += 1
    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
    payload = '{"nw_src": "'+str(packet[IP].src)+'", "nw_dst": "' + \
        str(packet[IP].dst) + \
        '", "nw_proto": "TCP", "actions": "DENY", "priority": "10"}'

    r = requests.post(url=url, data=payload, headers=headers)
    print("[3] add new rule, payload is ", payload)
    if r.text == '':
        print("add new rule error!")
    else:
        temp = eval(r.text)[0]
        if temp['command_result'][0]['result'] != 'success':
            print(" add new rule fail!!!")
            print(r.text)
        else:
            print("[4] add new rule success")
  #      print("response is ",r.text)


def judge(packet, payload=''):
    print("[1] start judge, payload is "+payload)
    if judge_payload(payload) == 1:
        print("[2] it is an evil payload")
        stop(packet)
    else:
        print("[2] it is a normal payload")


def http_header(packet):
 #   global httpPayload
    if packet.haslayer(Raw):
        temp = packet.getlayer(Raw).load.decode("utf-8")
        if 'GET' in temp:
            httpPayload = temp[temp.find('GET')+3:temp.find('HTTP')].strip()
            judge(packet, httpPayload)
            return True
    return False

print("firewall monitor start!")

dpkt = sniff(
    iface=iface,
    lfilter=http_header,
    filter="tcp", count=0)
