from django.http import HttpResponse
from django.shortcuts import render


# Students views
def students_list(request):
    # students_1 = Students.objects.all()
    students = (
        {
            "id": 1,
            "first_name": "Дмитро",
            "last_name": "Волошко",
            "ticket": 235,
            "image": "/media/img/image_1.jpeg",
        },
        {
            "id": 2,
            "first_name": "Ігор",
            "last_name": "Шевченко",
            "ticket": 2123,
            "image": "/media/img/image_2.jpg",
        },
        {
            "id": 3,
            "first_name": " Михайло",
            "last_name": "Петренко",
            "ticket": 565,
            "image": "/media/img/image_3.jpeg",
        },
        {
            "id": 4,
            "first_name": " Петро",
            "last_name": "Ворон",
            "ticket": 13,
            "image": "/media/img/image_4.png",
        },
    )
    return render(request, "students/student_list.html", {"students": students})


def students_add(request):
    # breakpoint()
    return HttpResponse("<h1>Student Add Form</h1>")


def students_edit(request, sid):
    return HttpResponse("<h1>Edit Student %s</h1>" % sid)


def students_delete(request, sid):
    return HttpResponse("<h1>Delete Student %s</h1>" % sid)
