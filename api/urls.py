"""zeitgeist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from .api_events import *
from .api_user_activate import *

urlpatterns = [
    path('events/all',APIEvent.as_view()),
    path('events/tech',APIEvent.as_view(type="tech")),
    path('events/cult',APIEvent.as_view(type="cult")),
    path('events/register-approve',APIEventRegisterApprove.as_view()),
    path('events/register',APIEventRegister.as_view()),
    path('events/payment',APIEventPayment.as_view()),

    path('account/info',APIAccountInfo.as_view()),
    path('account/info-update',APIAccountInfoUpdate.as_view()),
]
