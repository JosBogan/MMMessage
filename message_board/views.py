from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.


class ListView(APIView):

    def get(self, request):
        print('hello')