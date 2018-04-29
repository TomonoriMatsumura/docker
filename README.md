# DockerでSeleniumとownCloudを連携させる 

# Dockerのインストール

```
pip install --upgrade pip
pip install docker
pip install docker-compose
```
# コンテナを立ち上げる

```
git clone https://github.com/TomonoriMatsumura/docker.git
cd /path/to/projeckt/docker/selenium
docker build -t python3:selenium .
docker-compose up -d
cd /path/to/project/docker/owncloud
docker-compose up -d
```

# PythonコンテナでSeleniumをホスト（コンテナ外部）から実行する例

```
docker exec python /bin/bash -c "python /tmp/site.py"
```

# Seleniumで撮影したスナップショットをownCloudへアップロードする

```
curl -X PUT -u USER:PASSWORD "http://{{ owncloud_host }}/remote.php/webdav/{{ dir }}/{{ filename }}" -k --data-binary @{{ filename }}
```

# その他

環境に応じて適宜 dokcer/owncloud/.env ファイルを書き換える
