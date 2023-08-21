from django.urls import path

from .views import *

urlpatterns = [
    path("chatsql/", view=home, name="chat-sql-home"),
    path("chatsql/about/", view=about, name="chat-sql-about"),
]