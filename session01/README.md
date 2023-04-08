- [0. 허성진 소개](#0-허성진-소개)
- [1. 수업은 어떻게 진행하나요?](#1-수업은-어떻게-진행하나요)
- [2. 우리는 무엇을 하려는 건가요?](#2-우리는-무엇을-하려는-건가요)
  - [2-1. 소프트웨어 개발 절차](#2-1-소프트웨어-개발-절차)
  - [2-2. 소프트웨어 구성원의 역할](#2-2-소프트웨어-구성원의-역할)
  - [2-3. 학습 목표 (최종적으로 알려주고 싶은 것.)](#2-3-학습-목표-최종적으로-알려주고-싶은-것)
- [3. 왜 Flask인가요?](#3-왜-flask인가요)
  - [3-1. Flask를 왜 배워요?](#3-1-flask를-왜-배워요)
  - [3-2. 요즘 스타트업들이 Python+Flask로 개발하고 Java+Spring으로 넘어간다](#3-2-요즘-스타트업들이-pythonflask로-개발하고-javaspring으로-넘어간다)
- [4. 개발 환경 세팅](#4-개발-환경-세팅)
  - [4-1. 사용 스택 체크](#4-1-사용-스택-체크)
  - [4-2. 설치 및 설정](#4-2-설치-및-설정)
- [5. 요약](#5-요약)

<br><br>

# 0. 허성진 소개

- 이름: 허성진
- 학교: 인천전자마이스터고 정보통신과 8기 졸업
- 회사: (주)인포마이닝(2020.01~)
- 직무: iOS Developer

# 1. 수업은 어떻게 진행하나요?

> **Github Organization을 통해서 공유**
URL: [https://github.com/IEMHS-BRO](https://github.com/IEMHS-BRO)
> 
- `Flask_Class` 레포지토리로 공유합니다.
- 질문은 Issue에 올려주면 답변을 해드립니다.
- Git, Github과 친하게 지내봅니다. (저도 친해지는 중입니다...ㅎ)

> **Why → How to**
> 

‘어떻게 만드는지’보다 ‘왜 만드는 지'에 집중합니다.

어려운 코드를 쳐보려는 노력보다 쉬운 코드라도 하나씩 뜯어보며  정확히 이해하도록 합니다.

> **같이 검색**
> 
- 프로젝트, 실무에서 가장 중요한 검색 능력
- 전세계 모든 개발자들은 크롬 없으면 개발을 못하지 않을까,,,

# 2. 우리는 무엇을 하려는 건가요?

## 2-1. 소프트웨어 개발 절차

### **아래와 같은 복잡한 이론적 개발 절차는 나중에 필요할 때 이해해도 됩니다.**

![image](https://user-images.githubusercontent.com/46991314/226987573-6d02189f-747a-4f99-a90b-457f1a506a45.png)

### 최대한 직관적으로, 이해하기 쉽게! (이론 베이스가 아니다보니, 용어가 다를 수 있음)

1. **대표의 한마디**
2. **전략기획**
    - 비즈니스 생태계에서 살아남을 비즈니스 모델을 만드는 것
    - 언제 어디서나 방향을 잃지 않도록 하늘에 북극성을 띄어주는 것
3. **서비스기획**
    - 사용자를 고려하며 서비스 모델을 정교화하는 것
    - 그 북극성을 목표로 어떻게 바다를 헤쳐나갈지 선원들과 상의해서 노를 저어가는 것
4. **UI/UX디자인**
    - UI는 사용자가 제품/서비스를 사용할 때, 마주하게 되는 면
    - UX는 사용자 경험의 약자로, 사용자가 어떠한 서비스/ 제품을 직간접적으로 이용하면서 느끼는 종합적인 만족
5. **개발**
    - 서버 개발(DB, 웹 백엔드)
    - 클라이언트 개발(모바일, 웹 프론트)
6. **테스트**
    - 코드로 테스트
    - 직접 테스트
7. **배포**
    - 앱스토어, 플레이스토어 배포
    - 웹 서버 배포
8. **운영**
    - 관리자 페이지
    - CS(Customer Service)
    - 에러, 트래픽 대응

### ex) 배달의민족의 배민페이 시스템

1. **대표의 한마디**
    - 배달 결제할 때 우리 시스템에서 결제할 순 없나?
2. **전략기획**
    - 자체 결제 시스템을 개발하여, 타 결제 시스템을 사용할 때 발생되는 수수료를 절약하자
3. **서비스기획**
    - 결제 시스템을 사용하면 포인트를 주자
    - 카드나 계좌를 등록하여 편하게 결제되도록 하자
4. **UI/UX디자인**
    - UI: 카드 등록하는 버튼을 이쁘게 디자인하자
    - UX: 카드 등록하기 쉽게 화면을 디자인하자
5. **개발**
    - 서버 개발: 카드 등록하는 기능, 결제 시스템 연동
    - 클라이언트 개발: 카드 등록하는 화면, 결제 통신 기능
6. **테스트**
    - 카드 등록이 잘 되는가?
    - 등록된 카드가 없어지지는 않는가?
    - 결제가 잘 되어서 돈이 보내지는가?
    - 결제가 여러번 되지는 않는가?
    - ...등등
7. **배포**
    - 앱스토어에 신규 버전 배포
    - 서버 배포(먼저 배포하면 의미가 없음)
8. **운영**
    - 관리자 페이지 : 결제된 금액을 관리하는 페이지
    - CS(Customer Service) : 결제가 안됩니다
    - 에러, 트래픽 대응 : 결제 에러, 결제 트래픽 과다 등

## 2-2. 소프트웨어 구성원의 역할

![image](https://user-images.githubusercontent.com/46991314/226987737-33c45a00-c52a-4a4f-9b95-ce58965aa835.png)

> **백엔드는 서버와의 통신, 그리고 프론트와의 통신을 관리합니다. 서버와의 통신으로 데이터를 저장하고 프론트와의 통신으로 데이터를 출력합니다.**
> 

## 2-3. 학습 목표 (최종적으로 알려주고 싶은 것.)

> **DB를 거느릴 수 있는 API를 제공하는 백엔드 개발자 🔥**
> 

# 3. 왜 Flask인가요?

## 3-1. Flask를 왜 배워요?

### 1) Flask**란?**

Python 기반 ***micro*** 웹 프레임워크

---

### 2) 마이크로(micro)의 의미가 무엇인가요?

> The “micro” in microframework means Flask aims to keep the core simple but extensible.Everything else is up to you, so that Flask can be everything you need and nothing you don’t.
> 
> 
> 심플하지만 확장가능하게 유지한것을 의미한다. 즉, 어떻게 사용하냐에 따라 좋은 프레임워크가 될 수 있고 그렇지 않을 수도 있다.
> 

→ 프레임워크를 **간결**하게 유지하고 **확장**할 수 있도록 만들었다는 뜻.

1. **간결하다**
   
    아래 코드는 완벽하게 동작하는 Flask 웹 프로그램으로, 
    이 코드를 실행하여 웹 브라우저로 접속하면 화면에 “Hello World!”가 출력된다.
    **파일 하나로 구성된 짧은 코드만으로도 완벽하게 동작하는 웹 프로그램을 만들 수 있다.**
    
    ```python
    from flask import Flask
    
    app = Flask(__name__)
    
    @app.route("/")
    def hello():
    	return "Hello World!"
    
    if __name__ == "__main__":
    	app.run()
    ```
    
2. **확장성 있다**
   
    Flask에는 폼(form), 데이터베이스(database)를 처리하는 기능이 없다. Django는 프레임워크 자체에서 폼과 데이터베이스를 처리하는 기능이 포함되어 있다. Django는 쉽게 말해 큰 종합 선물 세트이다.
    
    그러면 Flask가 안좋은 걸까?
    
    Flask는 확장 모듈이라는 것을 사용하여 이를 보완한다. 이 말은 Flask로 만든 프로젝트의 무게가 가볍다는 것을 의미한다. 왜냐하면 Flask는 처음부터 모든 기능이 포함되어 있지 않고, 그때그때 개발자가 필요한 확장 모듈을 포함해 가며 개발하면 되기 때문이다.
    

---

### 3) Flask와 Django의 차이점

| 구분 | Flask | Django |
| --- | --- | --- |
| 생성년도 | 2010 | 2005 |
| 프레임워크 성향 | MSA | 모놀리식 |
| ORM (=Object Relational Mapping) | X | O |
| 지원기능 | 상대적으로 적음 | 상대적으로 많음 |
| 러닝 커브 | 상대적으로 낮음 | 상대적으로 높음 |
| 코드크기 | 상대적으로 작음 | 상대적으로 큼 |
| 유연성 | 좋음 | 제한됨 |
| 개발자의 책임 | 상대적으로 큼 | 상대적으로 작음 |

ORM: 데이터베이스를 쉽게 사용할 수 있도록 해주는 인터페이스

---

### 4) 인지도(?) 비교

[Build software better, together](https://github.com/search?o=desc&q=python+web+framework&s=stars&type=Repositories)

- 라이브러리나 프레임워크를 고를 때 Github의 Star수를 통해 인지도를 비교하곤 합니다.

---

### 5) 어느 프레임워크가 더 좋은가요?

어느 쪽이 더 좋다고 할 순 없다. 프로젝트에 맞는 프레임워크를 선택하면 된다.
일반적으로 MSA형태의 소규모 프로젝트에 단일 기능을 구현하는 웹에 Flask가 보다 더 적합하다.

간혹 Django는 소규모 프로젝트에 한해서 오버스펙이 되기도 한다.

Flask의 경우, 지원기능이 적은만큼 필요한 기능을 구현해야 할 때마다, 별도의 라이브러리를 설치하고 Flask 어플리케이션과 바인딩 해줘야한다.

즉, 살이 붙으면 붙을수록 개발 cost도 높아지게 된다.

- 주의점 : 너무 커스텀하지말자

---

**[Python developers survey 2020](https://www.jetbrains.com/lp/python-developers-survey-2020/)**

![https://user-images.githubusercontent.com/35549955/111418033-46bb7a80-872a-11eb-9446-6c4193e32a57.png](https://user-images.githubusercontent.com/35549955/111418033-46bb7a80-872a-11eb-9446-6c4193e32a57.png)

*<출처: [제트브레인](https://www.jetbrains.com/lp/python-developers-survey-2020)>*

---

## 3-2. 요즘 스타트업들이 Python+Flask로 개발하고 Java+Spring으로 넘어간다

![image](https://user-images.githubusercontent.com/46991314/230729359-6d6fe3bc-fbf6-4a44-8639-c97c43cebd92.png)

# 4. 개발 환경 세팅

## 4-1. 사용 스택 체크

- Anaconda
  
    → 가상환경을 위해 사용(venv를 사용하기도 함)
    
- Python: `v3.8.X`
- Flask
- VSCode(PyCharm도 무관)

### 1) PIP는 무엇인가요?

> **P**ip **I**nstalls **P**ackages
> 

파이썬으로 작성된 패키지 라이브러리를 설치하고 관리해주는 패키지 관리자(Package Manager)

---

### 2) 가상환경은 무엇인가요?

- 프로젝트를 진행할 때 독립된 환경을 만들어주는 고마운 도구
- 가상환경을 이용하면 하나의 데스크톱에 서로 다른 버전의 파이썬과 라이브러리를 쉽게 설치해 사용할 수 있다.

---

## 4-2. 설치 및 설정

### 1) Anaconda 설치

1. **설치 사이트에서 설치**
   
    [Anaconda | Anaconda Distribution](https://www.anaconda.com/products/distribution)
    
2. **환경변수 설정 부분에서는 그림의 박스 부분을 체크한다. (아나콘다를 환경변수에 추가하는 설정이다. 체크를 안하면 수동으로 추가를 해야한다.)**
   
    ![image](https://user-images.githubusercontent.com/46991314/226988133-dd29034b-57bf-4618-aace-e56b151f5d6e.png)
    
3. **Anaconda Prompt 실행**
4. **설치 확인**
   
    ```bash
    conda --version
    ```
    
5. **Anaconda Package Update**
   
    ```bash
    conda update
    ```
    

---

### 2) Anaconda 가상환경 생성

1. **가상환경 생성**
    
    파이썬을 특정 버전으로 지정하여 설치 가능
    
    ```bash
    # conda create -n (가상환경 이름) python=(버전)
    conda create -n flask_class python=3.8
    ```
    
2. **가상환경 리스트 조회**
    
    ```bash
    conda env list
    ```
    
3. **가상환경 활성화**
    
    활성화 시 명령줄 좌측에 (base)가 가상환경 이름으로 변경됨.
    
    ```bash
    #conda activate (가상환경 이름)
    conda activate flask_class
    ```
    
4. 현재 **가상환경 비활성화**
    
    ```bash
    conda deactivate
    ```
    
- **생성된 가상환경 삭제(패키지 포함)**
    
    ```bash
    conda remove -n (가상환경 이름) --all
    ```
    

---

### 3) Flask 설치

```bash
# 가상환경 활성
# conda activate (가상환경 이름)

pip install flask
```

---

### 4) 에디터에 가상환경 연결(Visual Studio Code)

1. **VSCode 준비**
2. **Python Extension 설치**
    - Extension > Python 설치 > 재실행
3. **인터프리터 설정**
    - Command Pallete 열기 : Ctrl + Shift + P
    - Python: Select Interpreter 입력 및 클릭
4. **생성한 가상환경 선택**

---

### 5) 테스트

1. **hello.py 파일 만들기**
2. **기본 어플리케이션 설정(원래 기본은 app)**
   
    ```bash
    set FLASK_APP=hello
    ```
    
3. **Flask 실행**
   
    ```bash
    flask run
    ```
    
4. **[http://127.0.0.1:5000](http://127.0.0.1:5000/) 접속**
    -> Hello, World!

---

# 5. 요약

1. Github Organization을 통해 수업 자료 공유
2. Why → How to
3. 소프트웨어의 개발 절차
4. 소프트웨어 구성원의 역할과 우리의 역할
5. Python/Flask를 선택한 이유
6. 개발환경 세팅(Anaconda, Flask, VSCode)
