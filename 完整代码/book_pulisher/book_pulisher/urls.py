"""book_pulisher URL Configuration

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
from django.conf.urls import url
from app01 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^login/', views.login),

    url(r'^publisher_list/', views.publisher_list),
    url(r'^add_publisher/', views.add_publisher),
    url(r'^delete_publisher/', views.delete_publisher),
    url(r'^edit_publisher/', views.edit_publisher),

    url(r'^book_list/', views.book_list),
    url(r'^add_book/', views.add_book),
    path('delete_book/', views.delete_book),
    path('edit_book/', views.edit_book),

    path('author_list/', views.auther_list),
    path('add_author/', views.add_author),
    path('delete_author/', views.delete_author),
    path('edit_author/', views.edit_author),

    url(r'^test/', views.test),
]
