from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Alumno, Sesion, Desempeno, Historias, SabiasQue
from .serializers import AlumnoSerializer, SesionSerializer, DesempenoSerializer, HistoriasSerializer, SabiasQueSerializer


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

	def post(self, request):
		data=request.data
		nombreCompleto=data['nombreCompleto']
		alumno=Alumno.objects.filter(nombreCompleto=nombreCompleto)	
		print(alumno)
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


"""{
  "nombreCompleto":"NILTON STEVEEN VELEZ GARCIA"
}"""