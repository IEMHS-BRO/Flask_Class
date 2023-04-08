# 1. RDBMS?

관계형 데이터베이스(Relational Database Management System, RDBMS)의 약자

저번 세션의 MySQL 또한 RDBMS.

데이터베이스는 기본 소양.
모바일 개발자인데 이 정도 개념을 설명이 가능함.

> 기본키 = primary key
> 
> 외래키 = foreign key

## 1) 엑셀을 상상해보자

| id | user_id | user_name | password |
| --- | --- | --- | --- |
| 1 | lucas | heoseongjin | heo1234 |
| 2 | daniel | kimdahun | kim1234 |

위와 같은 형태를 table이라고 합니다.

엑셀과 마찬가지로, RDBMS에서도 table은 이렇게 `행:column`과 `열:row`를 가집니다.

## 2) MySQL을 한 번 사용해보자

1. User 테이블 만들기
    
    
    | id | username |
    | --- | --- |
    | 1 | tester  |
    
    ```sql
    mysql> use flaskclass;
    
    # 테이블 생성
    mysql> create table user(id int(11), username varchar(20));
    
    # 데이터 삽입
    mysql> insert into user values(1, 'tester');
    
    # 데이터 조회
    mysql> select * from user;
    ```
    
2. User 테이블의 id를 이용하여 memo 테이블을 만들어보기
    
    
    | id | user_id | content |
    | --- | --- | --- |
    | 1 | 1 | test |
    
    ```sql
    # 테이블 생성
    mysql> create table memo(id int(11), user_id int(11), content varchar(100));
    
    # 데이터 삽입
    mysql> insert into memo(id, user_id, content) values(1,1,'test');
    
    # 데이터 조회
    mysql> select * from memo;
    ```
    
3. 관계가 있나?
    - 두 개의 테이블을 만들었고, memo.user_id가 user.id 를 의미한다고 생각해보자
    - 하지만 두 테이블은 연관성이 실제론 없고, 그저 다른 테이블
    - 두 테이블에 관계를 맺고, **id 값을 고유화** 해줘야한다.
        - 고유화 왜? 검색이 되어야함

테이블과 테이블을 관계를 맺을 때 사용하는 것이 **외래키**이고, 테이블의 id가 **기본키**에 적합합니다.

이렇게 **테이블과 테이블이 관계를 맺는 것이 RDBMS의 주요 특징**

## 3) 관계성을 가지는 테이블을 만들어보자

1. 기존에 만든 것들 삭제
    
    ```sql
    mysql> drop table user;
    mysql> drop table memo;
    ```
    
2. 기본키를 반영한 User 테이블 만들기
    
    ```sql
    # auto_increment(고유한 id이기 때문에 순차적으로 값을 증가시키겠다), id를 기본키로 지정
    mysql> create table user(id int(11) not null auto_increment, username varchar(20) not null, primary key (id));
    
    # user 테이블의 키 조회
    mysql> show keys from user;
    
    # user 테이블 명세
    mysql> describe user;
    ```
    
    ```sql
    # 데이터 삽입
    mysql> insert into user values(null,'tester');
    ```
    
    - ❌ Primary 키 장애
        - 같은 id(primary key)를 삽입 시도하면?
3. Memo 테이블 기본키 반영 및 User테이블 id와 외래키 관계 맺기
    
    ```sql
    # user_id를 user테이블의 id를 참조한 외래키(관계성 맺어주기)
    mysql> create table memo(id int(11) not null auto_increment, user_id int(11) not null, content varchar(20) not null, primary key(id), foreign key(user_id) references user(id));
    
    # 키 조회
    mysql> show keys from memo;
    
    # 테이블 명세
    mysql> describe memo;
    ```
    
    ```sql
    # 데이터 삽입
    mysql> insert into memo(id, user_id, content) values(null,1,'test');
    ```
    
    - ❌ 관계없는 엉뚱한 데이터 장애
        - 없는 유저의 데이터를 넣는다던지?

### 도식화

