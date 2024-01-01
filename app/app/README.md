app用 readme

project外のtemplateフォルダの設定の仕方
![app外のtemplateの設定](ref-img/projects外のtemplatesフォルダの設定.png)

テンプレートのdocs
https://docs.djangoproject.com/ja/4.2/topics/templates/



queryset object method
link[link](https://docs.djangoproject.com/en/5.0/ref/models/querysets/#queryset-api)
1. ModelName.objects.all()
2. ModelName.objects.get()
3. ModelName.objects.filter()
4. ModelName.objects.exclude()

__(ダブルアンダースコア)はQuerySetメソッドに対してどのカラムに対してどんな要素で情報を取ってくるかを意味している
```
>>> Entry.objects.filter(pub_date__lte="2006-01-01")
```
上記は下記のSQLと同等
```
SELECT * FROM blog_entry WHERE pub_date <= '2006-01-01';
```
「__lte」が詳細なデータのとってき方に相当している
query set チートシート
https://qiita.com/uenosy/items/54136aff0f6373957d22
https://zenn.dev/wtkn25/articles/django-field-lookups

チートシート
https://qiita.com/maisuto/items/bcdb0fd6c63cf0c544d6


フォームのカスタマイズを自由にするには??→'widget_tweaks'
https://hodalog.com/how-to-use-bootstrap-4-forms-with-django/

## テンプレート内での組み込みタグ一覧
projects.html内でのpluralizeから調べた内容
pluralize:valueが1でない場合に複数形を返すタグ
https://qiita.com/nachashin/items/d3f9cd637a9cecbda72c


## 別テーブルをリレーションしてそこからデータを引っ張ってくる方法
section6の Render Profilesでは表示させるProfileに紐づけているSkillをループで表示させている
その時の方法と注意点
1. models.pyで1対多の関係としてProfileと繋ぐ 
2. templateの方ではこんな感じ。.skillがリンクしているテーブル、_setを繋いで.allで全件取得
```html
    {% for skill in profile.skill_set.all %}
    <span class="tag tag--pill tag--main">
        <small>{{skill}}</small>
    </span>
    {% endfor %}
```
インスタンス名.モデル名_set.all()
「Django ForeignKey 逆参照 _set all」
- https://brhk.me/programing/django-foreignkey/
- https://chuna.tech/blog/web-application/Django/reference-foreignkey/
- https://daeudaeu.com/django-relation/


#### userの登録削除などをapp側にキャッチさせたい場合は、signals.pyで切り分けて書いた上で同じappでのapps.pyのclassの中に以下のdefを追記しないと信号をキャッチできない
```python
class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"
    
    # signalをアプリにキャッチさせたいのであればappsのところに書く必要がある
    def ready(self):
        import users.signals
```