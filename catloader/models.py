# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Cat(models.Model):
	name = models.CharField(max_length=20)
	picture = models.ImageField(upload_to='media')
