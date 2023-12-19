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