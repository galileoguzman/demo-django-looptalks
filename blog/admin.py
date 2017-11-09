# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog.models import Post

# Register your models here.
'''
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'post_status', 'updated_at','thumbnail', )
	list_filter = ('created_at',)
'''
# Register your models here.
admin.site.register(Post)