from django.shortcuts import render

# Create your views here.
def fornecedores(request):
    return render(request,'frontend/fornecedores.html' )

def logistica(request):
    return render(request, 'frontend/Menu/logistica.html')