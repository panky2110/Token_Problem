"""Token_Assignment URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from rest_framework_swagger.views import get_swagger_view
from  django.conf.urls import url
from token_app.helper import *
from token_app.views import *
schema_view = get_swagger_view(title='pool')
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'swagger/', schema_view),
    path('generate_token',generate_token),
    path('get_all_token',get_all_token),
    path('delete_token/<int:tid>',delete_token),
    path('assign',assign_token),
    path('unassign/<int:tid>',unassign_token),
    path('keep_alive/<int:tid>',keep_alive_token),
    path('keep_assign/<int:tid>',keep_assign_alive_token)

]
