from rest_framework import serializers
from .models import Alumno
from .models import Sesion
from .models import Estadistica
from .models import Texto
from .models import Tipo_Texto
from .models import Permisos
from .models import Grupo
from .models import Docente
from .models import Grupo_Docente
from .models import Juego
from .models import Configuracion


""" /////////////////DONE/////////////////////"""

class AlumnoSerializer(serializers.ModelSerializer):

	class Meta:
		model=Alumno
		fields=('id','nombre_completo','grupo')

class SesionSerializer(serializers.ModelSerializer):

	class Meta:
		model=Sesion
		fields=('id', 'fechaInicio', 'idAlumno','juego')

class GrupoSerializer(serializers.ModelSerializer):

	class Meta:
		model=Grupo
		fields=('id', 'descripcion')

class Grupo_DocenteSerializer(serializers.ModelSerializer):

	class Meta:
		model=Grupo_Docente
		fields=('docente', 'grupo')

class DocenteSerializer(serializers.ModelSerializer):

	class Meta:
		model=Docente
		fields=('id', 'nombre', 'contrasena', 'correo')

class TextoSerializer(serializers.ModelSerializer):

	class Meta:
		model=Texto
		fields=('id', 'tipoTexto', 'habilitado', 'descripcion')

class JuegoSerializer(serializers.ModelSerializer):

	class Meta:
		model=Juego
		fields=('id', 'descripcion', 'configuracion')

class ConfiguracionSerializer(serializers.ModelSerializer):

	class Meta:
		model=Configuracion
		fields=('id', 'rangoMin', 'rangoMax', 'orden', 'ayuda', 'numPorOp')

class Tipo_TextoSerializer(serializers.ModelSerializer):

	class Meta:
		model=Tipo_Texto
		fields=('id', 'nombre')

class EstadisticaSerializer(serializers.ModelSerializer):

	class Meta:
		model=Estadistica
		fields=('id','numeroAciertos','numeroFallos', 'nivel', 'tipoOperacion','fechaReporte','sesion')

class PermisosSerializer(serializers.ModelSerializer):

	class Meta:
		model=Permisos
		fields=('id', 'modulo', 'descripcion')