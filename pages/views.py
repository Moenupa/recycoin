from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import redirect, render

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"
    
def home(request):
    cur_user = request.user
    print(cur_user.id)
    return render(request, 'pages/home.html')

def signup(request):
    return render(request, 'pages/signup.html')