from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>¡Hola, EasyPanel! Mi proyecto Django está funcionando.</h1>")