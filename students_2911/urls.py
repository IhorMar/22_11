from django.contrib import admin
from django.urls import path

from students import views as all_views

urlpatterns = [
    # path(
    #     "test/", students_main.students_main, name="test_page"
    # ),  # Дві урли повісили на одну вюшку(students_main)
    # path(
    #     "empty/", students_main.students_main, name="test_page"
    # ),  # Дві урли повісили на одну вюшку(students_main)
    #
    # path("parse_request/", students_main.parse_request, name="parse_request"),
    # path("main_2/", students_main.main_page_render, name="main_2"),
    # path("test/<str:sid>/", students_main.students_personal, name="test_page_person"),
    path(
        "demonstration_page/", all_views.demonstration_page, name="demonstration_page"
    ),
    path("admin/", admin.site.urls),
    # Students url
    path("", all_views.students_list, name="main"),
    path("students/add/", all_views.students_add, name="students_add"),
    path("students/<int:sid>/edit/", all_views.students_edit, name="students_edit"),
    path(
        "students/<int:sid>/delete/", all_views.students_delete, name="students_delete"
    ),
    # Groups url
    # Journals url
]
