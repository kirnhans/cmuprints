import urllib2
import json
import string

printerList = []

class Printer(object):
    def __init__(self, name):
        #self.fullName = name
        self.parseName(name)
        self.location = "TBD"
        self.status = None
        self.error = None
        self.icon = None

    def parseName(self, name):
        start = name.find('-')
        if start == -1:
            self.name = "Name Error"
        else:
            name = name[start+2:]
            self.fullName = name
            self.id = name.replace(" ", "")
            if name.endswith("B&W"):
                self.name = name[:len(name)-len(" B&W")]
                self.color = False
            else:
                self.name = name[:len(name)-len(" Color")]
                self.color = True

    def __repr__(self):
        return "%s (%s): %s (%s)" % (self.name, self.id, self.icon, self.error)

    def __eq__(self, other):
        if isinstance(other, Printer):
            return self.fullName == other.fullName
        else:
            return self.fullName == other
        
    def setIcon(self, msg):
        if msg == "go.gif":
            status = "Available"
        elif msg == "yield.gif":
            status = "Warning"
        elif msg == "stop.gif":
            status = "Not working"
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
            printer = Printer(d.pop('name'))
            printerList.append(printer)

def getPrinterList():
    encoded_object = getInfo()
    myobj_instance = MyDecoder().decode(encoded_object)
    return printerList
