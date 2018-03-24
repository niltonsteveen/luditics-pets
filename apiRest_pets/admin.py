from django.contrib import admin
from .models import Alumno, Sesion, Estadistica, Grupo_Docente, Texto, Tipo_Texto, Docente, Grupo, Permisos, Configuracion, Juego


# Register your models here.

admin.site.register(Alumno)
admin.site.register(Sesion)
admin.site.register(Estadistica)
admin.site.register(Grupo_Docente)
admin.site.register(Texto)
admin.site.register(Tipo_Texto)
admin.site.register(Docente)
admin.site.register(Grupo)
admin.site.register(Permisos)
admin.site.register(Configuracion)
admin.site.register(Juego)
