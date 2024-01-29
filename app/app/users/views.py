from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# 検索用
# from django.db.models import Q
from .utils import searchProfiles, paginateProfiles


# デコレーター
from django.contrib.auth.decorators import login_required

from .models import Profile, Message

# 新たに設定し直しているformのclassをこちらにimportして使う
from .forms import CustomUserCreationForm, ProfileForm, SkillForm, MessageForm


# Create your views here.
def loginUser(request):
    page = "login"
    context = {"page": page}
    if request.user.is_authenticated:
        return redirect("profiles")

    if request.method == "POST":
        username = request.POST["username"].lower()
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
            return redirect(request.GET["next"] if "next" in request.GET else 'account')
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
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # データを登録
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "アカウント登録できました")

            login(request, user)
            return redirect("edit-account")

        else:
            messages.success(request, "登録中に問題が発生しました。")

    context = {"page": page, "form": form}
    return render(request, "users/login_register.html", context)


def profiles(request):
    # 関数化してutlsとしてファイルを切り分け
    profiles, search_query = searchProfiles(request)

    custom_range, profiles = paginateProfiles(request, profiles, 3)

    context = {
        "profiles": profiles,
        "search_query": search_query,
        "custom_range": custom_range,
    }
    return render(request, "users/profiles.html", context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    # descriptionがないやつを除外したものをtopskillsに代入している
    topSkills = profile.skill_set.exclude(description__exact="")
    # descriptionがないやつを代入している
    otherSkills = profile.skill_set.filter(description="")
    context = {"profile": profile, "topSkills": topSkills, "otherSkills": otherSkills}
    return render(request, "users/user-profile.html", context)


@login_required(login_url="login")
def userAccount(request):
    profile = request.user.profile

    # contextとして渡すものが何なのかをチェックする
    checkContextKeyAndValues(profile)

    # userProfileから転用
    # descriptionがないやつを除外したものをtopskillsに代入している
    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    context = {"profile": profile, "skills": skills, "projects": projects}

    return render(request, "users/account.html", context)


# プロフ編集ページ
@login_required(login_url="login")
def editAccount(request):
    profile = request.user.profile

    # ここで引数に入れていないと元のデータがinputタグに入らないので注意
    form = ProfileForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect("account")

    context = {"form": form}
    return render(request, "users/profile_form.html", context)


def checkContextKeyAndValues(arg):
    mold = str(type(arg))
    print(f"型: {mold}")

    # models.pyで定義されているclassかどうかを判定(findメソッドを使用)
    check_file_name = "models"
    if mold.find(check_file_name):

        listedArg = vars(arg)
        # print("型:",type(checkMethod1))

        print("classの中身のkeyの一覧はこちら")
        for v in listedArg:
            # print(f"{v}:",getattr(arg1,v))
            key = v
            value = getattr(arg, v)
            print(f"{key}: {value}")

        print("=以上=")
    else:
        print("定義済みのclassではありません")

    """
    参照記事
    classのkeyを取得する方法(vars)
    https://qiita.com/ganyariya/items/e01e0355c78e27c59d41
    https://minus9d.hatenablog.com/entry/2016/11/13/222629
    
    classのvalueを参照する方法(getattr)
    https://stackoverflow.com/questions/64039737/object-is-not-subscriptable-using-django-and-python
    """


@login_required(login_url="login")
def createSkill(request):
    profile = request.user.profile
    form = SkillForm()

    if request.method == "POST":
        form = SkillForm(request.POST)

        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request, "スキルが追加されました")

            return redirect("account")

    context = {"form": form}
    return render(request, "users/skill_form.html", context)


@login_required(login_url="login")
def updateSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)

    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, "スキルが変更されました")

            return redirect("account")

    context = {"form": form}
    return render(request, "users/skill_form.html", context)


def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)

    # 小文字のpostだと機能しないので注意
    if request.method == "POST":
        skill.delete()
        messages.success(request, "スキルが削除されました")
        return redirect("account")

    context = {"object": skill}
    return render(request, "delete_template.html", context)

@login_required(login_url="login")
def inbox(request):
    profile = request.user.profile
    messageRequests = profile.messages.all()
    unreadCount = messageRequests.filter(is_read=False).count()
    
    context={"messageRequests":messageRequests,"unreadCount":unreadCount}
    return render(request,'users/inbox.html',context)

@login_required(login_url="login")
def viewMessage(request,pk):
    profile = request.user.profile
    message= profile.messages.get(id=pk)
    
    if message.is_read == False:
        message.is_read = True
        message.save()
    
    context={"message":message}
    return render(request, 'users/message.html',context)

def createMessage(request,pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()
    
    try:
        sender = request.user.profile
    except Exception as e:
        sender = None
    
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient
            
            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()
            
            messages.success(request, 'your message was successfully sent!')
            return redirect('user-profile',pk=recipient.id)
    
    context={"recipient":recipient,"form":form}
    return render(request,'users/message_form.html',context)