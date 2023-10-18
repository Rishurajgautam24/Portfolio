from django.shortcuts import render
from django.http import HttpResponse
# request 

from django.shortcuts import render



# Create your views here.

def home(request):
    return render(request, 'home.html')







