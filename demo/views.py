from django.shortcuts import render
from rest_framework import viewsets
from .models import Map
from .serializers import MapSerializers
from django.views.generic.base import View
from django.http import HttpResponse,JsonResponse


class MapView(viewsets.ModelViewSet):
    queryset = Map.objects.all()

    def get(self,request):
        rec = request.META
        body = request.body
        print(rec)
        print(body)
    serializer_class = MapSerializers


"""
返回token
"""

def user(request):
    if request.method == 'POST':
        data = {}
        account = request.POST.get('account')
        passwd = request.POST.get('passwd')
        if account == 'haoge' and passwd == '123456':
            data = {'token':'xxx123456xxx','user_id':'111','ret':400}
        else:
            data = {}
    return JsonResponse(data=data)