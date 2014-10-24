# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response as rtr
from models import Printer_List

def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    printer = Printer_List()
    printer_list = printer.li()
    context_dict = {'printers':printer_list}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return rtr('index/index.html', context_dict, context)

def about(request):
    context=RequestContext(request)
    return rtr('index/about.html',{},context)
