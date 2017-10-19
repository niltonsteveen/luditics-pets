from django.contrib import admin
from .models import Alumno
from .models import Sesion
from .models import Historias
from .models import SabiasQue
from .models import Desempeno


# Register your models here.

admin.site.register(Alumno)
admin.site.register(Sesion)
admin.site.register(Historias)
admin.site.register(SabiasQue)
admin.site.register(Desempeno)
