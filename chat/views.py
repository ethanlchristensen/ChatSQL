from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django_tables2 import RequestConfig
from .forms import QueryForm
from .utils import OpenAIPrompter

PROMPTER = OpenAIPrompter()

# Create your views here.
@login_required
def home(request):
    """
    View to render out the home page
    """

    if request.method == "POST":
        form = QueryForm(request.POST)

        if form.is_valid():
            # get the query
            query = form.cleaned_data.get("query")
            # get the response from gpt, SQL
            sql = PROMPTER.complete(prompt=query)
            # process the SQL
            sql = sql.split("```")[1][3:]
            # get the template name
            template = "chat/home.html"
            # get the title
            title = "Home"
            # create the context
            context = {"title": title, "i_am": "home", "SQL": sql, "query": query, "form": QueryForm()}
            # render template
            return render(request, template_name=template, context=context)
    else:
        # get the template name
        template = "chat/home.html"
        # set the title
        title = "Home"
        # create the form to get the query from the user
        form = QueryForm()
        # create the context
        context = {"title": title, "i_am": "home", "form": form}
        # render the template
        return render(request, template_name=template, context=context)


def about(request):
    """
    View to render out the about page
    """

    # get the template name
    template = "chat/about.html"
    # get the title
    title = "About"
    # create the context
    context = {"title": title, "i_am": "about"}
    # render template
    return render(request, template_name=template, context=context)
