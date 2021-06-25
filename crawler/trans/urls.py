from django.urls import path, include
from .views import *
urlpatterns=[
    path("Hello/",hello),
    path("test/",test),
]