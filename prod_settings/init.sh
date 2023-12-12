# パッケージ管理ツールの最新版への更新
sudo yum update -y

# gitのinstall
sudo yum install git -y

# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑
# ここまでを手作業で実行。git clone後に init.shにて環境構築実行

# echo "git cloneは自分で実行してください"

# dockerのインストール
sudo yum install docker -y

# dockerの起動
sudo service  docker start

# ec2にdockerの権限を割り当て
sudo usermod -a -G docker ec2-user

# docker-composeのダウンロード
# https://gist.github.com/npearce/6f3c7826c7499587f00957fee62f8ee9
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose

# 実行権限の委譲
sudo chmod +x /usr/local/bin/docker-compose

# gitが無事入っているかを確認
git --version

# docker-composeが無事入っているかを確認
docker-compose version

# nano .env
# 保存・終了後は ctrl + X
# ↓
# yes
# ↓
# [Enter]

# sudo docker-compose up --build
# docker system  prune -a --volumes



# python3 -m venv venv
# /home/ec2-user/venv/bin/python3 -m pip install --upgrade pip


# python3 manage.py makemigrations
# python3 manage.py migrate
# python3 manage.py createsuperuser 


# postgresql側(DB側)のセキュリティグループのインバウンドルールにEC2のプライベート IPv4 アドレスをくっつける。
# それをソースに追加指定して保存