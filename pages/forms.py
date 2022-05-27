from django import forms
from .models import *

class RecycoinForm(forms.ModelForm):
    class Meta:
        model = RecycoinModel
        fields = ['recycledAmount']
        
class ExchangeRequestForm(forms.ModelForm):
    class Meta:
        model = ExchangeRecordModel
        fields = ['prize']
