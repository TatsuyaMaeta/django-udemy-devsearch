1. venvを作成する
   1. ```python -m venv venv```
2. venv環境に入る
   1. ``` source venv/bin/activate ```
3. pip update
   1. ``` pip install --upgrade pip ```
4. 以下のライブラリをインストール
   1. Django
   2. app
   3. python-decouple
5. project作成
   1. ``` django-admin startproject config .``` 
6. アプリケーション作成
   1. ``` django-admin startapp <APP_NAME> .```

1. dockerを起動
   1. docker compose up --build




========
https://www.youtube.com/watch?v=Gkpdg6zBC90

LAST
https://www.youtube.com/watch?v=P5Tkhvx1NoM&t=3s

admin
admin@admin.com
admin123


gunicorn main_app.wsgi:application --bind 0.0.0.0:8000
※staticファイルが見つけられない

docker build  -t myimage .

 myimageというdocker imageを用いてport8000で起動
docker run -p 8000:8000 myimage

gunicornでstaticファイルが読み込めないときはこれ
https://zenn.dev/ktnyt/scraps/e01c9dd89fb7a7


container, image全てを無に返すコマンド
docker system  prune -a --volumes


postgresに関するライブラリの設定
requirements.txtに
https://qiita.com/b2bmakers/items/d1b0db5966ac145b0e29



起動コマンド
docker-compose up --build

コンテナ、イメージ全て削除
docker system  prune -a --volumes

python my_app/manage.py collectstatic

## whitenoise とは
nginxなどのwebサーバ無しに、静的ファイルを提供できるライブラリ
使用の際のコマンド
```
pip install whitenoise
```
https://pypi.org/project/whitenoise/