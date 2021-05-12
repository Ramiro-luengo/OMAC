from django import template
from django.db import reset_queries
from django.http import HttpResponse
from django.template import context, loader
from .models import Item


def home(request):
    template = loader.get_template("core/home.html")
    context = {}
    # Se puede setear context. context = {'algo' : 'algo'}
    # return HttpResponse(template.render(context,request))
    return HttpResponse(template.render(context,request))

def item_list(request):
    items = list(Item.objects.all())
    response = "<h1>ItemList:\n<ul>"
    for i in items:
        response = response + "<li>"
        response = response + "<p>Name: " + i.name + "</p>\n"
        response = response + "</li>"
    
    response = response + "</ul></h1>"

    return HttpResponse(response)

def item(request,name):
    i = Item.objects.get(name=name)
    response = "<p>Name: " + i.name + "</p>\n"
    response = response + "<p>Price: " + str(i.price) + "</p>\n"
    response = response + "<p>Description: " + i.description + "</p>\n"

    return HttpResponse(response)