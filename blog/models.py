# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Post(models.Model):
	title = models.CharField(
						max_length=200,
						verbose_name="Título de la entrada"
					)
	body = models.TextField()
	tags = models.CharField(
						max_length=300,
						verbose_name="Contenido de la entrada"
					)
	show_image = models.BooleanField(
						default=True,
						verbose_name="Mostrar imagen"
					)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	image = models.ImageField(
						upload_to='media'
					)
	
	def __str__(self):
		return self.title

	def __unicode__(self):
		return self.title

	def thumbnail(self):
		if self.image:
			return u'<img src="%s" width=40 height=40 style="border-radius: 20px"/>' % (self.image_1x.url)
		else:
			return u'No image file found'
	thumbnail.short_description = 'Thumbnail image'
	thumbnail.allow_tags = True
