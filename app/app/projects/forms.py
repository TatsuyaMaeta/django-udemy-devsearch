# formをカスタマイズするためにwidgetsを追加でimport
from django.forms import ModelForm, widgets

from django import forms

from .models import Project, Review


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # fields="__all__"
        # 特定のカラム要素だけ渡すこともできる
        fields = [
            "title",
            "featured_image",
            "description",
            "demo_link",
            "source_link",
            "tags",
        ]

        # これはあんまり良くない
        widgets = {
            "tags": forms.CheckboxSelectMultiple(),
        }

    # ===========================
    # formのパーツにclassを当てる方法
    # ===========================
    # initファイルをoverwriteしてclassを追加する
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        # ループ処理で全ての項目にclassを付与
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})

        # self.fields['title'].widget.attrs.update({"class":"input","placeholder":"Add title"})
        # self.fields['description'].widget.attrs.update({"class":"input"})
        # self.fields['title'].widget.attrs.update({"class":"input","placeholder":"Add title"})


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ["value", "body"]

        labels = {"value": "place your vote", "body": "Add a comment with your bote"}

    # ===========================
    # formのパーツにclassを当てる方法
    # ===========================
    # initファイルをoverwriteしてclassを追加する
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        # ループ処理で全ての項目にclassを付与
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})
