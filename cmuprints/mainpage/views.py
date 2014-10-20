# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Page under work. Check back soon!")

def about(request):
    return HttpResponse("Project by Kim Kleiven, Jenna Choo, Clark Chen and Kirn Hans")
