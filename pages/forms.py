from django import forms
from .models import *

class RecycoinForm(forms.ModelForm):
    class Meta:
        model = RecycoinModel
        fields = ['user', 'amount']
        
class ExchangeRecordForm(forms.ModelForm):
    class Meta:
        model = ExchangeRecordModel
        fields = ['user', 'prize']