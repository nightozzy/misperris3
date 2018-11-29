"""misperris URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import redirect
def logout_view(request):
    logout(request)
    return redirect('')
	
urlpatterns = [
	path('', include('core.urls')),
	path('',include('django.contrib.auth.urls')),
	path('admin/', admin.site.urls),
	path('oauth/', include('social_django.urls', namespace='social')),#agregaremos las url necesarias
	path('', include('pwa.urls')),
]
#Personalizacion de titulos de admin



admin.site.site_header="Administración de Mis perris"
admin.site.index_title="Mis perris"
admin.site.site_title="Adminisración Mis perris"