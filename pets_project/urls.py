"""pets_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from apiRest_pets import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^alumnos/', views.Alumnos.as_view()),
    url(r'^sesiones/', views.Sesiones.as_view()),
    url(r'^desempenos/', views.Desempenos.as_view()),
    url(r'^historias/', views.Histories.as_view()),
    url(r'^sabiasQue/', views.Sabiasque.as_view()),
    url(r'^buscaAlumno/', views.buscaAlumno.as_view()),
    url(r'^barras/', views.barras.as_view()),
    url(r'^lineas/', views.lineas.as_view()),
    url(r'^lineasMax/', views.lineasMax.as_view()),
    url(r'^cuenta/', views.cuenta.as_view()),
]
