# main/views.py
from django.http import HttpResponse
from .tasks import add

def home(request):
    return HttpResponse("<h1>¡Hola, EasyPanel! Mi proyecto Django está funcionando.</h1><p><a href='/run-task/'>Ejecutar tarea en segundo plano</a></p>")

def run_task_view(request):
    # Llama a la tarea para que se ejecute en segundo plano.
    # .delay() es el atajo para enviar la tarea al broker.
    add.delay(5, 7)
    return HttpResponse("La tarea de sumar 5 + 7 ha sido enviada al worker. Tardará 10 segundos en completarse. Revisa los logs del worker.")