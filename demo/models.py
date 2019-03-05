from django.db import models
from datetime import datetime

# Create your models here.


class Map(models.Model):
    """
    地图资源模型
    """
    title = models.CharField(max_length=50,verbose_name='监控点名称')
    longitude = models.FloatField(verbose_name='经度')
    latitude = models.FloatField(verbose_name='纬度')
    dev_id = models.CharField(max_length=50,verbose_name='设备id')
    status = models.BooleanField(default=True,verbose_name='设备状态')
    address = models.CharField(max_length=50,null=True, blank=True, verbose_name='监控地址')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='添加时间')

    class Meta:
        verbose_name = '云平台模型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title