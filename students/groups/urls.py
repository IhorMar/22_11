from django.urls import path

from . import views as groups_views

urlpatterns = [
    # Groups urls
    path("groups/", groups_views.groups_list, name="groups"),
    path("groups/add/", groups_views.groups_add, name="groups_add"),
    path("groups/<int:gid>/edit/", groups_views.groups_edit, name="groups_edit"),
    path("groups/<int:gid>/delete/", groups_views.groups_delete, name="groups_delete"),
]
