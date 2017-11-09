# myapp/api.py
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS

from tastypie.authorization import DjangoAuthorization
from tastypie.cache import SimpleCache
from blog.models import Post



class PostResource(ModelResource):

	class Meta:
		queryset = Post.objects.all()
		resource_name = 'posts'
		allowed_methods = ['get']
		

