from django.urls import path
from .views import home, registro,registroMascotas,listarMascotas, login, eliminarMascota,modificarMascotas

urlpatterns = [
    path('', home, name="home"),
    path('registro/',registro,name='registro'),
    path('registroMascotas/',registroMascotas,name='registroMascotas'),
    path('listarMascotas/',listarMascotas,name='listarMascotas'),
    path('eliminarMascota/<id>',eliminarMascota,name='eliminarMascota'),
	path('modificarMascotas/<id>',modificarMascotas,name='modificarMascotas'),
    path('login/',login,name='login'),
	
    
]
