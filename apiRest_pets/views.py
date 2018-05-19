from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from .models import Alumno, Sesion, Estadistica, Grupo_Docente, Texto, Tipo_Texto, Docente, Grupo, Permisos, Configuracion, Juego
from .serializers import AlumnoSerializer, PermisosSerializer, TextoSerializer, Tipo_TextoSerializer, GrupoSerializer, DocenteSerializer, Grupo_DocenteSerializer, ConfiguracionSerializer, SesionSerializer, EstadisticaSerializer, JuegoSerializer
from django.db.models import Sum, Count, Max, Min, DateField
from django.db.models.functions import Cast
from datetime import datetime

class Alumnos(APIView):

	def get(self, request):
		listaAlumnos=Alumno.objects.all()
		serializer= AlumnoSerializer(listaAlumnos, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer=AlumnoSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

	def put(self, request, format=None):
			alumno=Alumno.objects.filter(id=request.data['id'])
			print(request.data)
			serializer=AlumnoSerializer(alumno[0], data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			else:
				return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class AlumnoDetail(APIView):
	def get(self, request, pk, format=None):
		alumno=Alumno.objects.filter(id=pk)
		serializer= AlumnoSerializer(alumno[0], many=False)
		return Response(serializer.data)

	def delete(self, request, pk, format=None):
		alumno = Alumno.objects.filter(id=pk)
		alumno[0].delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class DocenteById(APIView):
	def post(self, request):
		docente=Docente.objects.get(identificacion=request.data['identificacion'])
		if docente == None:
			return Response(data={"error":"El docente ingresado no esta registrado"}, status=status.HTTP_400_BAD_REQUESTS)
		else:
			serializer=DocenteSerializer(docente, many=False)
			if serializer.is_valid() && serializer['password']==request.data['password']:				
				return Response(serializer.data)
			else:
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS)

class Docentes(APIView):

	def get(self, request):
		listaDocentes=Docente.objects.all()
		serializer= DocenteSerializer(listaDocentes, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer=DocenteSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

	def put(self, request, format=None):
		docente=Docente.objects.get(identificacion=request.data['id'])
		serializer=DocenteSerializer(docente, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
<<<<<<< HEAD
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS)
=======
			return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)			
>>>>>>> f81defff5514eaf56dde653c6c6f3b05c21ed35c


class Permisos(APIView):

	def get(self, request):
		listaPermisos=Permisos.objects.all()
		serializer= PermisosSerializer(listaPermisos, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer=PermisosSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

	def put(self, request, format=None):
		permiso=Permisos.objects.get(id=request.data['id'])
		serializer=PermisosSerializer(permiso, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
<<<<<<< HEAD
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS)
=======
			return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)		
>>>>>>> f81defff5514eaf56dde653c6c6f3b05c21ed35c


class Grupos(APIView):

	def get(self, request):
		listaGrupos=Grupo.objects.all()
		serializer= GrupoSerializer(listaGrupos, many=True)
		return Response(serializer.data)

	def post(self, request):
		data=request.data
		serializer=GrupoSerializer(data=request.data)
		print(data['id'])
		if serializer.is_valid():
			print('entro por aca')
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

	def put(self, request, format=None):
		grupo=Grupo.objects.get(id=request.data['id'])
		serializer=GrupoSerializer(grupo, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
<<<<<<< HEAD
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS)
=======
			return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
>>>>>>> f81defff5514eaf56dde653c6c6f3b05c21ed35c

class GruposDetail(APIView):
	def get(self, request, pk, format=None):
		grupo=Grupo.objects.filter(id=pk)
		serializer= GrupoSerializer(grupo[0], many=False)
		return Response(serializer.data)

	def delete(self, request, pk, format=None):
		grupo = Grupo.objects.filter(id=pk)
		grupo[0].delete()
		return Response(status=status.HTTP_204_NO_CONTENT)	

					

class Configuraciones(APIView):

	def get(self, request):
		config=Configuracion.objects.all()
		serializer= ConfiguracionSerializer(config, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer=ConfiguracionSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

	def put(self, request, format=None):
		config=Configuracion.objects.get(id=request.data['id'])
		serializer=ConfiguracionSerializer(config, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
<<<<<<< HEAD
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS)
=======
			return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)					
>>>>>>> f81defff5514eaf56dde653c6c6f3b05c21ed35c


class Sesiones(APIView):

	def get(self, request):
		listaSesiones=Sesion.objects.all()
		serializer= SesionSerializer(listaSesiones, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer=SesionSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
"""
	def put(self, request, format=None):
		sesion=Sesion.objects.get(fechaInicio=request.data['fechaInicio'])
		serializer=SesionSerializer(sesion, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

"""
class Estadisticas(APIView):

	def get(self, request):
		listaEstadisticas=Estadistica.objects.all()
		serializer= EstadisticaSerializer(listaEstadisticas, many=True)
		return Response(serializer.data)

	def post(self, request):	
		print(request.data['sesion'])

		serializer=EstadisticaSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

	def put(self, request, format=None):
		est=Estadistica.objects.get(id=request.data['id'])
		serializer=EstadisticaSerializer(est, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)



class Textos(APIView):
	def get(self, request):
		listaTextos=Texto.objects.all()
		serializer= TextoSerializer(listaTextos, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer=TextoSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

	def put(self, request, format=None):
		texto=Texto.objects.get(id=request.data['id'])
		serializer=TextoSerializer(texto, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

class Historias(APIView):
	def get(self, request):
		listaHistorias=Texto.objects.filter(tipoTexto=1)
		serializer= TextoSerializer(listaHistorias, many=True)
		return Response(serializer.data)

	def post(self, request):
		if request.data['tipoTexto'] == 1:
			serializer=TextoSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			else:
				return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
		else:
			return Response(data={"msg":"El texto ingresado no corresponde a una historia"})

	def put(self, request, format=None):
		if request.data['tipoTexto'] == 1:
			historia=Texto.objects.filter(id=request.data['id'])
			serializer=TextoSerializer(historia[0], data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			else:
				return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
		else:
			return Response(data={"msg":"El texto ingresado no corresponde a una historia"})
<<<<<<< HEAD

=======
>>>>>>> f81defff5514eaf56dde653c6c6f3b05c21ed35c

class HistoriasDetail(APIView):
	def get(self, request, pk, format=None):
		listaTextos=Texto.objects.filter(id=pk)
		serializer= TextoSerializer(listaTextos[0], many=False)
		return Response(serializer.data)

	def delete(self, request, pk, format=None):
		texto = Texto.objects.filter(id=pk)
		texto[0].delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class SabiasQue(APIView):
	def get(self, request):
		listaTextos=Texto.objects.filter(tipoTexto=2)
		serializer= TextoSerializer(listaTextos, many=True)
		return Response(serializer.data)

	def post(self, request):
		if request.data['tipoTexto'] == 2:
			serializer=TextoSerializer(data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			else:
				return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
		else:
			return Response(data={"msg":"El texto ingresado no corresponde a un sabías que"})

	def put(self, request, format=None):
		if request.data['tipoTexto'] == 2:
			historia=Texto.objects.filter(id=request.data['id'])
			serializer=TextoSerializer(historia[0], data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data)
			else:
				return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
		else:
			return Response(data={"msg":"El texto ingresado no corresponde a un sabías que"})

class SabiasQueDetail(APIView):
	def get(self, request, pk, format=None):
		print("has entrado muchacho")
		listaTextos=Texto.objects.filter(id=pk)	
		print(len(listaTextos))	
		serializer= TextoSerializer(listaTextos[0], many=False)
		return Response(serializer.data)

	def delete(self, request, pk, format=None):
		texto = Texto.objects.filter(id=pk)
		texto[0].delete()
		return Response(status=status.HTTP_204_NO_CONTENT)


class buscaAlumno(APIView):

	def get(self, request):
		username = request.GET.get('username','default')
		nombreCompleto=username
		alumno=Alumno.objects.filter(nombre_completo=nombreCompleto)
		if not alumno:
			return Response(data={"existe":False})
		else:
			serializer=AlumnoSerializer(alumno[0])
			respuesta={
				"nombre_completo":serializer.data['nombre_completo'],
				"id":serializer.data['id'],
				"grupo":serializer.data['grupo'],
				"existe":True
			}
			return Response(respuesta)

class barras(APIView):

	def post(self, request):
		try:
			data=request.data
			idEstudiante=data['idAlumno']
			fechaInicio=data['fechaInicio']
			fechaFin=data['fechaFin']
		except KeyError:
			return Response(data={"msg": " Datos ingresados de manera incorrecta"})
		query=Estadistica.objects.values('tipoOperacion', 'nivel').annotate(aciertos=Sum('numeroAciertos'), fallos=Sum('numeroFallos'))\
		.filter(sesion__idAlumno=idEstudiante, fechaReporte__gte=fechaInicio, fechaReporte__lte=fechaFin)
		if not query:
			return Response(data={"msg":"no se encontraron datos"})
		else:
			return Response(query)


class lineas(APIView):

	def post(self, request):
		try:
			data=request.data
			idEstudiante=data['idAlumno']
			fechaInicio=data['fechaInicio']
			fechaFin=data['fechaFin']
			sesiones=Sesion.objects.filter(fechaInicio__gte=fechaInicio, fechaInicio__lte=fechaFin)
		#sesion=Sesion.objects.first().fechaInicio
		except KeyError:
			return Response(data={"msg": " Datos ingresados de manera incorrecta"})

		"""query=Desempeno.objects.values('idSesion__fechaInicio').annotate(jugados=Count('idSesion'),fmax=Max('fechaReporte'), finicial=Min('fechaReporte'))\
		.filter(idAlumno=idEstudiante, idSesion__in=(sesiones))"""

		query=Estadistica.objects.values('sesion__idAlumno').annotate(jugados=Count('sesion'),fmax=Max('fechaReporte'), finicial=Min('sesion__fechaInicio'))\
		.filter(sesion__idAlumno=idEstudiante, sesion__in=(sesiones))


		if not query:
			return Response(data={"msg":"no se encontraron datos"})
		else:
			return Response(query)


class lineasMax(APIView):

	def post(self, request):
		try:
			data=request.data

			if len(data)==5:
				idEstudiante1=data['idEstudiante1']
				idEstudiante2=data['idEstudiante2']
				idEstudiante3=data['idEstudiante3']
				ids=[idEstudiante1,idEstudiante2,idEstudiante3]
			elif len(data)==4:
				idEstudiante1=data['idEstudiante1']
				idEstudiante2=data['idEstudiante2']
				ids=[idEstudiante1,idEstudiante2]
			elif len(data)==3:
				idEstudiante1=data['idEstudiante1']
				ids=[idEstudiante1]
			fechaInicio=data['fechaInicio']
			fechaFin=data['fechaFin']

			sesiones=Sesion.objects.filter(fechaInicio__gte=fechaInicio, fechaInicio__lte=fechaFin)
		except KeyError:
			return Response(data={"msg": " Datos ingresados de manera incorrecta"})
<<<<<<< HEAD

		query=Desempeno.objects.values('idAlumno', 'tipoOperacion').annotate(maxNivel=Max('nivel'))\
		.filter(idAlumno__in=ids, idSesion__in=(sesiones)).order_by('idAlumno','tipoOperacion')
=======
		
		query=Estadistica.objects.values('sesion__idAlumno', 'tipoOperacion').annotate(maxNivel=Max('nivel'))\
		.filter(sesion__idAlumno__in=ids, sesion__in=(sesiones)).order_by('sesion__idAlumno','tipoOperacion')
>>>>>>> f81defff5514eaf56dde653c6c6f3b05c21ed35c

		result= query.annotate(sesion=Cast("sesion__fechaInicio", DateField()))
		if not query:
			return Response(data={"msg":"no se encontraron datos"})
		else:
			return Response(result)


class cuenta(APIView):

	def post(self, request):
		try:
			data=request.data
			grupo=data['grupo']
			estudiantes=Alumno.objects.filter(grupo=grupo)
			fechaInicio=data['fechaInicio']
			fechaFin=data['fechaFin']
			sesiones=Sesion.objects.filter(fechaInicio__gte=fechaInicio, fechaInicio__lte=fechaFin)
		except KeyError:
			return Response(data={"msg": " Datos ingresados de manera incorrecta"})

		query=Estadistica.objects.values('sesion__idAlumno', 'tipoOperacion', 'sesion__fechaInicio').annotate(maxNivel=Max('nivel'))\
		.filter(sesion__idAlumno__in=estudiantes,sesion__in=sesiones)
		if not query:
			return Response(data={"msg":"no se encontraron datos"})
		else:
			response=query.values('tipoOperacion','nivel').annotate(cuenta=Count('sesion__idAlumno'))

			return Response(response)

class getEstudiantesPorGrupo(APIView):
	def get(self, request):
		grupo = request.GET.get('grupo','default')
		alumnos=Alumno.objects.filter(grupo=grupo)
		if not alumnos:
			return Response(data={"msg":"no hay alumnos en ese grupo"})
		else:
			serializer=AlumnoSerializer(alumnos, many=True)
			return Response(serializer.data)



"""{
  "nombreCompleto":"NILTON STEVEEN VELEZ GARCIA"
}"""
