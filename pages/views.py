from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.views import View
from .forms import RecycoinForm, ExchangeRecordForm

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"
    
class ExchangeFormView(TemplateView):
    form_class = ExchangeRecordForm
    template_name = "pages/exchange.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class({'user': request.user, 'amount': 0})
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})
    
class GetCoinsFormView(View):
    form_class = RecycoinForm
    template_name = "pages/getcoins.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class({'user': request.user})
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})