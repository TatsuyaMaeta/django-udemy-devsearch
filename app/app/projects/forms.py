from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # fields="__all__"
        # 特定のカラム要素だけ渡すこともできる
        fields = ["title", "description", "demo_link", "source_link", "tags"]
