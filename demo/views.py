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
        account = request.POST.get('account')
        passwd = request.POST.get('passwd')
        if account == 'haoge' and passwd == '123456':
            data = {'token':'xxx123456xxx','user_id':'111','ret':400}
        else:
            data = {}
    return JsonResponse(data=data)


def del_map(request):
    if request.method == 'POST':
        dev_id = request.POST.get('dev_id')
        Map.objects.filter(dev_id=dev_id).delete()
        print('删除设备成功，请刷新页面～')
        data = {'status_code':200,'status':'deleted'}
        return JsonResponse(data=data, status_code=200)
