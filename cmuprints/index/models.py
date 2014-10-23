from django.db import models

# Create your models here.
class Printer():
    def __init__(self):
        self.name="Test"
        self.id=3
    #need to use JSON here to create printer
    
class Printer_List(models.Model):
    def li(self):
        return [Printer()]
