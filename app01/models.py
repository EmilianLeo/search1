#!/usr/bin/python
#-- coding:utf8 --
from django.db import models

# Create your models here.

class wx01(models.Model):
    # id=models.AutoField(primary_key=True)
    # 机柜=models.CharField(max_length=32)
    IPMI=models.CharField(max_length=32)
    USER=models.CharField(max_length=32)
    PASS=models.CharField(max_length=32)

    def __str__(self):
        return self.IPMI















