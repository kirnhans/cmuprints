import urllib2
import json
import string
from printerSetup import getPrinterList

printerList = getPrinterList()

def getInfo():
    info = urllib2.urlopen('http://198.211.113.33:3000/printers')
    str_info = ''
    for line in info:
        str_info += line
    return str_info

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
for printer in printerList:
    print printer
