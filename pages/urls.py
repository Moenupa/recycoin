from django.urls import path

from .views import *

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("exchange/", ExchangeFormView.as_view(), name="exchange"),
    path("getcoins/", GetCoinsFormView.as_view(), name="coins"),
]
