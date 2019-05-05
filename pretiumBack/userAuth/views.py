import json

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate

from rest_framework import status

from . import serializers
from . import models


@csrf_exempt
def auth_login_username(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        serializer = serializers.UserSerializer(user)
        return JsonResponse(serializer.data)
    return HttpResponse(status=401)


@csrf_exempt
def auth_login_email(request):
    email = request.POST['email']
    password = request.POST['password']
    user_exists = models.User.objects.get(email=email)
    if user_exists:
        user = authenticate(username=user_exists.username, password=password)
        login(request, user)
        serializer = serializers.UserSerializer(user)
        return JsonResponse(serializer.data)
    return HttpResponse(status=401)


@csrf_exempt
def signup(request):
    if models.User.objects.filter(username=request.POST['username']).exists():
        return HttpResponse(status=403)
    elif models.User.objects.filter(email=request.POST['email']).exists():
        return HttpResponse(status=405)
    else:
        u = models.User(username=request.POST['username'], email=request.POST['email'],
                        fullname=request.POST['fullname'])
        u.set_password(request.POST['password'])
        u.save()
        login(request, u)
        serializer = serializers.UserSerializer(u)
        return JsonResponse(serializer.data)


def auth_logout(request):
    logout(request)
    return HttpResponse(status=200)


@csrf_exempt
def change_password(request):
    uid = request.POST['uid']
    new_password = request.POST['new_password']
    user_exists = models.User.objects.get(uid=uid)
    if user_exists:
        user_exists.set_password(new_password)
        user_exists.save()
        return HttpResponse(status=200)
    return HttpResponse(status=401)
