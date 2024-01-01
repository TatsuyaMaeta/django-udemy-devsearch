from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User
from .models import Profile


# デコレータ
# @receiver(post_save, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    print("Profile signal triggered")
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user, username=user.username, email=user.email, name=user.first_name
        )
        print("done")
    # print("profile Saved!!!!!!")
    # print("instance:", instance)
    # print("create:", created)
    # print("")


def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete
    print("deleting")


post_save.connect(createProfile, sender=User)
post_delete.connect(deleteUser, sender=Profile)
