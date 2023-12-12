from django.shortcuts import render
from django.http import HttpResponse

projectList = [
    {"id": 1, "title": "hoge", "description": "hogehoge"},
    {"id": 2, "title": "fuga", "description": "fugafuga"},
    {"id": 3, "title": "bar", "description": "barbar"},
]


def projects(request):
    msg = "Projects"
    number = 100
    context = {"msg": msg, "num": number, "projects": projectList}
    return render(request, "projects/projects.html", context)


def project(request, pk):
    projectObj = None
    for i in projectList:
        if i["id"] == int(pk):
            projectObj = i

    return render(request, "projects/single-project.html", {"project": projectObj})
