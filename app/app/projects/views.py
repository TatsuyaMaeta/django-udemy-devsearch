from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Project, Tag
from .forms import ProjectForm

# デコレーター
from django.contrib.auth.decorators import login_required

from django.db.models import Q

from .utils import searchProjects, paginateProjects


# projectList = [
#     {"id": 1, "title": "hoge", "description": "hogehoge"},
#     {"id": 2, "title": "fuga", "description": "fugafuga"},
#     {"id": 3, "title": "bar", "description": "barbar"},
# ]


def projects(request):
    # msg = "Projects"
    # number = 100
    # context = {"msg": msg, "num": number, "projects": projectList}

    projects, search_query = searchProjects(request)

    custom_range, projects = paginateProjects(request, projects, 6)

    context = {
        "projects": projects,
        "search_query": search_query,
        "custom_range": custom_range,
    }
    return render(request, "projects/projects.html", context)


def project(request, pk):
    # projectObj = None
    # for i in projectList:
    #     if i["id"] == int(pk):
    #         projectObj = i
    projectObj = Project.objects.get(id=pk)
    # 上記のprojectObjに含まれているtagsのカラムの要素を全て取得している
    tags = projectObj.tags.all()

    return render(
        request, "projects/single-project.html", {"project": projectObj, "tags": tags}
    )


@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile

    # forms.pyからclassを引っ張ってくる
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            # ここでのredirect先の指定はurls.pyのurlpatternのnameを指定している
            return redirect("projects")

    context = {"form": form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")
def updateProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        # mediaファイルを追加できるように変更したのでupdateにもfileについて追加する
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            # ここでのredirect先の指定はurls.pyのurlpatternのnameを指定している
            return redirect("account")

    context = {"form": form}
    return render(request, "projects/project_form.html", context)


@login_required(login_url="login")
def deleteProject(request, pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method == "POST":
        project.delete()
        return redirect("projects")

    context = {"object": project}
    return render(request, "delete_template.html", context)
