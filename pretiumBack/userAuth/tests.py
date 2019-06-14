from django.test import TestCase
from .views import signup
from .models import User
from django.http import HttpRequest, QueryDict


class UserAuthTestCase(TestCase):

    def test_create_model_and_check(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST = QueryDict.__init__(request.POST, 'email=vasyapupkin1988@gmail.com&username=Vasiliy&fullname=Vasiliy Ivanovich Pupkin&password=velosiped124', True)
        signup(request)
        if User.objects.filter(username='Vasiliy').exists():
            self.assertEqual(User.objects.filter(username='Vasiliy').password, 'velosiped124')
        elif User.objects.filter(email='vasyapupkin1988@gmail.com').exists():
            self.assertEqual(User.objects.filter(username='Vasiliy').password, 'velosiped124')
        else:
            self.assertTrue(False)
