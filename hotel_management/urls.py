from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create_record/", views.create_record_view, name="create_record"),
]