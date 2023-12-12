from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("projects.urls"))
    # path("home/", getHomePage),
    # path("projects/", projects, name="projects"),
    # path("project/<str:pk>/", project, name="project"),
]
