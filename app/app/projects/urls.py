from django.urls import path
from . import views


urlpatterns = [
    # urlに何もくっついてない時にはviews.projectsのdefを見にいけよな
    path("", views.projects, name="projects"),
    path("project/<str:pk>/", views.project, name="project"),
]
