from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


# def index(request):
#     return HttpResponse("Hello there")


class Homepage(generic.View):
    def get_queryset(self):
        pass
