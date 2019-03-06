from django.shortcuts import render
from rest_framework import viewsets
from .models import Map
from .serializers import MapSerializers
from django.views.generic.base import View
from django.http import HttpResponse


class MapView(viewsets.ModelViewSet):
    queryset = Map.objects.all()
    serializer_class = MapSerializers


"""
返回token
"""

def user(request):
    if request.method == 'POST':
        account = request.POST.get('account')
        passwd = request.POST.get('passwd')
        print(account)
        print(passwd)

    return HttpResponse('haha')