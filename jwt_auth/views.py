from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_422_UNPROCESSABLE_ENTITY

from .serializers import UserSerializer

# Create your views here.

class RegisterView(APIView):

    def post(self, req):
        serialized_user = UserSerializer(data=req.data)
        if serialized_user.is_valid():
            serialized_user.save()
            return Response({'message': 'Registration Sucessfull'})

        return Response(serialized_user.errors, status=HTTP_422_UNPROCESSABLE_ENTITY)

