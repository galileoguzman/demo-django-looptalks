# urls.py
from django.conf.urls import include, url
from blog import views as blog_views



from tastypie.api import Api
from blog.api import PostResource

api_v1 = Api(api_name='v1')
api_v1.register(PostResource())


urlpatterns = [
    url(r'^blog/$', blog_views.index_blog, name='index_blog'),
    # for API
    url(r'^api/', include(api_v1.urls)),
]