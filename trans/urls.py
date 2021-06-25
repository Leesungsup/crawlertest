from django.urls import path, include
from .views import *
urlpatterns=[
    path("Hello/",hello),
    path("test/",test),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)