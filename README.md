# 프로젝트 소개

### [기획서 링크](https://kdt-gitlab.elice.io/Jungin/mini-project2/-/wikis/%EA%B8%B0%ED%9A%8D%EC%84%9C)
 
### 개발 환경
1. 선작업으로 mysql 설치 필요합니다.  
  - 1-1. Ubuntu의 경우 추가작업이 필요합니다 ([참고링크](https://github.com/PyMySQL/mysqlclient#prerequisites))
    + 1-1-1. 명령어 : sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
2. 패키지 설치하기 : pip3 install -r requirement.txt
3. mysql 데이터베이스 경로 설정하기 : app.py 파일의 "SQLALCHEMY_DATABASE_URI"를 "mysql://[*유저이름*]:[*비밀번호*]@[*서버주소*]/[*데이터베이스이름*]" 로 설정해주세요.

