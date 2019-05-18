from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:form_id>", views.show_form, name="show_form"),
    path("save_result/<str:form_id>", views.save_result, name="save_result"),
    path("show_result/<str:form_id>", views.show_result, name="show_result"),
    path("create_form", views.create_form, name="create_form"),
]
