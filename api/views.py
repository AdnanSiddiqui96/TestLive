from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response

# Create your views here.
    


class result(APIView):

    def get(self,request):

        data = results.objects.values()
        return Response({'status':True,'data':data})

    def post(self,request):

        name = request.data.get('name')
        result = request.data.get('result')                     
        data = results(name = name,result=result)
        data.save()
        return Response({'status':True,'message':"Add new result successfully"})