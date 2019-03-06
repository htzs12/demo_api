from django.urls import path
from .views import MapView,UsersView


app_name = 'demo'

urlpatterns = [
    path('',MapView.as_view(),name='map'),
    path('users/',UsersView.as_view(),name='user')
]