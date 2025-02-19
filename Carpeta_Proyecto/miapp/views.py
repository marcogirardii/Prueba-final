from django.shortcuts import render

# Create your views here.

def index(request):
    gracias = {"mensaje": "Gracias por visitar mi página"}
    return render(request, 'miapp/index.html', gracias)
