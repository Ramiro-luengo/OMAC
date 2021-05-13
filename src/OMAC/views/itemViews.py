from django import template
from django.db import reset_queries
from django.http import HttpResponse
from django.http.request import HttpRequest
from django.template import context, loader
from django.shortcuts import render

# Check imports before doing them.
from OMAC.models.Item import Item


def home(request):
    if request.method == 'GET':
        template = loader.get_template("core/home.html")
        context = {}
        return HttpResponse(template.render(context,request))

def item_list(request: HttpRequest):

    if request.method == 'GET':
        item_id = request.GET.get('filtro')
        items = list(Item.objects.all())
        context = {'item_list' : items}
        if item_id:
            context = {'item_list' : [Item.objects.get(id=item_id)]}
        return HttpResponse(render(request, 'core/items.html', context))

def item(request,name):
    i = Item.objects.get(name=name)
    response = "<p>Name: " + i.name + "</p>\n"
    response = response + "<p>Price: " + str(i.price) + "</p>\n"
    response = response + "<p>Description: " + i.description + "</p>\n"

    return HttpResponse(response)