"""
URL configuration for students_2911 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from students import views as students_main

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("test/", students_main.students_main, name='test_page'),
    path("", students_main.students_main, name="test_page"),
    path("parse_request/", students_main.parse_request, name="parse_request"),
    path("test/<str:sid>/", students_main.students_personal, name="test_page_person"),
]
