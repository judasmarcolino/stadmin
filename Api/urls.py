from django import urls
from django.urls import path
from . import views


urlpatterns = [


    #Logistic
    path('logistica', views.logistica, name="logistica"),
    path('',views.fornecedores, name="fornecedores"),
    

    path("prospensao", views.prospensao, name="prospensao")
    
]

