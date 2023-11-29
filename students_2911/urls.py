from django.contrib import admin
from django.urls import path

from students import views as students_main

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "test/", students_main.students_main, name="test_page"
    ),  # Дві урли повісили на одну вюшку(students_main)
    path(
        "", students_main.students_main, name="test_page"
    ),  # Дві урли повісили на одну вюшку(students_main)
    path("parse_request/", students_main.parse_request, name="parse_request"),
    path("test/<str:sid>/", students_main.students_personal, name="test_page_person"),
]
