from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect


from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request,'main/home.html')


#

