# core/celery.py
import os
from celery import Celery

# Establece el módulo de configuración de Django para el programa 'celery'.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# Usa una cadena aquí para que el worker no tenga que serializar
# el objeto de configuración a los procesos hijos.
# - namespace='CELERY' significa que todas las claves de configuración de Celery
#   deben tener un prefijo `CELERY_` en settings.py.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Carga automáticamente los módulos de tareas de todas las aplicaciones registradas en Django.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')