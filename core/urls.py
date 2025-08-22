from django.contrib import admin
from django.urls import path
from main.views import home
from django.conf import settings
from django.conf.urls.static import static

# core/urls.py
from main.views import home, run_task_view # Importa la nueva vista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('run-task/', run_task_view, name='run_task'), # <--- AÑADE ESTA LÍNEA
]

if settings.DEBUG is False: # O True si quieres que funcione en ambos
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)