from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import *
from users.serializers import*
class GetStudentsView(APIView):

 def get(self,request):
    print("req",request.get)
    name=request.get.get("my name")
    print("name",name)
    if name:
     instance = Students.object.filter()
     instance = Students.objects.all()
     serializers=studentserializers(instance,many=True)
     return Response('serializer'.data)

 
 



