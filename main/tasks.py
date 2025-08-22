# main/tasks.py
from celery import shared_task
import time

@shared_task
def add(x, y):
    """Una tarea simple que suma dos números y simula un trabajo largo."""
    print(f"Ejecutando tarea: sumando {x} + {y}")
    time.sleep(10)  # Simula un trabajo que tarda 10 segundos
    result = x + y
    print(f"Tarea completada: {x} + {y} = {result}")
    return result

@shared_task
def print_hello():
    """Una tarea programada que simplemente imprime un mensaje."""
    print("Hola desde una tarea programada de Celery Beat!")