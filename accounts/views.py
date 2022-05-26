from django.shortcuts import render

# Create your views here.
from allauth.account.views import SignupView

class AccountSignupView(SignupView):
    # Signup View extended

    # change template's name and path
    template_name = "account/signup.html"

    # You can also override some other methods of SignupView
    # Like below:
    def form_valid(self, form):
        pass
    # def get_context_data(self, **kwargs):
    #     ...