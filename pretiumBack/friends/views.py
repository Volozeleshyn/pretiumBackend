from django.shortcuts import render
from . import models
from . import forms
from django.http import JsonResponse, HttpResponse
# Create your views here.

@csrf_exempt
def get_friends(request):
    friends = request.POST['friends']
    user_id = request.POST['id']
    social_network = request.POST['social_network']
    for friend_id in friends:
        friend_id = social_network + friend_id
        data = {'user1': user_id,
                'user2': friend_id,
                'status': 1}
        f = FriendshipCreation(data)
        if f.is_valid():
            f.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=401)
