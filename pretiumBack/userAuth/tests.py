from django.test import TestCase, RequestFactory
from .views import signup
from .models import User
from django.http import HttpRequest, QueryDict
from django.contrib.sessions.backends.db import SessionStore


class UserAuthTestCase(TestCase):

    def test_create_model_and_check(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST = QueryDict('email=vasyapupkin1988@gmail.com&username=Vasiliy&fullname=Vasiliy Ivanovich Pupkin&password=velosiped124')
        request.session = SessionStore()
        signup(request)
        user_obj1 = User.objects.get(username='Vasiliy')
        user_obj2 = User.objects.get(email='vasyapupkin1988@gmail.com')
        if user_obj1:
            self.assertEqual(user_obj1.email, 'vasyapupkin1988@gmail.com')
        elif user_obj2:
            self.assertEqual(user_obj2.username, 'Vasiliy')
        else:
            self.assertTrue(False)
