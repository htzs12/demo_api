from django.urls import path
from .views import MapView,user


app_name = 'demo'

urlpatterns = [
    path('',MapView.as_view(),name='map'),
    
]