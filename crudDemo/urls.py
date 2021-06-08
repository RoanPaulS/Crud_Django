"""crudDemo URL Configuration

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
from crudApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('crud/',views.retrieve_view , name = "crud"),
    path('create/',views.create_view , name="create"),
    path('delete/<id>',views.delete_view , name="Delete"),
    path('update/<id>',views.update_view , name="Update"),
]
