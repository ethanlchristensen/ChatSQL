from django.urls import path

from .views import *

urlpatterns = [
    path("", view=home, name="chat-home"),
    path("about/", view=about, name="chat-about")
]