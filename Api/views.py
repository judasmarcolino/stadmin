from django.shortcuts import render

# Create your views here.
def fornecedores(request):
    return render(request,'frontend/fornecedores.html' )