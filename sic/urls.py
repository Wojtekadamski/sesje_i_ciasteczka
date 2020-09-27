"""sic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from sesjeiciasteczka import views

urlpatterns = [
    path('admin/', admin.site.urls),
path('', views.Index.as_view()),
path('show_session/', views.ShowSessionView.as_view()),
path('set_session/', views.SetSessionView.as_view()),
path('delete_session/', views.DelSessionView.as_view()),
path('set_cookie/', views.SetCookieView.as_view()),
path('show_cookie/', views.ShowCookieView.as_view()),
path('show_sessionkeyvalue/', views.ShowSessionKeyValue.as_view()),
path('set_sessionkeyvalue/', views.SetSessionKeyValue.as_view()),
path('del_sessionkeyvalue/', views.DelSessionKeyValue.as_view()),


]
