
import imp
from django.contrib import admin
from django.urls import path, include
from sosn_main_app.views import index
from django.conf import settings
from django.conf.urls.static import static
from .views import programListView, programDetailView, classroom, passCode



app_name = "program"

urlpatterns = [
    # programs path
    path('', programListView.as_view(), name='all'),
    path("view/<slug:slug>", programDetailView.as_view(), name="program_detail"),
    path("view/<slug:slug>/classroom", classroom , name="program_classroom"),
    path('view/course-passcode-validate/', passCode)
]
