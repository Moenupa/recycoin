from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.views import View

from pages.models import RecycoinModel, ExchangeRecordModel, PrizeModel
from .forms import ExchangeRequestForm, RecycoinForm

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"
    
class ExchangeFormView(View):
    template_name = "pages/exchange.html"
    form_class = ExchangeRequestForm

    def get(self, request, *args, **kwargs):
        prizes = PrizeModel.objects.all()
        return render(request, self.template_name, {'prizes': prizes})

    def post(self, request, *args, **kwargs):
        form = request.POST.get('prize_id')
        prize_id = int("".join(c for c in form if c.isdigit()))
        
        sel_prize = PrizeModel.objects.all().filter(id=prize_id)
        user = request.user
        if sel_prize and (user.wallet >= sel_prize[0].price):
            # print(f'{user} wallet increased')
            user.wallet -= sel_prize[0].price
            new_record = ExchangeRecordModel(user=user, prize=sel_prize[0], amount=sel_prize[0].price)
            new_record.save()
            user.save()
            return render(request, self.template_name, {
                    'prizes': sel_prize, 
                    'lock': True,
                    'msg': {
                            'level': 'success',
                            'content': f"Exchange success! You have exchanged {sel_prize[0].price} Recycoin for {sel_prize[0].item}."
                        }
                    })
        else:
            error = "not enough balance"

        prizes = PrizeModel.objects.all()
        return render(request, self.template_name, {
            'prizes': prizes, 
            'msg': {
                    'level': 'danger',
                    'content': f"Fail to exchange the prize: {error}."
                }
            })
    
class ExchangeHistoryView(View):
    template_name = "pages/history.html"
    
    def get(self, request, *args, **kwargs):
        records = request.user.exchanged_records.all()
        return render(request, self.template_name, {'records': records})
class GetCoinsHistory(View):
    template_name = "pages/history.html"
    
    def get(self, request, *args, **kwargs):
        records = request.user.recycled_coins.all()
        return render(request, self.template_name, {'records': records})
    
class GetCoinsFormView(View):
    form_class = RecycoinForm
    template_name = "pages/getcoins.html"
    recycled_to_coins_ratio = 5.0

    def get(self, request, *args, **kwargs):
        form = self.form_class({'recycledAmount': 0})
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            recycled = form.cleaned_data['recycledAmount']
            user = request.user
            amount = int(recycled / self.recycled_to_coins_ratio)
            
            new_coins = RecycoinModel(user=user, amount=amount, recycledAmount=recycled)
            new_coins.save()
            user.wallet += amount
            user.save()
            
            return redirect('/exchange/')

        return render(request, self.template_name, {'form': form})