# 이미지 만들기
docker build . --tag adoc_api_server:1.0
# 실행
docker run --name adoc_api_server -d -p 8080:8080  adoc_api_server:1.0

docker run --name adoc_api_server -d -p 8080:8080  adoc_api_server:1.0 

docker rm -f adoc_api_server; docker run --name adoc_api_server -d -p 8080:8080  adoc_api_server:1.0


# run localsetting
python3 manage.py runserver --settings=kakao_demo.settings.local_settings
## local migration
python3 manage.py migrate --settings=kakao_demo.settings.local_settings
