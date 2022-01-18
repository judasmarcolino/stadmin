from django.shortcuts import render

# Create your views here.
def fornecedores(request):
    return render(request,'frontend/fornecedores.html' )

def logistica(request):
    return render(request, 'frontend/Menu/logistica.html')

def prospensao(request):
    return render(request, 'frontend/prospensao.html')

def projecto(request):
    return render (request, 'frontend/pojecto.html' )