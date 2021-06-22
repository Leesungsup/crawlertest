from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from .models import Player_info
import random
# Create your views here.
def hello(request):
    html="<html><body>Hello world!</body></html>"
    return HttpResponse(html)
def test(request):
    return render(request,'./templates/test.html')