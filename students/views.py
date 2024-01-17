from django.http import HttpResponse
from django.shortcuts import render

from students_2911.differ_data.differ_variables import students_list_data


# from django.shortcuts import render


# Create your views here.
# def students_main(request):
#     return HttpResponse(
#         "<h1>Some text in the browser</h1><p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum tortor quam, feugiat vitae, ultricies eget, tempor sit amet, ante. Donec eu libero sit amet quam egestas semper. Aenean ultricies mi vitae est. Mauris placerat eleifend leo. Quisque sit amet est et sapien ullamcorper pharetra. Vestibulum erat wisi, condimentum sed, commodo vitae, ornare sit amet, wisi. Aenean fermentum, elit eget tincidunt condimentum, eros ipsum rutrum orci, sagittis tempus lacus enim ac dui. Donec non enim in turpis pulvinar facilisis. Ut felis. Praesent dapibus, neque id cursus faucibus, tortor neque egestas augue, eu vulputate magna eros eu erat. Aliquam erat volutpat. Nam dui mi, tincidunt quis, accumsan porttitor, facilisis luctus, metus</p>")


# def students_personal(request, sid):
#     breakpoint()
#     try:
#         sid = int(sid)
#     except ValueError:
#         raise Http404
#     else:
#         return HttpResponse("<h1>Some text</h1>" f"<h2><p>{sid}</p><h2>")


# def parse_request(request):
#     request_info = {
#         "method": request.method,
#         "path": request.path,
#         "GET_params": dict(request.GET),
#         "POST_params": dict(request.POST),
#         "headers": dict(request.headers),
#         "user_agent": request.headers.get("User-Agent"),
#         "remote_address": request.META.get("REMOTE_ADDR"),
#     }
#
#     response_data = json.dumps(request_info, indent=4)
#
#     response_html = f"<pre>{response_data}</pre>"
#
#     return HttpResponse(response_html)


# def main_page(request):
#     template = loader.get_template('students/index.html')
#     context = {}
#     return HttpResponse(template.render(context))

# def base(request):
#     students=()
#     render(request, "students/base.html", {"students":students})
# def demonstration_page(request):
#     students = (
#         {
#             "id": 1,
#             "first_name": "Дмитро",
#             "last_name": "Волошко",
#             "ticket": 235,
#             "image": "img/image_1.jpeg",
#         },
#         {
#             "id": 2,
#             "first_name": "Ігор",
#             "last_name": "Шевченко",
#             "ticket": 2123,
#             "image": "/img/image_2.jpg",
#         },
#     )
#
#     # breakpoint()
#     return render(request, "students/demonstration.html", {"students": students})


# Students views
def students_list(request):
    # students_1 = Students.objects.all()
    students = (
        {
            "id": 1,
            "first_name": "Дмитро",
            "last_name": "Волошко",
            "ticket": 235,
            "image": "img/image_1.jpeg",
        },
        {
            "id": 2,
            "first_name": "Ігор",
            "last_name": "Шевченко",
            "ticket": 2123,
            "image": "img/image_2.jpg",
        },
        {
            "id": 3,
            "first_name": " Михайло",
            "last_name": "Петренко",
            "ticket": 565,
            "image": "img/image_3.jpeg",
        },
        {
            "id": 4,
            "first_name": " Стів",
            "last_name": "Возняк",
            "ticket": 13,
            "image": "img/image_4.png",
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


# Group views


def groups_list(request):  # GET
    groups = (
        {
            "id": 1,
            "group_name": "Група_1_test",
            "leader_group_first_name": "Волошко",
            "leader_group_last_name": "Петро",
        },
        {
            "id": 2,
            "group_name": "Група_2_test",
            "leader_group_first_name": "Івашко",
            "leader_group_last_name": "Володимир",
        },
    )
    return render(request, "students/groups_list.html", {"groups": groups})


def groups_add(request):  # POST
    return render(request, "students/groups_list.html", {})


def groups_edit(request, gid):  # PATCH
    return HttpResponse("<h1>Groups Edit %s</h1>" % gid)


def groups_delete(request, gid):  # DELETE
    return HttpResponse("<h1>Groups Delete %s</h1>" % gid)


# Journal
def journal_list(request):
    return HttpResponse("<h1>Journal list TEST for student -- </h1>")
