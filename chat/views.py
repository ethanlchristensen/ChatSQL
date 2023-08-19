from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django_tables2 import RequestConfig

# Create your views here.
@login_required
def home(request):
    """
    View to render out the home page
    """

    # get the template name
    template = "pull/home.html"
    # set the title
    title = "Home"
    # create the context
    context = {"title": title, "i_am": "home"}
    # render the template
    return render(request, template_name=template, context=context)


def about(request):
    """
    View to render out the about page
    """

    # get the template name
    template = "pull/about.html"
    # get the title
    title = "About"
    # create the context
    context = {"title": title, "i_am": "about"}
    # render template
    return render(request, template_name=template, context=context)
