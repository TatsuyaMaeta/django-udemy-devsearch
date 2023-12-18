from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

# projectList = [
#     {"id": 1, "title": "hoge", "description": "hogehoge"},
#     {"id": 2, "title": "fuga", "description": "fugafuga"},
#     {"id": 3, "title": "bar", "description": "barbar"},
# ]


def projects(request):
    # msg = "Projects"
    # number = 100
    # context = {"msg": msg, "num": number, "projects": projectList}
    project = Project.objects.all()
    context = {"projects": project}
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


def createProject(request):
    # forms.pyからclassを引っ張ってくる
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            # ここでのredirect先の指定はurls.pyのurlpatternのnameを指定している
            return redirect("projects")

    context = {"form": form}
    return render(request, "projects/project_form.html", context)


def updateProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            # ここでのredirect先の指定はurls.pyのurlpatternのnameを指定している
            return redirect("projects")

    context = {"form": form}
    return render(request, "projects/project_form.html", context)


def deleteProject(request, pk):
    project = Project.objects.get(id=pk)

    if request.method == "POST":
        project.delete()
        return redirect("projects")

    context = {"object": project}
    return render(request, "projects/delete_template.html", context)
