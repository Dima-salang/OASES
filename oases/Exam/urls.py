from django.urls import path

from . import views

urlpatterns = [
    path("upload/", views.upload_exam, name="upload_exam"),
    
]