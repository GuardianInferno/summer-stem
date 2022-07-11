from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserInfoSerializer
from .models import userInfo
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

# Create your views here.
@api_view(['GET', 'POST'])
def get_post(request):
    if request.method == 'GET':
        info = userInfo.objects.all()
        serializer = UserInfoSerializer(info, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        info_data = JSONParser().parse(request)
        serializer = UserInfoSerializer(data=info_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT'])
def get_put(request,pk):
    try:
        info = userInfo.objects.get(pk=pk)
    except:
        pass
    if request.method == 'GET':
        serializer = UserInfoSerializer(info)
        return Response(serializer.data)
    elif request.method == 'PUT':
        info_data = JSONParser().parse(request)
        serializer = UserInfoSerializer(info, data=info_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




