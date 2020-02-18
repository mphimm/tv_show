from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("all_shows/",views.all_shows),
    path("create_show", views.create_show),
    path("info_page/<int:id>", views.viewInfoPage),
    path("edit/<int:id>", views.edit),
    path("all_shows/<int:id>/destroy", views.deleteShow),
    path("info_page/<int:id>/", views.viewInfoPage),
    path("info_page/<int:id>/destroy", views.viewInfoPage),
    path("edit_process/<int:id>", views.edit_process),
]
