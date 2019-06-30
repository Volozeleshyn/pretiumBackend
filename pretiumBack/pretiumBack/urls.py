"""pretiumBack URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from userAuth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/email', views.auth_login_email),
    path('login/username', views.auth_login_username),
    path('logout', views.auth_logout),
    path('signup', views.signup),
    path('change_password', views.change_password),
    path('check_id', views.check_id),
    path('get_sn_data', views.get_sn_data)
]
