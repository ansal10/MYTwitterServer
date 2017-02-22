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
    posts = Post.objects.all().order_by('-updated_at')
    posts = [p.to_json(keys=['user']) for p in posts]
    return JsonResponse({"results": posts})


@api_view(['GET', 'DELETE', 'PUT'])
def show(request, id=None):
    post = Post.objects.filter(Q(id=id)).order_by('-updated_at')
    if not post.exists():
        return JsonResponse({"error": "No post found for id %s" % id}, status=404)

    post = post.first()

    if request.method == 'GET':
        return JsonResponse({"result": post.to_json(keys=['user', 'comments'])})
    elif request.method == 'DELETE':
        post.delete()
        return JsonResponse({"result": "Deleted Successfully"})
    elif request.method == 'PUT':
        data = json.loads(request.body)
        if data['post'] is None or data['post'].strip() == '':
            return JsonResponse({"error": "Cannot update blank or empty post"}, status=400)
        post.post = data['post']
        post.save()
        return JsonResponse({"result": "Post updated Successfully"})


@api_view(['DELETE', 'PUT'])
def comment_index(request, id=None):
    comment = Comment.objects.filter(Q(id=id))
    if not comment.exists():
        return JsonResponse({"error": "No Comment found for id %s" % id}, status=404)

    if not comment.exists():
        return JsonResponse({"error": "Cannot find the comment with id %s" % id}, status=400)

    comment = comment.first()

    if request.method == 'DELETE':
        comment.delete()
        return JsonResponse({"result": "Deleted Successfully"})
    elif request.method == 'PUT':
        data = json.loads(request.body)
        if data['comment'] is None or data['comment'].strip() == '':
            return JsonResponse({"error": "Cannot update blank or empty comment"}, status=400)
        comment.comment = data['comment']
        comment.save()
        return JsonResponse({"result": "Comment updated Successfully"})
