from django.contrib import admin
from django.urls import include, path


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
    # admin urls
    path("admin/", admin.site.urls),
    # others urls
    path("students/", include("students.students.urls")),
    path("journal/", include("students.journal.urls")),
    path("groups/", include("students.groups.urls")),
]
