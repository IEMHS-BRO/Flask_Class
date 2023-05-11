# 1. Application Factories

[Application Factories — Flask Documentation (1.1.x)](https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/)

(Basic Factories 참고)

- flask run을 할 때 그 파일에 create_app이란게 있으면 이걸 실행함
- 여기서 리턴 받은 것을 앱으로 사용하여 실행함

- `__init__.py`를 만들게 되면, 해당 디렉토리가 파이썬 모듈화된다는 의미

```python
__init__.py

from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return 'hello world'

    return app
```

- `export FLASK_APP=디렉토리명`
    - 기존에는 파일만 설정했었는데, 이제 디렉토리로 관리가 가능해짐.
- `flask run`

# 2. Blueprint

[Modular Applications with Blueprints — Flask Documentation (1.1.x)](https://flask.palletsprojects.com/en/1.1.x/blueprints/)

- 라우트 처리가 많이지고 점차 관리가 힘들어질때, 블루프린트를 이용하면 확장에 용이해짐

- `routes` 폴더 생성
- `base_routes.py`
    
    ```python
    from flask import Blueprint
    
    NAME = 'BASE'
    
    bp = Blueprint(NAME, __name__) // 이제 이 NAME은 네임스페이스가 될 것
    
    @bp.route('/')
    def index():
        return 'hello world'
    ```
    
- 플라스크랑 연결을 해줘야함
    
    ```python
    ''' Routes INIT '''
    from test.routes import base_routes
    app.register_blueprint(base_routes.bp)
    ```
    
- auth_routes.py (인증)
    
    ```python
    from flask import Blueprint
    
    NAME = 'AUTH'
    
    bp = Blueprint(NAME, __name__) // 이제 이 NAME은 네임스페이스가 될 것
    
    @bp.route('/auth/')
    def index():
        return 'hello world'
    ```
    

# 3. 기획서 공유

https://www.figma.com/file/PpCS4QFVD4WpJ86M2mzYIs/StrawberryMarket?node-id=0%3A1&t=BHcfXP1yCKZE4hZB-1

- 우리가 만들려는 것은 무엇인가?

## 3-1. 요구사항 분석, 데이터 설계

- 요구사항 분석
    - 개발 대상에 대한 사용자의 요구사항 중 명확하지 않거나 모호한 부분을 걸러내기 위한 방법
    - 다양한 기법이 존재함
- 데이터 설계
    - 보여줘야하는 데이터를 모아보자
    - 그 외에 관리해야하는 데이터도 있을까?

- UserTable
    - 아이디
    - 비밀번호
    - 이름
    - 전화번호
- ProductTable
    - 사진
    - 제목
    - 가격
    - 내용
    - **판매자**
    - 날짜

## 3-2. Figma를 사용해보자

- 예술과 디자인은 다르다. 디자인 능력 중요
    - 할 줄 알면 무조건 좋다.
    - UI말고도 UX라도(러프하게)
    - 프로토타이핑 최고
- 그 외에도 다양한 Tool을 적극 사용해보자
    - 새로운 기술을 잘 수용하는 태도를 가져보자
- Figjam도 좋아요
    - FlowChart, Brain Storming
