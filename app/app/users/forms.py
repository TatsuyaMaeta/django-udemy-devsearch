from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# プロフ編集用
from .models import Profile, Skill, Message


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "email", "username", "password1", "password2"]
        labels = {
            "first_name": "Name",
        }

        # ===========================

    # formのパーツにclassを当てる方法
    # ===========================
    # initファイルをoverwriteしてclassを追加する
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        # ループ処理で全ての項目にclassを付与
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile

        # これだと都合が悪いので欲しい情報だけに絞る
        # fields="__all__"

        fields = [
            "name",
            "email",
            "username",
            "location",
            "bio",
            "short_intro",
            "profile_image",
            "social_github",
            "social_linkedin",
            "social_twitter",
            "social_youtube",
            "social_website",
        ]

    # formのパーツにclassを当てる方法
    # ===========================
    # initファイルをoverwriteしてclassを追加する
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        # ループ処理で全ての項目にclassを付与
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = "__all__"
        exclude = ["owner"]

    # formのパーツにclassを当てる方法
    # ===========================
    # initファイルをoverwriteしてclassを追加する
    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        # ループ処理で全ての項目にclassを付与
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ["name","email","subject","body"]


    # formのパーツにclassを当てる方法
    # ===========================
    # initファイルをoverwriteしてclassを追加する
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        # ループ処理で全ての項目にclassを付与
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})
