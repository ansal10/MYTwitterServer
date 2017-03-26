from django.http import JsonResponse
from django.shortcuts import render
from virtualmall.models import Users
import json

# Create your views here.
from rest_framework.decorators import api_view


@api_view(['POST'])
def registration(request):
    data = json.loads(request.body)

    emailId = data.get('emailId')
    firstName = data.get('firstName')
    lastName = data.get('lastName')
    password = data.get('password')
    confirmPassword = data.get('confirmPassword')
    role = data.get('role')
    contactNumber = data.get('contactNumber')

    for field in ['emailId', 'password', 'role', 'contactNumber']:
        if data.get(field) is None or data.get(field).__str__().strip() == "":
            return JsonResponse({"error": "%s is Required" % field}, status=400)

    if password != confirmPassword:
        return JsonResponse({"error": "Password and confirmed password not matched"}, status=400)

    if role not in ['seller', 'buyer']:
        return JsonResponse({"error": "Role can either be seller or buyer"}, status=400)

    user = Users(emailId=emailId, firstName=firstName, lastName=lastName, password=password, role=role,
                 contactNumber=contactNumber)
    user.save()
    return JsonResponse({"status": "ok"})
