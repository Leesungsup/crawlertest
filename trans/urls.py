from django.urls import path, include
from .views import *
from django.conf.urls.static import static
urlpatterns=[
    path("Hello/",hello),
    path("test/",test),
]