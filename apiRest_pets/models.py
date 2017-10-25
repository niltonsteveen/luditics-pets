from django.db import models

# Create your models here.

class SabiasQue(models.Model):
	id=models.AutoField(primary_key=True)
	texto=models.CharField(max_length=400)
	habilitado=models.BooleanField(default=True)
	"""docstring for ClassName"""
	def __str__(self):
		return self.texto



class Historias(models.Model):
	id=models.AutoField(primary_key=True)
	texto=models.CharField(max_length=400)
	tipoMascota=models.CharField(max_length=5)
	habilitado=models.BooleanField(default=True)
	tipoOperacion=models.IntegerField(blank=False)

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

	def __str__(self):
		return self.id



class Sesion(models.Model):
	fechaInicio=models.DateTimeField(auto_now_add=True,primary_key=True)
	idAlumno=models.ForeignKey('Alumno',on_delete=models.CASCADE)

	def __str__(self):
		return self.fechaInicio



class Alumno(models.Model):
	id=models.AutoField(primary_key=True)
	nombreCompleto=models.CharField(max_length=30)
	grupo=models.CharField(max_length=5)

	def __str__(self):
		return self.nombreCompleto

