from django.contrib import admin
from django.urls import path

from students import views as work_views

# urlpatterns = [
#     # path(
#     #     "test/", students_main.students_main, name="test_page"
#     # ),  # Дві урли повісили на одну вюшку(students_main)
#     # path(
#     #     "empty/", students_main.students_main, name="test_page"
#     # ),  # Дві урли повісили на одну вюшку(students_main)
#     #
#     # path("parse_request/", students_main.parse_request, name="parse_request"),
#     # path("main_2/", students_main.main_page_render, name="main_2"),
#     # path("test/<str:sid>/", students_main.students_personal, name="test_page_person"),
#     path(
#         "demonstration_page/", all_views.demonstration_page, name="demonstration_page"
#     ),
#     path("admin/", admin.site.urls),
#     # Students url
#     path("", all_views.students_list, name="main"),
#     path("students/add/", all_views.students_add, name="students_add"),
#     path("students/<int:sid>/edit/", all_views.students_edit, name="students_edit"),
#     path(
#         "students/<int:sid>/delete/", all_views.students_delete, name="students_delete"
#     ),
#     # Groups url
#     path("groups_all/", all_views.groups_list, name="groups_all"),
#     path("groups/add/", all_views.groups_list_add, name="groups_list_add"),  # add
#     path(
#         "groups/<int:gid>/edit/", all_views.groups_list_edit, name="groups_list_edit"
#     ),  # edit
#     path(
#         "groups/<int:gid>/delete/",
#         all_views.groups_list_delete,
#         name="groups_list_delete",
#     ),  # delete
#     # Journals url
#     path("journal/<int:sid>", all_views.journal_list, name="journal")
# ]

urlpatterns = [
    path("admin/", admin.site.urls),
    # Students urls
    path("", work_views.students_list, name="home"),
    path("students/add/", work_views.students_add, name="students_add"),
    path("students/<int:sid>/edit/", work_views.students_edit, name="students_edit"),
    path(
        "students/<int:sid>/delete/", work_views.students_delete, name="students_delete"
    ),
    # Groups urls
    path("groups/", work_views.groups_list, name="groups"),
    path("groups/add/", work_views.groups_add, name="groups_add"),
    path("groups/<int:gid>/edit/", work_views.groups_edit, name="groups_edit"),
    path("groups/<int:gid>/delete/", work_views.groups_delete, name="groups_delete"),
    # Journals url
    path("journal/", work_views.journal_list, name="journal"),
]
