from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
    path('reg', RegisterAPIView.as_view()),
    path('log', LoginAPIView.as_view()),
    path('don/food', DonateFoodAPIView.as_view()),
    path('acc/food',DonateFoodReceveAPIVIEW.as_view() ),

    path('don/gros', DonateGroceryAPIView.as_view()),
    path('acc/gros',DonateGroceryReceveAPIVIEW.as_view() ),

    path('don/req', RequestAPIView.as_view()),
    path('acc/req',RequestReceveAPIVIEW.as_view() ),

    path('food',GETDonateFoodAPIView.as_view()),
    path('gros',GETDonateGroceryAPIView.as_view()),
    path('req',GETRequestAPIView.as_view()),
    path('user',GETCustomUserAPIView.as_view()),
]