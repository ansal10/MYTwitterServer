import json

from django.db.models import Q
from django.http import JsonResponse
from rest_framework.decorators import api_view

from posts.models import Post, Comment
from users.models import Users


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        users = Users.objects.defer('password').all()
        data = [user.to_json() for user in users]
        return JsonResponse({"results": data})

    elif request.method == 'POST':
        data = json.loads(request.body)
        for key in ['first_name', 'last_name', 'email', 'username', 'password']:
            if data.get(key) is None or data.get(key).strip() == "":
                return JsonResponse({"error": "%s is Required" % key}, status=400)
        user = Users.objects.filter(Q(username=data['username']) | Q(email=data['email']))
        if user.__len__() > 0:
            return JsonResponse({"error": "User already registered with same username OR Email"}, status=400)
        user = Users(**data)
        user.save()

        return JsonResponse({"result": user.to_json()})


@api_view(['POST'])
def login(request):
    data = json.loads(request.body)
    for key in ['username', 'password']:
        if data.get(key) is None or data.get(key).strip() == "":
            return JsonResponse({"error": "%s is Required" % key}, status=400)
    user = Users.objects.filter(Q(username=data['username']) & Q(password=data['password']))
    if user.__len__() > 0:
        return JsonResponse({"result": user[0].to_json()})
    else:
        return JsonResponse({"error": "Username and Password not Matched"}, status=401)


@api_view(['POST'])
def post(request, username=None):
    user = Users.objects.filter(Q(username=username))
    if not user.exists():
        return JsonResponse({"error": "Posting post for Unknown User"}, status=400)
    user = user.first()

    # POST
    if request.method == 'POST':
        data = json.loads(request.body)
        for key in ['post']:
            if data.get(key) is None:
                return JsonResponse({"error": "%s is Required" % key}, status=400)

        post = Post(**data)
        post.user = user
        post.save()
        return JsonResponse({"result": post.to_json()})

    # GET
    elif request.method == 'GET':
        posts = Post.objects.filter(user__username=username)
        posts = [p.to_json(keys=['user']) for p in posts]
        return JsonResponse({"results": posts})


@api_view(['POST'])
def comment(request, username=None, post_id=None):
    post = Post.objects.filter(Q(id=post_id))
    user = Users.objects.filter(Q(username=username))

    if not post.exists() or not user.exists():
        return JsonResponse({"error": "Cannot comment for unknown user or post"}, status=400)
    user = user.first()
    post = post.first()

    data = json.loads(request.body)
    for key in ['comment']:
        if data.get(key) is None:
            return JsonResponse({"error": "%s is required" % key}, status=400)

    comm = Comment(comment=data['comment'], user=user, post=post)
    comm.save()

    return JsonResponse({"result": comm.to_json(keys=['user', 'post'])})