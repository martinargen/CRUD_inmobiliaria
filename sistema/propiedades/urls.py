from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('inmuebles', views.inmuebles, name='inmuebles'),
    path('inmuebles/crear', views.crear, name='crear'),
    path('inmuebles/editar', views.editar, name='editar'),
    path('borrar/<int:id>', views.borrar, name='borrar'),
    path('inmuebles/editar/<int:id>', views.editar, name='editar')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)