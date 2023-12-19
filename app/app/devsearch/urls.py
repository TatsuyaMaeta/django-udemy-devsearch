from django.contrib import admin
from django.urls import path, include

# image用の設定
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("projects/", include("projects.urls")),
    # path("home/", getHomePage),
    # path("projects/", projects, name="projects"),
    # path("project/<str:pk>/", project, name="project"),
    # デフォルトのページの設定を変更
    path("", include("users.urls")),
]

# media root設定を追加
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
