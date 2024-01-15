from .models import Skill, Profile
from django.db.models import Q

# ページネーション用
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def paginateProfiles(request, profiles, results):

    page = request.GET.get("page")

    paginator = Paginator(profiles, results)

    try:
        profiles = paginator.page(page)

    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(1)
    except EmptyPage:
        page = paginator.num_pages
        # print("page: ",page)
        profiles = paginator.page(page)

    leftIndex = int(page) - 4

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = int(page) + 4

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages

    custom_range = range(leftIndex, rightIndex + 1)

    return custom_range, profiles


def searchProfiles(request):
    search_query = ""

    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")

    # Skillモデルをimportしてskillの名前を小文字で平してから検索
    skills = Skill.objects.filter(name__icontains=search_query)

    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query)
        | Q(short_intro__icontains=search_query)
        |
        # この検索先は別のテーブルを見ているから、Skill.objects.filterを実施している
        Q(skill__in=skills)
    )

    return profiles, search_query
