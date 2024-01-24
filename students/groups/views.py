from django.http import HttpResponse
from django.shortcuts import render

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
