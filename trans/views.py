from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Player_info
import random
# Create your views here.
def helloAPI(request):
    return Response("Hello world!")