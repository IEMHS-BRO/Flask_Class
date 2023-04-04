<!-- TOC start -->
- [1. 데이터베이스 입문하기](#1-데이터베이스-입문하기)
  * 1-1. 관계형 데이터베이스란 무엇인가요?
  * 1-2. SQL이란 무엇인가요?
  * 1-3. ORM이란 무엇인가요?
- [2. 데이터베이스 로컬 개발환경 구축 : MySQL with Docker](#2-데이터베이스-로컬-개발환경-구축--mysql-with-docker)
  * [2-1. Docker 설치](#2-1-docker-설치)
    + 설치 성공 판단
  * [2-2. Docker로 MySQL 세팅](#2-2-docker로-mysql-세팅)
    + 1) 시작하기 : 프로세스 보기
    + 2) 일단 MySQL 5.7로 런해보기
    + 3) 패스워드 설정과 함께  MySQL 5.7 런해보기
    + 4) 러닝되고 있는 MySQL 컨테이너 포트 확인
    + 5) 3306포트 열어버리기
    + 6) 데이터베이스로 바로 진입하기
    + 7) 데이터베이스 생성하기
    + 8) MySQL에서 한국어 사용할 수 있도록 설정하기
    + 9) 컨테이너 생성할 때부터 데이터베이스도 함께 생성하기
  * [2-3. Docker가 뭐임? 왜 Docker?](#2-3-docker가-뭐임-왜-docker)
    + 도커 컨테이너
    + **도커 컨테이너와 Virtual Machine**
    + 도커 이미지
    + 왜 쓰는지 정리해보기(요약)
<!-- TOC end -->

# 1. 데이터베이스 입문하기

데이터베이스(Database)는 데이터를 저장하고 관리하는 시스템입니다. 일반적으로 디스크나 메모리에 저장된 데이터의 집합을 의미합니다.

## 1-1. 관계형 데이터베이스란 무엇인가요?

관계형 데이터베이스(Relational Database)는 데이터를 테이블 형태로 구성하고, 이 테이블들 간의 관계를 정의하며, SQL(Structured Query Language)을 이용해 데이터를 관리하는 데이터베이스입니다.

## 1-2. SQL이란 무엇인가요?

SQL(Structured Query Language)은 관계형 데이터베이스에서 데이터를 조작하고 관리하기 위한 언어입니다. 데이터베이스에 저장된 데이터를 CRUD(Create, Read, Update, Delete)의 형태로 조작할 수 있습니다.

## 1-3. ORM이란 무엇인가요?

ORM(Object-Relational Mapping)은 객체와 관계형 데이터베이스 간의 매핑을 지원하는 도구입니다. 객체지향 프로그래밍에서 사용되는 객체와 관계형 데이터베이스의 테이블을 연결시켜 객체를 데이터베이스에 저장, 검색, 수정, 삭제할 수 있도록 해줍니다.

Flask에서 SQLAlchemy라는 라이브러리를 이용하여 사용할 수 있습니다.

# 2. 데이터베이스 로컬 개발환경 구축 : MySQL with Docker

## 2-1. Docker 설치

- [Install Docker Desktop on Windows](https://docs.docker.com/desktop/install/windows-install/)
- [Install Docker Desktop on Mac](https://docs.docker.com/desktop/install/mac-install/)

### 설치 성공 판단

terminal에서 `docker`를 쳤을 때 무엇인가 나오면 됨(**Mac 기준**)

![image](https://user-images.githubusercontent.com/46991314/229362878-d0cfcd1f-7efb-4c9b-908b-6911be502096.png)


## 2-2. Docker로 MySQL 세팅

### 1) 시작하기 : 프로세스 보기

```bash
$ docker ps
# (도커 프로세스) 도커로 띄운 컨테이너가 뜸 (러닝되고 있는 친구들만)
```

```bash
$ docker ps -a
# docker ps와 동일하지만, 스탑되어있는 친구들도 나옴
```

> Apple Silicon Mac은 `—platform linux/amd64`를 옵션으로 한 번 사용하여야 5.7이 깔림
> 
> 
> [[오류 천국 : Docker편] (Mac M1) no matching manifest for linux/arm64/v8 in the manifest list entries](https://velog.io/@sujeongim/오류-천국-Docker편-Mac-M1-no-matching-manifest-for-linuxarm64v8)
> 

### 2) 일단 MySQL 5.7로 런해보기

```bash
$ docker run --rm —-name testdb mysql:5.7
# 도커 허브에 있는 mysql 이미지 기반으로 띄워지게됨
```

`**—rm`(리무브)는 스탑을 시켰을 때 이 컨테이너를 스탑이 되는 상태로 두지 말고 없애버리라는 의미**

`**—rm` 없는 상태로 한 번 해볼까요?**

```bash
$ docker run —-name testdb mysql:5.7
```

- 에러가 뜸
- `docker ps`에는 컨테이너 안 뜸(실행이 안되었으니)
- `docker ps -a`하면 컨테이너 뜸(종료 되었다!)
- `docker rm testdb`하면 없어집니다.

**`—rm` 있는 상태로 실행해보자**

```bash
$ docker run **--rm** --name testdb mysql:5.7
```

- 둘 다 안뜹니다!(`ps`, `ps -a`)
- `docker rm testdb`를 할 필요도 없음(사라졌기 때문에)
- 패스워드를 설정하라고 에러가 나옵니다.

### 3) 패스워드 설정과 함께  MySQL 5.7 런해보기

```bash
$ docker run --rm -d --name testdb -e MYSQL_ROOT_PASSWORD=password mysql:5.7
```

- 비밀번호를 설정합니다 (-e 환경 옵션 추가)
- **-d 데몬 형식으로 해라! 라는 옵션도 추가됨**

**`-d` 없이 해볼까요? (역시 보여주는게 빠름)**

```bash
$ docker run --rm --name testdb -e MYSQL_ROOT_PASSWORD=password mysql:5.7
```

- 나갈 수가 없습니다. (Ctrl+C해도)
    - 터미널 또 열어서 `docker stop testdb`
- 컨테이너가 띄워져있기는 하나, 우리가 떨어질 수가 없음(프로세스)
- 백그라운드 형식으로 돌아가게 해야함

**`-d` 있는 상태로 해볼까요?**

```bash
$ docker run --rm -d --name testdb -e MYSQL_ROOT_PASSWORD=password mysql:5.7
```

- 깔끔하다 (뭐 따로 뜨지도 않음)
- `docker ps`로도 확인 가능(떠 있으니까)

**진입하기**

```bash
$ docker exec -it testdb bash
```

- `-it`터미널 환경을 쓸 수 있게끔 도와주는 옵션값
- bash로 붙을 거야
- MySQL 서버 가상환경에 들어가짐!! 격리된 환경에 접속을 했다

**MySQL 사용하기**

```bash
$ mysql -u root -p
# Enter password: [패스워드입력]
# MySQL 시작

mysql> show databases;
# 뭐 없죠?
```

**나가기**

- exit(mysql 나가기)
- exit(bash 나가기)

### 4) 러닝되고 있는 MySQL 컨테이너 포트 확인

```bash
CONTAINER ID   IMAGE       COMMAND                  CREATED          STATUS          PORTS                 NAMES
452098268ad8   mysql:5.7   "docker-entrypoint.s…"   12 minutes ago   Up 12 minutes   3306/tcp, 33060/tcp   testdb
```

- 우리가 사용하려면, 컨테이너 기준 외부로 오픈을 해야합니다.

### 5) 3306포트 열어버리기

```bash
$ docker run --rm -d --name testdb -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password mysql:5.7
```

- `-p 3306:3306` 3306번 포트를 여는 옵션
    - `-p 3307:3306` 컨테이너 3306 → 로컬 3307번 포트를 여는 옵션

**(3306이었는데,,, 현재 로컬에 있는 MySQL과 겹쳐서,,, 3307으로 바꿉니다)**

**연결 확인**

- `ps -a`로 확인
- 아까와는 다르게 외부 포트로 연결이 됨

```bash
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                  PORTS                               NAMES
c2346a7e9cc6        mysql:5.7           "docker-entrypoint.s…"   1 second ago        Up Less than a second   0.0.0.0:3306->3306/tcp, 33060/tcp   testdb
```

### 6) 데이터베이스로 바로 진입하기

원래는 컨테이너 진입 후, mysql에 또 진입해야함

```bash
$ docker exec -it testdb bash
$ mysql -u root -p
```

mysql로 바로 진입하는 방법

```bash
$ docker exec -it testdb mysql -u root -p
# Enter password: [패스워드입력]
# MySQL 시작
```

- 바로 패스워드 입력하고 시작됨

### 7) 데이터베이스 생성하기

```bash
mysql> create database flaskclass;
# flaskclass라는 데이터베이스를 생성합니다.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| flaskclass         |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.01 sec)
```

### 8) MySQL에서 한국어 사용할 수 있도록 설정하기

현재 MySQL 서버에 존재하는 모든 데이터베이스의 정보를 확인

```bash
mysql> select * from information_schema.SCHEMATA;
+--------------+--------------------+----------------------------+------------------------+----------+
| CATALOG_NAME | SCHEMA_NAME        | DEFAULT_CHARACTER_SET_NAME | DEFAULT_COLLATION_NAME | SQL_PATH |
+--------------+--------------------+----------------------------+------------------------+----------+
| def          | information_schema | utf8                       | utf8_general_ci        | NULL     |
| def          | flaskclass         | latin1                     | latin1_swedish_ci      | NULL     |
| def          | mysql              | latin1                     | latin1_swedish_ci      | NULL     |
| def          | performance_schema | utf8                       | utf8_general_ci        | NULL     |
| def          | sys                | utf8                       | utf8_general_ci        | NULL     |
+--------------+--------------------+----------------------------+------------------------+----------+
```

- 기본적으로 우리는 latin1임(CharSet)

- utf8로 해야 한국어가 가능함(아래는 테이블을 변경할 때)

```bash
mysql> select * from information_schema.SCHEMATA;
mysql> show full columns from '테이블명';
mysql> alter table '테이블명' convert to character set utf8;
```

### 9) 컨테이너 생성할 때부터 데이터베이스도 함께 생성하기

- 기존 testdb 컨테이너 나가기: `docker stop testdb`

```bash
docker run --rm -d --name testdb \
-p 3307:3307 \
-e MYSQL_DATABASE=flaskclass \
-e MYSQL_ROOT_PASSWORD=password \
mysql:5.7 \
--character-set-server=utf8 \
--collation-server=utf8_general_ci
```

- 명령 프롬프트는,,,, ^더라,,,

```bash
docker run --rm -d --name testdb ^
-p 3306:3306 ^
-e MYSQL_DATABASE=flaskclass ^
-e MYSQL_ROOT_PASSWORD=password ^
mysql:5.7 ^
--character-set-server=utf8 ^
--collation-server=utf8_general_ci
```

(주석 포함)

```bash
docker run --rm -d --name testdb \ # 도커를 실행(run)할건데 컨테이너 정지 시, 컨테이너를 삭제(--rm)하고 백그라운드(-d)로 띄우고 컨테이너명(--name)은 testdb이다.
-p 3306:3306 \ # 포트는 3306을 사용할 것이고, 외부에 3306 포트로 오픈할것이다.
-e MYSQL_DATABASE=flaskclass \ # 기본적으로 flaskclass라는 MySQL 데이터베이스를 생성할 것이고,
-e MYSQL_ROOT_PASSWORD=password \ # root 유저의 패스워드는 password로 설정하고,
mysql:5.7 \ # MySQL 5.7버전을 이용할 것이다.
--character-set-server=utf8 \ # 한국어 지원을 위해 utf-8설정을 진행한다.
--collation-server=utf8_general_ci
```

## 2-3. Docker가 뭐임? 왜 Docker?

- 로컬에 구성을 할까 했는데, 너무 다 다름
- 이게 편하다고 판단

- 원래 각 OS에 MySQL을 설치하기 위해서는 더 복잡한 과정을 거쳐야함
    - 각 OS (윈도우, 맥OS, 리눅스 등)에 따라 설치 방법도 상이하고 과정 자체도 매우 귀찮
- 특정 애플리케이션을 신속하게 구축, 테스트 배포할 수 있는 소프트웨어 플랫폼이 도커
- 즉, 현재 나의 호스트 PC/서버의 OS환경을 신경 쓸 필요없이 도커만 설치되어 있다면, 원하는 애플리케이션을 실행

### 도커 컨테이너

도커를 통해 실행된 소프트웨어 구동 격리 환경

![image](https://user-images.githubusercontent.com/46991314/229362961-193f6b88-df1c-4fbc-bd84-112f1705f2a4.png)


### **도커 컨테이너와 Virtual Machine**

도커가 등장하기 이전엔 흔히 VM을 사용함

| 도커 | VM |
| --- | --- |
| 도커데몬 | 하이퍼바이저 |
| 프로세스 | 하드웨어 가상화 |
| 호스트 OS위, 컨테이너 프로세스 | 가상 하드웨어 위, 게스트 OS |

![image](https://user-images.githubusercontent.com/46991314/229362976-8c998d4c-d55d-456c-bfd9-8849bc7fc3e1.png)

VM은 OS전체를 띄우기 때문에, 비교적 무겁고 성능문제가 존재합니다.

이에 반해 도커는 호스트 OS의 자원을 이용하며, 필요한 만큼 CPU와 메모리를 이용하기 때문에, 성능적으로 우수합니다. 컨테이너 내부에도 접근할 수 있어, VM에서 할 수 있었던 것들 대부분이 가능

격리된 다른 환경을 만드는 점에서는 동일하지만, 둘의 OS자원 이용방법은 위 와 같이 다름

### 도커 이미지

- 이미지는 컨테이너 실행에 필요한 파일, 설정, 환경 등의 집합체
- 하나의 이미지를 통해서 복수개의 컨테이너를 생성할 수 있고, 컨테이너가 바뀌더라도 바라보는 이미지는 불변

### 왜 쓰는지 정리해보기(요약)

1. **개발 환경 구축 용이성**
    
    Docker는 개발 환경을 컨테이너로 묶어서 배포할 수 있으므로, 개발자는 다른 개발자와 동일한 환경에서 작업할 수 있습니다. 이를 통해 개발 환경을 구축하는 데 드는 시간과 비용을 절감할 수 있습니다.
    
2. **유연성**
    
    Docker는 다양한 운영체제와 언어를 지원하므로, 다양한 애플리케이션을 실행할 수 있습니다. 또한, Docker 이미지를 사용하여 다른 시스템에서도 동일한 애플리케이션을 실행할 수 있습니다.
    
3. **환경 일치성 보장**
    
    Docker는 애플리케이션을 실행하는 데 필요한 모든 요소를 포함하는 독립적인 컨테이너를 만들어줍니다. 이를 통해 각각의 컨테이너는 서로 다른 환경에서도 동일한 방식으로 동작할 수 있으므로 환경 일치성을 보장할 수 있습니다.
    
4. **자원 절약**
    
    Docker는 가상화 기술을 사용하여, 호스트 시스템의 자원을 효율적으로 활용할 수 있습니다. 이를 통해 더 많은 애플리케이션을 동일한 시스템에서 실행할 수 있습니다.
    
5. **배포 및 스케일링 용이성**
    
    Docker는 애플리케이션을 컨테이너로 묶어서 배포할 수 있으므로, 서버 환경이 달라지더라도 애플리케이션을 쉽게 배포할 수 있습니다. 또한, 컨테이너를 더 추가하거나 제거하여 스케일링을 쉽게 할 수 있습니다.
