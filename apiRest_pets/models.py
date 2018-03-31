from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.

class Texto(models.Model):
	id=models.AutoField(primary_key=True)
	tipoTexto=models.ForeignKey('Tipo_Texto',on_delete=models.CASCADE)
	habilitado=models.BooleanField(default=True)
	descripcion=models.CharField(max_length=400)
	tipoMascota=models.CharField(max_length=400, blank=True, null=True)
	tipoOperacion=models.IntegerField(blank=True, null=True)
	nivel=models.IntegerField(blank=True, null=True)
	"""docstring for ClassName"""
	def __str__(self):
		return self.descripcion

class Permisos(models.Model):
	id=models.AutoField(primary_key=True)
	modulo=models.CharField(max_length=400)
	descripcion=models.CharField(max_length=400)
	"""docstring for ClassName"""
	def __str__(self):
		return self.descripcion

class Juego(models.Model):
	id=models.CharField(primary_key=True, max_length=30)
	descripcion=models.CharField(max_length=400)
	configuracion=models.OneToOneField('Configuracion', on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return self.descripcion

class Configuracion(models.Model):
	id=models.AutoField(primary_key=True)
	rangoMin=models.IntegerField()
	rangoMax=models.IntegerField()
	ayuda=models.IntegerField()
	orden=models.BooleanField(default=True)
	numPorOP=models.IntegerField()

	def __str__(self):
		return str(self.id)

class Sesion(models.Model):
	id=models.AutoField(primary_key=True)
	fechaInicio=models.DateTimeField(auto_now_add=True)
	idAlumno=models.ForeignKey('Alumno',on_delete=models.CASCADE)
	juego=models.ForeignKey('Juego', on_delete=models.CASCADE)
	
	def __str__(self):
		return str(self.fechaInicio)

class Alumno(models.Model):
	id=models.AutoField(primary_key=True)
	nombre_completo=models.CharField(max_length=30)
	grupo=models.ForeignKey('Grupo',on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre_completo

class Grupo(models.Model):
	id=models.CharField(primary_key=True, max_length=30)
	descripcion=models.CharField(max_length=200)

	def __str__(self):
		return self.id

class Grupo_Docente(models.Model):
	docente=models.ForeignKey('Docente',on_delete=models.CASCADE)
	grupo=models.ForeignKey('Grupo',on_delete=models.CASCADE)

	def __str__(self):
		return str(self.docente)+' '+str(self.grupo)

class Docente(models.Model):
	id=models.IntegerField(primary_key=True)
	nombre=models.CharField(max_length=30)
	contrasena=models.CharField(max_length=30)
	correo=models.CharField(max_length=100)

	def __str__(self):
		return self.nombre

class Tipo_Texto(models.Model):
	id=models.IntegerField(primary_key=True)
	nombre=models.CharField(max_length=30)

	def __str__(self):
		return self.nombre

class Estadistica(models.Model):
	id=models.AutoField(primary_key=True)
	numeroAciertos=models.IntegerField()
	numeroFallos=models.IntegerField()
	nivel=models.IntegerField(blank=True, null=True)
	tipoOperacion=models.IntegerField()
	fechaReporte=models.DateTimeField(auto_now_add=True)
	sesion=models.ForeignKey('Sesion',on_delete=models.CASCADE)

	def __str__(self):
		return str(self.id)