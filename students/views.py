import json

from django.http import HttpResponse, Http404
from django.shortcuts import render

# Create your views here.
def students_main(request):
    return HttpResponse("<h1>Some text in the browser</h1>")


def students_personal(request, sid):
    # breakpoint()
    try:
        sid = int(sid)
    except ValueError:
        raise Http404
    else:
        return HttpResponse("<h1>Some text</h1>" f"<h2><p>{sid}</p><h2>")


def parse_request(request):
    request_info = {
        "method": request.method,
        "path": request.path,
        "GET_params": dict(request.GET),
        "POST_params": dict(request.POST),
        "headers": dict(request.headers),
        "user_agent": request.headers.get("User-Agent"),
        "remote_address": request.META.get("REMOTE_ADDR"),
    }

    response_data = json.dumps(request_info, indent=4)

    response_html = f"<pre>{response_data}</pre>"

    return HttpResponse(response_html)
