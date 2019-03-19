from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


# def index(request):
#     return HttpResponse("Hello there")


class Home(generic.TemplateView):

    template_name = "personal_site/home.html"

    def get_queryset(self):
        pass


class Projects(generic.TemplateView):
    pass


class Resume(generic.TemplateView):
    pass


class About(generic.TemplateView):
    
    template_name = "personal_site/about.html"
