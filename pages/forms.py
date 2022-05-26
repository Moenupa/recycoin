from django import forms
from .models import *

class RecycoinForm(forms.ModelForm):
    class Meta:
        model = RecycoinModel
        fields = ['user', 'amount']