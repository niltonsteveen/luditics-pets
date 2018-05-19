from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class SabiasQue(models.Model):
	id=models.AutoField(primary_key=True)
	texto=models.CharField(max_length=400)
	habilitado=models.BooleanField(default=True)
	"""docstring for ClassName"""
	def __str__(self):
		return self.texto

class Permisos(models.Model):
	id=models.AutoField(primary_key=True)
	modulo=models.CharField(max_length=400)
	descripcion=models.CharField(max_length=400)
	"""docstring for ClassName"""
	def __str__(self):
		return self.id



class Historias(models.Model):
	id=models.AutoField(primary_key=True)
	texto=models.CharField(max_length=400)
	tipoMascota=models.CharField(max_length=5)
	habilitado=models.BooleanField(default=True)
	tipoOperacion=models.IntegerField(blank=False)
	nivel=models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

	def __str__(self):
		return self.texto


class Actividad(models.Model):
	id=models.AutoField(primary_key=True)
	texto=models.CharField(max_length=400)
	habilitado=models.BooleanField(default=True)
	"""docstring for ClassName"""
	def __str__(self):
		return self.texto

class Desempeno(models.Model):
	id=models.AutoField(primary_key=True)
	numeroAciertos=models.IntegerField()
	numeroFallos=models.IntegerField()
	nivel=models.IntegerField()
	tipoOperacion=models.IntegerField(blank=False)
	idAlumno=models.ForeignKey('Alumno',on_delete=models.CASCADE)
	idSesion=models.ForeignKey('Sesion',on_delete=models.CASCADE)
	fechaReporte=models.DateTimeField(auto_now_add=True)
	grupo=models.ForeignKey('Grupo',on_delete=models.CASCADE)
	def __str__(self):
		return str(self.id)



class Sesion(models.Model):
	idSesion=models.AutoField(primary_key=True)
	fechaInicio=models.DateTimeField(auto_now_add=True)
	idAlumno=models.ForeignKey('Alumno',on_delete=models.CASCADE)

	def __str__(self):
		return str(self.fechaInicio)


class Grupo(models.Model):
	id=models.AutoField(primary_key=True)
	grupoId=models.CharField(max_length=30)
	descripcion=models.CharField(max_length=200)

	def __str__(self):
		return str(self.grupoId)

class Alumno(models.Model):
	id=models.AutoField(primary_key=True)
	nombreCompleto=models.CharField(max_length=30)
	grupo=models.ForeignKey('Grupo',on_delete=models.CASCADE)

	def __str__(self):
		return self.nombreCompleto

class Grupo_Docente(models.Model):
	docente=models.ForeignKey('Docente',on_delete=models.CASCADE)
	grupo=models.ForeignKey('Grupo',on_delete=models.CASCADE)

	def __str__(self):
		return self.nombreCompleto

class Docente(models.Model):
	identificacion=models.IntegerField(primary_key=True)
	nombre=models.CharField(max_length=300)
	password=models.CharField(max_length=30)
	correo=models.CharField(max_length=355)
	rol=models.CharField(max_length=30)


	def __str__(self):
		return self.nombre
