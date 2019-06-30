import json

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.db.utils import IntegrityError
from . import helper

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
        new_hash = helper.create_hash()
        while 1:
            try:
                user = models.User(username=request.POST['username'], email=request.POST['email'],
                                   fullname=request.POST['fullname'], hash_id=new_hash)
                user.set_password(request.POST['password'])
                user.save()
                login(request, user)
                serializer = serializers.UserSerializer(user)
                return JsonResponse(serializer.data)
            except IntegrityError:
                new_hash = helper.create_hash()
                pass


def auth_logout(request):
    logout(request)
    return HttpResponse(status=200)


@csrf_exempt
def change_password(request):
    id = request.POST['id']
    new_password = request.POST['new_password']
    user_exists = models.User.objects.get(hash_id=id)
    if user_exists:
        user_exists.set_password(new_password)
        user_exists.save()
        return HttpResponse(status=200)
    return HttpResponse(status=401)


@csrf_exempt
def check_id(request):
    id = request.POST['id']
    user_exists = models.User.objects.get(hash_id=id)
    if user_exists:
        serializer = serializers.UserSerializer(user_exists)
        return JsonResponse(serializer.data)
    return HttpResponse(status=401)


@csrf_exempt
def get_sn_data(request):
    email = request.POST['email']
    username = request.POST['username']
    user_exists = models.User.objects.get(email=email)
    if user_exists:
        return HttpResponse(status=403)
    user_exists = models.User.objects.get(username=username)
    if user_exists:
        return HttpResponse(status=401)
    user = models.User(username=request.POST['username'], email=request.POST['email'],
                       fullname=request.POST['fullname'], hash_id='social_network')
    user.set_password(request.POST['password'])
    user.save()
    login(request, user)
    serializer = serializers.UserSerializer(user)
    return JsonResponse(serializer.data)
