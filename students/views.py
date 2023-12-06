from django.http import HttpResponse
from django.shortcuts import render


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


def demonstration_page(request):
    return render(request, "students/demonstration.html", {})


# Students views
def students_list(request):
    return render(request, "students/index.html", {})


def students_add(request):
    # breakpoint()
    return HttpResponse("<h1>Student Add Form</h1>")


def students_edit(request, sid):
    return HttpResponse("<h1>Edit Student %s</h1>" % sid)


def students_delete(request, sid):
    return HttpResponse("<h1>Delete Student %s</h1>" % sid)
