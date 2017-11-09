# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from blog.models import Post



# Create your views here.

def index_blog(request):
	index_template = "blog.html"
	post = Post.objects.all().order_by('-created_at')
	
	return render(request,index_template, {
		'posts': post
	})


def detail_post(request, slug):

	post = get_object_or_404(Post, slug=slug)
	
	return render(request, 'app/blog-details.html', {
		'posts': post,
		'title_page': post.title
	})