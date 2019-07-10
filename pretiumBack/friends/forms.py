from django import forms
from friends.models import Friendship

class FriendshipCreation(forms.ModelForm):

    class Meta:
        model = Friendship
        fields = ['user1', 'user2', 'status']
