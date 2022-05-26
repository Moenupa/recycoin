from django import forms
from .models import *

class RecycoinForm(forms.ModelForm):
    class Meta:
        model = RecycoinModel
        fields = ['user','caption']
        
class ExchangeRecordFrom(forms.ModelForm):
    class Meta:
        model = ExchangeRecordModel
        fields = ['user', 'item_id']