<img src="https://user-images.githubusercontent.com/46991314/230728309-5e32679c-7e17-4b95-b4bd-f47b868fbcb2.png" width="200">

- 1:N의 관계(RDBMS의 특징)

## 4) ACID

### Atomicity(원자성)

- 트랜잭션은 실패할 거면 모두 실패하고, 성공하려면 모두 성공해야 합니다. (애매한 상태가 없어야 한다.)

### Consistency(일관성)

- 트랜잭션 완료 이후, 데이터베이스의 데이터는 모두 일관되어야 합니다. (데이터 타입처럼)

### Isolation(격리성)

- 각 트랜잭션은 분리되어있어야 합니다.

### Durability(지속성)

- 트랜잭션이 성공하면, 영구적으로 보존되어야 합니다.

## 5) 공부 필요

- [https://www.w3schools.com/sql/sql_foreignkey.asp](https://www.w3schools.com/sql/sql_foreignkey.asp)
- [https://www.w3schools.com/sql/sql_autoincrement.asp](https://www.w3schools.com/sql/sql_autoincrement.asp)

# 2. 툴 세팅: Flask SQLAlchemy, Flask Migrate

- Flask Migrate를 설치하면 Flask SQLAlchemy도 함께 설치됨

## 1) ORM

ORM은 Object Relational Mapping 즉, 객체-관계 매핑의 줄임말이며,

객체 관계 매핑은 데이터베이스와 객체 지향 프로그래밍 언어 간 호환되지 않는 데이터를 변환하는 프로그래밍 기법

<img src="https://user-images.githubusercontent.com/46991314/230728335-7dfab32d-e525-4150-a7b3-ee55f5bf5c35.png" width="200">

## 2) 참고 URL

- [https://flask-sqlalchemy.palletsprojects.com/en/2.x/](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)
- [https://flask-migrate.readthedocs.io/en/latest/](https://flask-migrate.readthedocs.io/en/latest/)

## 3) 세팅하기

- testdb 컨테이너 재생성하고 시작하기
    - 불필요하게 설정된 테이블들 다 제거하고 새롭게 깨끗하게 시작

```bash
$ pip install flask-migrate
# SQLAlchemy도 같이 설치됨
```

```bash
$ pip install pymysql
# MySQL 쓰려면 필요함(없으면 에러)
```

**라이브러리 저장**

- `pip freeze > requirements.txt`
    - `pip install -r requirements.txt`

## 4) 코드를 쳐보자

1. 초기 구축
    
    ```python
    from flask import Flask
    from flask_sqlalchemy import SQLAlchemy
    from flask_migrate import Migrate
    
    app = Flask(__name__)
    
    db = SQLAlchemy()
    migrate = Migrate()
    
    # 3306이면 따로 포트 명시 안해도 됨.
    hostname = "localhost:3307"
    username = "root"
    password = "password"
    db_name = "flaskclass"
    uri = "mysql://"+username+":"+password+"@"+hostname+"/"+db_name+"?charset=utf8"
    app.config['SQLALCHEMY_DATABASE_URI'] = uri
    
    # DB INIT
    db.init_app(app)
    migrate.init_app(app, db)
    
    if __name__ == "__main__":
        app.run()
    ```
    
2. 실행하기
    
    ```bash
    $ flask run
    ```
    
    - 에러남(`ModuleNotFoundError: No module named ‘MySQLdb’`)
    - pymysql 사용하자
        - before `uri = "mysql://"+username+":"+password+"@"+hostname+"/"+db_name+"?charset=utf8”`
        - after `uri = "mysql+pymysql://"+username+":"+password+"@"+hostname+"/"+db_name+"?charset=utf8”`

## 5) DB 커맨드

- `flask db`
    - flask run으로 db가 열려야 가능함
    - `flask --help`해보면 없었는데 나옴
    - `flask db --help`해보면 여러가지가 나옴
- `flask db init`
    - 마이그레이션 폴더가 생성됨
- `flask db current`
    - 현재 DB형상은 어딘지 알려줍니다.
- `flask db migrate -m "Init database"`
    - 지금 마이그레이션 기록을 시작하는 초기 기반이 되었다고 선언.
- `flask db upgrade`
    - 바뀐 건 없지만, 바뀐 게 있으면 호출
    - 수정사항이 반영됨

## 6) DB 확인

- mysql 들어가봅시다
- 우리가 생성하지 않았는데 alembic_version 테이블이 생김
    - 이게 Flask에서 생성해준 거임. 기본 설정은 완료한거임.    

# 3. DB User 모델 생성

- 써봐야 아는 법!
- 바로 코드로 짜봅시다
    
    <img src="https://user-images.githubusercontent.com/46991314/230728392-be6dc319-3759-4b6d-875e-2ef0c3e8ae4c.png" width="200">
    

## 1) 구현

이제 이 클래스는 SQL에서 테이블이 됩니다.(테이블명은 User)

```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(20), unique=True, nullable=False)
    user_name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)
```

1. Migrations에 지금 폴더 아무것도 없음
2. `flask db migrate -m "Add User Model"`
    - 우리가 커밋한 걸 기반으로 파이썬 파일 생김
        ![image](https://user-images.githubusercontent.com/46991314/230728416-8a8e3f6e-4939-42be-8cdb-e041ddc9d7aa.png)

        
    - 파일 보기
3. docker mysql 들어가보자
    - 테이블 아무것도 없음
    - 터미널 하나 더 띄워서 docker용 flask용으로 나누자
4. `flask db upgrade`
    - running upgrade가 되었다
    - show tables하면 생김
    - migrate는 이런 메세지를 작성하고 형상을 관리하는 버전 파일 생성
    - upgrade는 이 버전 파일을 기반으로 데이터베이스에 적용해줌
5. `describe user`
    - 우리가 생성한 것 그대로 반영이 됨

# 4. Flask SQLAlchemy 기초 쿼리

## 1) 참고 URL

- [https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/](https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/)

## 2) Flask Shell 써보기

- Flask Shell 들어가기
    
    ```bash
    $ flask shell
    ```
    
- db 객체 가져오기
    
    ```bash
    >>> from app import db
    ```
    
- DB 세션 가져와서 여러가지 쿼리 사용해보기
    
    ```bash
    # 데이터 추가하기
    >>> db.session.add(User(user_id='lucasheo', user_name='lucas', password='test1234'))
    >>> db.session.commit()
    
    # 데이터 조회하기
    >>> User.query.all()
    [<User 1>]
    >>> User.query.all()[0].user_id
    'lucasheo'
    
    # 데이터 조회하기(필터링)
    >>> User.query.filter_by(user_name='lucas').first()
    <User 1>
    >>> User.query.filter_by(user_name='lucas').first().user_name
    'lucas'
    
    # Primary Key로 검색
    >>> User.query.get(1).user_name
    'lucas'
    
    # 데이터 삭제
    >>> user = User.query.get(1)
    >>> db.session.delete(user)
    >>> db.session.commit()
    ```
    
- 다 공식문서에 있다
    - order by
    - limit
    - 기타 등등

- sql 쿼리를 잘 몰라도, 파이썬으로 원하는 정보에 접근이 가능해짐
    - ORM의 힘
    - 직접 써보니까 좋지 않은가?

# 5. 리팩토링: 조회수 시스템

```python
'''
리팩토링: 조회수 시스템을 만들어보자

/hits/<id> 페이지의 조회수를 저장하고 json으로 반환하는 시스템
'''
from flask import jsonify

class Hit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    views = db.Column(db.Integer, default=0)

@app.route("/hits/<int:id>")
def hits(id):
    hit = Hit.query.get(id)
    if hit is None:
        hit = Hit(id=id)
        db.session.add(hit)
        db.session.commit()
    hit.views += 1
    db.session.commit()
    return jsonify(
        id=hit.id,
        views=hit.views
    )
```

- migrate 기록
- upgrade
