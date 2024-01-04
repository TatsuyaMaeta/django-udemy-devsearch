from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# デコレーター
from django.contrib.auth.decorators import login_required

from .models import Profile
# 新たに設定し直しているformのclassをこちらにimportして使う
from .forms import CustomUserCreationForm


# Create your views here.
def loginUser(request):
    page = "login"
    context = {"page": page}
    if request.user.is_authenticated:
        return redirect("profiles")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
            print("user is exists")
        except Exception as e:
            print("username dont exist")
            messages.error(request, "ユーザーネームがなかったです")

        user = authenticate(request, username=username, password=password)
        print(user)
        print(request.POST)

        # userが存在しなかった場合
        if user is not None:
            login(request, user)
            return redirect("profiles")
        else:
            messages.error(request, "ユーザーネームまたはパスワードが一致しませんでした")
            print("Username OR Password is incorrect")
        # kate / junjun123
    return render(request, "users/login_register.html", context)


def logoutUser(request):
    logout(request)
    messages.info(request, "ユーザーがログアウトしました")
    return redirect("login")


def registerUser(request):
    page = "register"
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # データを登録
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "アカウント登録できました")

            login(request, user)
            return redirect("profiles")
        else:
            messages.success(request, "登録中に問題が発生しました。")

    context = {"page": page, "form": form}
    return render(request, "users/login_register.html", context)


def profiles(request):
    profiles = Profile.objects.all()
    context = {"profiles": profiles}
    return render(request, "users/profiles.html", context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    # descriptionがないやつを除外したものをtopskillsに代入している
    topSkills = profile.skill_set.exclude(description__exact="")
    # descriptionがないやつを代入している
    otherSkills = profile.skill_set.filter(description="")
    context = {"profile": profile, "topSkills": topSkills, "otherSkills": otherSkills}
    return render(request, "users/user-profile.html", context)
