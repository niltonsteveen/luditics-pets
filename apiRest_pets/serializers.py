from rest_framework import serializers
from .models import Alumno
from .models import Sesion
from .models import Desempeno
from .models import Historias
from .models import SabiasQue
from .models import Permisos
from .models import Actividad
from .models import Grupo
from .models import Docente
from .models import Grupo_Docente

class AlumnoSerializer(serializers.ModelSerializer):

	class Meta:
		model=Alumno
		fields=('id','nombreCompleto','grupo')


class SesionSerializer(serializers.ModelSerializer):

	class Meta:
		model=Sesion
		fields=('idSesion', 'fechaInicio', 'idAlumno')


class DesempenoSerializer(serializers.ModelSerializer):

	class Meta:
		model=Desempeno
		fields=('id', 'numeroAciertos', 'numeroFallos','nivel', 'tipoOperacion', 'idAlumno', 'idSesion', 'fechaReporte', 'grupo')


class HistoriasSerializer(serializers.ModelSerializer):

	class Meta:
		model=Historias
		fields=('id', 'texto', 'tipoMascota', 'habilitado','tipoOperacion', 'nivel')


class SabiasQueSerializer(serializers.ModelSerializer):

	class Meta:
		model=SabiasQue
		fields=('id', 'texto', 'habilitado')

class PermisosSerializer(serializers.ModelSerializer):

	class Meta:
		model=Permisos
		fields=('id', 'modulo', 'descripcion')

class ActividadSerializer(serializers.ModelSerializer):

	class Meta:
		model=Actividad
		fields=('id', 'texto', 'habilitado')

class GrupoSerializer(serializers.ModelSerializer):

	class Meta:
		model=Grupo
		fields=('id', 'grupoId', 'descripcion')


class DocenteSerializer(serializers.ModelSerializer):

	class Meta:
		model=Docente
		fields=('identificacion', 'nombre', 'password', 'correo', 'rol')

class Grupo_DocenteSerializer(serializers.ModelSerializer):

	class Meta:
		model=Grupo_Docente
		fields=('docente', 'grupo')
