from django.db import models
import uuid
from users.models import Profile

# Create your models here.
class Project(models.Model):
    # ForeignKey:別のテーブルの情報を持ってきますよ
    # この場合、Profile tableから情報持ってきていて、Profile Classはデフォルトだとnameを戻す設定になっている
    # テンプレートでは詳細のテーブル名を指定したらそのテーブル名で情報を取得できる
    owner = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.SET_NULL)

    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    # あとからこれを追加。画像を扱うならpillowが必要なのでinstallすること
    # 新しくmodelを追加した時点でDBと整合性が取れなくなるのでmakemigration -> migrateすること
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField("Tag", blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["created"]
        # これで降順になる
        # ordering =["-created"]
    
    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        


class Review(models.Model):
    VOTE_TYPE = (("up", "up vote"), ("down", "down vote"))

    owner = models.ForeignKey(Profile,on_delete=models.CASCADE, null=True)
    # 関連付けたい外部キーを設定する場合は第一引数にそのclass名を入れる
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    
    
    class Meta:
        unique_together = [["owner","project"]]

    def __str__(self) -> str:
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self) -> str:
        return self.name
