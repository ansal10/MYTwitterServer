import json

from django.db.models import Q
from django.http import JsonResponse
from rest_framework.decorators import api_view

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

        return JsonResponse({"results": user.to_json()})


@api_view(['POST'])
def login(request):
    data = json.loads(request.body)
    for key in ['username', 'password']:
        if data.get(key) is None or data.get(key).strip() == "":
            return JsonResponse({"error": "%s is Required" % key}, status=400)
    user = Users.objects.filter(Q(username=data['username']) & Q(password=data['password']))
    if user.__len__() > 0:
        return JsonResponse({"results": "login successful"})
    else:
        return JsonResponse({"error": "Username and Password not Matched"}, status=401)

