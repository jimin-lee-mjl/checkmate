# 프로젝트 소개

### [기획서 링크](https://kdt-gitlab.elice.io/Jungin/mini-project2/-/wikis/%EA%B8%B0%ED%9A%8D%EC%84%9C)
 
### 개발 환경
1. 선작업으로 mysql 설치 필요합니다.  
  - 1-1. Ubuntu의 경우 추가작업이 필요합니다 ([참고링크](https://github.com/PyMySQL/mysqlclient#prerequisites))
    + 1-1-1. 명령어 : sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
2. 패키지 설치하기 : pip3 install -r requirement.txt
3. mysql 데이터베이스 경로 설정하기 
  - 3-1. config.py 파일을 만들어주세요.
  - 3-2. config.py 파일 안에 아래 코드를 복사하여 DB_CONNECT를 만들어주세요.
  ```
  DB_CONNECT = {
    'username' : '유저 이름',
    'password' : '비밀번호',
    'dbname' : '데이터베이스 이름',
    'server' : '127.0.0.1'
  }
  ```
  - 3-3. '유저 이름', '비밀번호', '데이터베이스 이름'을 채워넣어 주세요. (이 파일은 git이 추적하지 않습니다.)


