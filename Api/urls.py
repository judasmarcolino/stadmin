from django import urls
from django.urls import path
from . import views


urlpatterns = [

    path('fornecedores',views.fornecedores, name="fornecedores")
    
]

