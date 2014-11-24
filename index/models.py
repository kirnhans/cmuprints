from django.db import models
from jsonTest import *
import urllib2
import json
import string
from printerSetup import getPrinterList

class PrinterList(models.Model):
    plist=printerList

Printers = PrinterList()

def getInfo():
    info = urllib2.urlopen('http://198.211.113.33:3000/printers')
    str_info = ''
    for line in info:
        str_info += line
    return str_info

def updateData():
    encoded_object = getInfo()
    myobj_instance = MyDecoder().decode(encoded_object)

class Printer(object):
    def __init__(self, name):
        self.fullName = name
        self.parseName(name)
        self.status = None
        self.error = None
        self.icon = None

    def parseName(self, name):
        start = name.find('-')
        if start == -1:
            self.name = "Name Error"
        else:
            name = name[start+2:]
            self.name = name
            if name.endswith("B&W"):
                #self.name = name[:len(name)-len("B&W")]
                self.color = False
            else:
                #self.name = name[:len(name)-len("Color")]
                self.color = True

    def __repr__(self):
        return "%s: %s (%s)" % (self.name, self.icon, self.error)
        
    def setIcon(self, msg):
        if msg == "go.gif":
            status = "available"
        elif msg == "yield.gif":
            status = "warning"
        elif msg == "stop.gif":
            status = "not working"
        else:
            status = "unknown"
        self.icon = status
    def getIcon(self):
        return self.icon
    
    def setStatus(self, msg):
        self.status = msg
    def getStatus(self):
        return self.status

    def setErrorMessage(self, msg):
        self.error = msg
    def getErrorMessage(self):
        return self.error


class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.dict_to_object)

    def dict_to_object(self, d):
        if 'name' in d:
            fullName = d.pop('name')
            for printer in printerList:
                if printer == fullName:
                    if 'ready' in d:
                        printer.setStatus(d.pop('ready'))
                    if 'icon' in d:
                        printer.setIcon(d.pop('icon'))
                    if 'status' in d:
                        printer.setErrorMessage(d.pop('status'))

encoded_object = getInfo()
myobj_instance = MyDecoder().decode(encoded_object)

for printer in Printers.plist:
    print printer.status
