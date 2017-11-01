from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Alumno, Sesion, Desempeno, Historias, SabiasQue
from .serializers import AlumnoSerializer, SesionSerializer, DesempenoSerializer, HistoriasSerializer, SabiasQueSerializer
from django.db.models import Sum, Count, Max, Min

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
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS)

	def put(self, request, format=None):
		alumno=Alumno.objects.get(id=request.data['id'])
		serializer=AlumnoSerializer(alumno, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS)


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
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS)

	def put(self, request, format=None):
		sesion=Sesion.objects.get(fechaInicio=request.data['fechaInicio'])
		serializer=SesionSerializer(sesion, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS)


class Desempenos(APIView):

	def get(self, request):
		listaDesempenos=Desempeno.objects.all()
		serializer= DesempenoSerializer(listaDesempenos, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer=DesempenoSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS)

	def put(self, request, format=None):
		des=Desempeno.objects.get(id=request.data['id'])
		serializer=DesempenoSerializer(des, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS)



class Histories(APIView):


	def get(self, request):
		listaHistorias=Historias.objects.all()
		serializer= HistoriasSerializer(listaHistorias, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer=HistoriasSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS)

	def put(self, request, format=None):
		historia=Historias.objects.get(id=request.data['id'])
		serializer=HistoriasSerializer(historia, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS)



class Sabiasque(APIView):

	def get(self, request):
		listaSabiasQue=SabiasQue.objects.all()
		serializer= SabiasQueSerializer(listaSabiasQue, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer=SabiasQueSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS)

	def put(self, request, format=None):
		sabiasque=SabiasQue.objects.get(id=request.data['id'])
		serializer=SabiasQueSerializer(sabiasque, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUESTS)


class buscaAlumno(APIView):

	def get(self, request):
		username = request.GET.get('username','default')
		nombreCompleto=username
		alumno=Alumno.objects.filter(nombreCompleto=nombreCompleto)
		if not alumno:
			return Response(data={"existe":False})
		else:
			serializer=AlumnoSerializer(alumno[0])
			respuesta={
				"nombreCompleto":serializer.data['nombreCompleto'],
				"id":serializer.data['id'],
				"grupo":serializer.data['grupo'],
				"existe":True
			}
			return Response(respuesta)

class barras(APIView):

	def post(self, request):
		data=request.data
		nombreEstudiante=data['estudiante']
		grupo=data['grupo']
		estudiante=Alumno.objects.get(nombreCompleto=nombreEstudiante , grupo=grupo)
		grupo=estudiante.grupo
		idEstudiante=estudiante.id
		fechaInicio=data['fechaInicio']
		fechaFin=data['fechaFin']
		query=Desempeno.objects.values('tipoOperacion', 'nivel').annotate(aciertos=Sum('numeroAciertos'), fallos=Sum('numeroFallos'))\
		.filter(idAlumno=idEstudiante, fechaReporte__gte=fechaInicio, fechaReporte__lte=fechaFin)
		return Response(query)


class lineas(APIView):

	def post(self, request):
		data=request.data
		nombreEstudiante=data['estudiante']
		grupo=data['grupo']
		estudiante=Alumno.objects.get(nombreCompleto=nombreEstudiante , grupo=grupo)
		grupo=estudiante.grupo
		idEstudiante=estudiante.id
		fechaInicio=data['fechaInicio']
		fechaFin=data['fechaFin']



		query=Desempeno.objects.values('idSesion').annotate(jugados=Count('idSesion'),fmax=Max('fechaReporte'), finicial=Min('fechaReporte'))\
		.filter(idAlumno=idEstudiante, idSesion__gte=fechaInicio, idSesion__lte=fechaFin)

		return Response(query)


class lineasMax(APIView):

	def post(self, request):
		data=request.data
		nombreEstudiante1=data['estudiante1']
		nombreEstudiante2=data['estudiante2']
		nombreEstudiante3=data['estudiante3']
		grupo=data['grupo']
		estudiante1=Alumno.objects.get(nombreCompleto=nombreEstudiante1 , grupo=grupo)
		idEstudiante1=estudiante1.id
		estudiante2=Alumno.objects.get(nombreCompleto=nombreEstudiante2 , grupo=grupo)
		idEstudiante2=estudiante2.id
		estudiante3=Alumno.objects.get(nombreCompleto=nombreEstudiante3 , grupo=grupo)
		idEstudiante3=estudiante3.id
		ids=[idEstudiante1,idEstudiante2,idEstudiante3]
		fechaInicio=data['fechaInicio']
		fechaFin=data['fechaFin']


		query=Desempeno.objects.values('idAlumno', 'tipoOperacion', 'idSesion').annotate(maxNivel=Max('nivel'))\
		.filter(idAlumno__in=ids, idSesion__gte=fechaInicio, idSesion__lte=fechaFin)

		return Response(query)


class cuenta(APIView):

	def post(self, request):
		data=request.data
		grupo=data['grupo']
		estudiantes=Alumno.objects.filter(grupo=grupo)
		fechaInicio=data['fechaInicio']
		fechaFin=data['fechaFin']


		query=Desempeno.objects.values('idAlumno', 'tipoOperacion', 'idSesion').annotate(maxNivel=Max('nivel'))\
		.filter( idAlumno__in=estudiantes,idSesion__gte=fechaInicio, idSesion__lte=fechaFin)

		response=query.values('tipoOperacion','nivel').annotate(cuenta=Count('idAlumno'))

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
