from django.db import models
from jsonTest import *
import urllib2
import json
import string
from printerSetup import getPrinterList

class PrinterList(models.Model):
    def __init__(self):
        self.plist=getPrinterList()
        super(PrinterList, self).__init__()

    def getInfo(self):
        req = urllib2.Request('http://198.211.113.33:3000/printers')
        response = urllib2.urlopen(req)
        the_page = response.read()
        return the_page

    def updateData(self):
        encoded_object = self.getInfo()
        myobj_instance = MyDecoder(self.plist).decode(encoded_object)

class MyDecoder(json.JSONDecoder):
    def __init__(self, plist):
        self.plist = plist
        json.JSONDecoder.__init__(self, object_hook=self.dict_to_object)

    def dict_to_object(self, d):
        if 'name' in d:
            fullName = d.pop('name')
            for printer in self.plist:
                if printer == fullName:
                    if 'ready' in d:
                        printer.setStatus(d.pop('ready'))
                    if 'icon' in d:
                        printer.setIcon(d.pop('icon'))
                    if 'message' in d:
                        printer.setErrorMessage(d.pop('message'))

Printers = PrinterList()
