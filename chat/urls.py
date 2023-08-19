from django.urls import path

from .views import *

urlpatterns = [
    path("", view=home),
    path("about/", view=about)
]