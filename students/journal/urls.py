from django.contrib import admin
from django.urls import path

from . import views as journal_views


urlpatterns = [
    # Journals url
    path("", journal_views.journal_list, name="journal"),
]
