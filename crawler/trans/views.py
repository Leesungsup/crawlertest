from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Quiz
from .models import Player_info
from .serializes import QuizSerializer
import random
# Create your views here.
def helloAPI(request):
    return Response("Hello world!")