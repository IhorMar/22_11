from django.urls import path

# from students.students import views as students_views
from . import views as students_views

urlpatterns = [
    # Students urls
    path("", students_views.students_list, name="home"),
    path("students/add/", students_views.students_add, name="students_add"),
    path(
        "students/<int:sid>/edit/", students_views.students_edit, name="students_edit"
    ),
    path(
        "students/<int:sid>/delete/",
        students_views.students_delete,
        name="students_delete",
    ),
]
