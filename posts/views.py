import json

from django.db.models import Q
from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view

from posts.models import Post, Comment
from users.models import Users





@api_view(['GET'])
def index(request):
    posts = Post.objects.all()
    posts = [p.to_json(keys=['user']) for p in posts]
    return JsonResponse({"results": posts})


@api_view(['GET'])
def show(request, id=None):
    post = Post.objects.filter(Q(id=id))
    if not post.exists():
        return JsonResponse({"error": "No post found for id %s" % id}, status=404)

    post = post.first()
    return JsonResponse({"result": post.to_json(keys=['user', 'comments'])})



