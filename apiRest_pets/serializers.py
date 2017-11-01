from rest_framework import serializers
from .models import Alumno
from .models import Sesion
from .models import Desempeno
from .models import Historias
from .models import SabiasQue

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
		fields=('id', 'numeroAciertos', 'numeroFallos','nivel', 'tipoOperacion', 'idAlumno', 'idSesion', 'fechaReporte')


class HistoriasSerializer(serializers.ModelSerializer):

	class Meta:
		model=Historias
		fields=('id', 'texto', 'tipoMascota', 'habilitado','tipoOperacion')


class SabiasQueSerializer(serializers.ModelSerializer):

	class Meta:
		model=SabiasQue
		fields=('id', 'texto', 'habilitado')
