"""messenger_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from messenger.views import login_view, messages_view, new_message_view, message_sent_view, full_message_view, logout_view, change_password_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', messages_view, name='inbox'),
    path('outbox/', messages_view, {'folder': 'outbox'}, name='outbox'),
    path('new/', new_message_view, name='write'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('message/<int:id>/', full_message_view, name='full_message'),
    path('change_password/', change_password_view, name='change_password')
]
