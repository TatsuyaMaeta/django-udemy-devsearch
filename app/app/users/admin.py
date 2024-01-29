from django.contrib import admin

# Register your models here.
from .models import Profile, Skill, Message

# これがないとadminパネルに設定の反映ができないので注意
admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Message)

