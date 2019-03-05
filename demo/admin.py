from django.contrib import admin
from .models import Map


class MapsAdmin(admin.ModelAdmin):
    list_display = ['title','longitude','latitude','dev_id','status','address','add_time']


admin.site.register(Map,MapsAdmin)