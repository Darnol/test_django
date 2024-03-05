# Map URL to Views

from django.urls import path
from . import views

urlpatterns = [
    path("hello/", views.say_hello),
    path("hello/noname", views.say_hello_noname)
]