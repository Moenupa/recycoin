from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.views import View

from pages.models import PrizeModel
from .forms import RecycoinForm

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"
    
class ExchangeFormView(TemplateView):
    template_name = "pages/exchange.html"

    def get(self, request, *args, **kwargs):
        prizes = PrizeModel.objects.all()
        return render(request, self.template_name, {'prizes': prizes})

    def post(self, request, *args, **kwargs):
        prize = request.POST.get('prize')
        prize_id = int("".join([c for c in prize if c.isdigit()]))
        print("form:", prize_id)

        sel_prize = PrizeModel.objects.all().filter(id=prize_id)
        # TODO: add the prize to the user's account and decrease its wallet by the prize's amount
        # and add a record to exchange_history
        return render(request, self.template_name, {'prizes': sel_prize, 'msg': f"You have selected a prize:", 
                                                    'lock': True})
    
class GetCoinsFormView(View):
    form_class = RecycoinForm
    template_name = "pages/getcoins.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class({'user': request.user})
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})