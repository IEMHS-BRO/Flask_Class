# 1. 안녕 Flask!

## 1-1. hello.py 파헤쳐 보기

```python
'''
from 모듈 import 이름 -> 모듈 내에서 필요한 것만 콕 찍어서 가져오기
'''
from flask import Flask

'''
플라스크 애플리케이션을 생성하는 코드. 이 코드에서 __name__이라는 변수에는 모듈명이 담긴다.
즉, 이 파일이 실행되는 거면 hello.py라는 모듈이 실행되는 것 __name__ -> hello
'''
app = Flask(__name__)

'''
@app.route는 특정 주소에 접속하면 바로 다음 줄에 있는 함수를 호출하는 Flask의 데코레이터
'''
@app.route("/")
def hello():
    return "Hello World!"

'''
__main__은 최상위 코드가 실행되는 엔트리 포인트가 있는 영역의 이름을 의미
__name__은 모듈명이 담긴다고 했는데, 엔트리 포인트가 될 경우 __main__이 저장됩니다.
현재 파일이 엔트리 포인트로 사용되는지, 모듈로 import되어 사용되는지를 구분하기 위해서 사용하는 것.
(파이썬은 모듈을 import하여 가져오게 되면 해당 모듈이 실행되기에 구별이 필요함)
'''
if __name__ == "__main__":
    app.run()
```

실행하기 (2가지 모두 가능)

```bash
flask run
```

```bash
python hello.py
```

## 1-2. 디버그 모드 활성화

> 2가지 방법이 존재합니다.
> 
1. Flask 실행 환경을 개발 환경으로 설정(환경 변수를 설정하는 명령어)
    
    ```bash
    set FLASK_ENV=development
    
    # 개발 모드 활성화
    ```
    
2. 디버그 모드 활성화(방법 2가지)
    - Flask 어플리케이션 객체를 실행하면서 활성화
        
        ```python
        # 디버그 모드 활성화
        app.run(debug=True)
        ```
        
        ```bash
        # 파이썬 파일을 실행
        python hello.py
        ```
        
    - Flask 설정을 활성화
        
        ```bash
        # 디버그 모드 활성화
        set FLASK_DEBUG=true
        ```
        
        ```bash
        # 플라스크 실행(FLASK_APP 잘 설정해놔야함)
        flask run
        ```
        
- **디버그 모드 활성화**
    
    플라스크 실행 환경을 개발 환경으로 설정하면 디버그 모드가 활성화된다.
    
    - **에러발생화면** : 디버그 모드는 오류가 발생하면 디버깅 결과 메시지를 웹 브라우저에 출력해주며,
    - **Auto Reload** : 서버를 실행하고 있을 때 프로그램을 변경하면 서버가 자동으로 다시 시작하여 변경된 내용을 적용한다.

# 2. Flask로 백엔드는 어떻게 하는건가요?

## 2-1. 어떤 형식으로 데이터를 주고 받을까

### JSON

- **J**ava**S**cript **O**bject **N**otation
- 사람이 읽을 수 있는 경량화된 텍스트 기반의 데이터 교환 **표준**
- 우리가 잘 알고 있는 **XML(eXtensible Markup Language)**도 서로 다른 언어들간의 데이터 교환, 사람이 볼 수 있는 정보 표기, 쉽구 단순한 구성 등을 목표로 만들어진 데이터 교환방식 중의 하나인데 이보다 좀 더 쉽고 가볍게 만들어진 것이 **JSON**
- 속성-값(attribute-value) 구조
    - 자료형(Number, String, Boolean, Array, Object, Null)

```jsx
{
    "name": "성진",
    "age": 23,
    "isMale": True,
    "CompanyInfo": {
        "name": "인포마이닝"
    }
}
```

### JSON 쓰는 이유

1. **이기종 간의 데이터 교환**
2. **JSON은 특정 언어에 종속되지 않는다. → 데이터 형식 통일**
3. **XML보다 가볍기 때문에 최소한의 용량으로 데이터 전송이 가능**

### Hello, World!를 Json으로 보내보자(jsonify)

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/hello")
def hello():
    return jsonify(text="Hello World!")

if __name__ == "__main__":
    app.run()
```

## 2-2. 백엔드 예시

- 조회수 시스템을 만들어보자
    
    ```python
    hit_count = 0
    
    @app.route("/hits")
    def hits():
        global hit_count # 함수 외부에서 선언된 변수를 global 키워드로 재선언하면 접근 가능
        hit_count += 1
        return jsonify(
            text="Hits",
            count=hit_count
        )
    ```
    

## 2-3. Html 띄워보기(render_template)

- 프로젝트 내에 templates 폴더 생성(이름 준수!)
- templates 폴더 내부에 index.html 생성
    
    ```html
    <!DOCTYPE html>
    <html>
    <body>
        <h1>Welcome Home</h1>
        <h2>with Html</h2>
        <a href="/hello">Hello World! 바로가기</a>
        <br>
        <a href="/hits">조회수 시스템 바로가기</a>
    </body>
    </html>
    ```
    
- python
    
    ```python
    from flask import render_template
    
    @app.route("/")
    def home():
        return render_template("index.html")
    ```
    

# 3. Postman

[Postman API Platform | Sign Up for Free](https://www.postman.com/)

> API 개발자가 **API 테스트**, **문서화 및 공유**를 쉽게 할 수 있도록 도와주는 플랫폼
> 
- Postman을 사용하면 API 요청을 손쉽게 테스트하고, 요청과 응답을 쉽게 볼 수 있습니다.
- 또한, API 요청에 대한 문서화를 쉽게 할 수 있고, 다른 사람과 API 요청을 공유할 수도 있습니다.

### 가이드

1. Postman에서 "New" 버튼을 클릭하고, "Request"를 선택합니다.
2. 요청 메소드와 URL을 입력합니다.
3. 필요한 경우, 요청 헤더 및 바디를 추가합니다.
4. Send 버튼을 눌러 요청을 보내고, 응답을 확인합니다.
5. 요청을 저장하거나, 공유할 수 있습니다.

# 4. RestAPI

## 4-1. API는 무엇인가

- **A**pplication **P**rogramming **I**nterface
- 응용 프로그램(어플리케이션)에서 사용할 수 있도록, 운영체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스

## 4-2. RESTful을 훑어보자

- **RE**presentational **S**tate **T**ransfer( = 대표 상태 전송? )

### 먼저 알아야할 점

- 규칙보다는 가이드, 누구나 꼭 따라야 하는 것은 아니다
- RESTful하게 API를 설계할지 말지는 개발자의 선택이다.
- RESTful하지 않다고 나쁜 API는 아니다. 다만, 웹 발전적이라고는 말할 수 없다.
- RESTful의 특징은 설명해주는 것 외에도 엄청 많다.
- 즉, RESTful한 API를 만들려면 많은 시간과 노오력이 필요하다.

### REST의 구성요소

자원, 행위, 표현

- URL을 통해 **자원**을 **표현**
- 접근 자원에 대한 **행위**를 METHOD로 구분

### 메소드별 역할

HTTP 메소드에 대해 알아봅시다

| METHOD | Role | CRUD |
| --- | --- | --- |
| POST | 리소스 생성 | C(reate) |
| GET | 리소스 조회 | R(ead) |
| PUT | 리소스 교체 (없을 경우 생성) | U(pdate) |
| DELETE | 리소스 삭제 | D(elete) |

### 자원의 표현과 행위 예시

- 메모 데이터 조회
    
    ```
    GET http://example.com/api/memos/1 (O)
    GET http://example.com/api/memos/read/1 (X)
    ```
    
- 메모 데이터 생성
    
    ```
    POST http://example.com/api/memos (O)
    POST http://example.com/api/memos/create (X)
    ```
    
- 메모 데이터 삭제
    
    ```
    DELETE http://example.com/api/memos/1 (O)
    DELETE http://example.com/api/memos/delete/1 (X)
    ```
    
- 메모 데이터 수정
    
    ```
    PUT http://example.com/api/memos/1 (O)
    PUT http://example.com/api/memos/update/1 (X)
    ```
    

### 추가 예시

- 계층관계 표현
    
    ```
    http://example.com/api/ios/user
    http://example.com/api/and/memo
    http://example.com/api/web/memo/img
    ```
    
- URI 설계 포인트
    - 대문자와 밑줄(_)은 사용하지 않는다.
    - 가독성을 위해 써야한다면, 하이픈(-)을 사용한다.
    - 확장자는 URI에서 제거한다.
    
    ```
    http://example.com/API/Backends/Languages (X)
    http://example.com/api/backend_developers/1 (X)
    **http://example.com/api/backend-developers/1 (O)** 
    http://example.com/api/backenddevelopers/1 (O)
    ```
    

### 추가 공부

- HTTP
    
    [https://developer.mozilla.org/ko/docs/Web/HTTP](https://developer.mozilla.org/ko/docs/Web/HTTP)
    
- HTTP method
    
    [https://developer.mozilla.org/ko/docs/Web/HTTP/Methods](https://developer.mozilla.org/ko/docs/Web/HTTP/Methods)
    
- HTTP 상태코드
    
    [https://developer.mozilla.org/ko/docs/Web/HTTP/Status](https://developer.mozilla.org/ko/docs/Web/HTTP/Status)
    

# 5. Request Context

- HTTP : 우리가 평소 웹을 이용할 때, 자연스럽게 사용되는 **비연결성 프로토콜**입니다.(Request → Response)

같은 엔드포인트의 HTTP 리퀘스트더라도 **METHOD**가 다르거나, 같이 넘어온 페이로드에 따라 서버의 응답값이 바뀌어야한다.

**즉, 우리는 리퀘스트에 대한 데이터를 접근하고 구분할 수 있어야한다.**

```python
from flask import request, session
```

주요한 리퀘스트 컨텍스트에는 `request`, `session`이 있다. 클라이언트에 의해 인입된 HTTP 리퀘스트 컨텐츠를 상기 컨텍스트를 통해 손쉽게 접근할 수 있다.

- 참고
    
    [https://flask.palletsprojects.com/en/1.1.x/api/#flask.Request](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Request)
    

1. code 입력
    
    ```python
    from flask import request
    
    @app.route('/test/method/<id>')
    def method_test(id):
        return jsonify({
            'id': id,
            'request.method': request.method,
            'request.args': request.args,
            'request.form': request.form,
            # silent 파라미터는 JSON parsing fail 에 대해서 None 처리 여부를 설정
            # True 로 주면 get_json() 호출시 에러가 나지 않고 None을 리턴한다.
            'request.json': request.get_json(silent=True) 
        })
    ```
    
2. Postman으로 Request 던져보기
    
    ![image](https://user-images.githubusercontent.com/46991314/228394247-1ca859ee-c8d0-4452-bfb4-b01172e8abf4.png)
    
    ![image](https://user-images.githubusercontent.com/46991314/228394261-9e60dceb-447e-45fd-bcf5-c350721001ff.png)
    
    - Method를 Post로 했을 때 에러가 남
3. Method 허용 추가
    
    ```python
    from flask import request
    
    @app.route('/test/method/<id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
    def method_test(id):
        return jsonify({
            'request.method': request.method,
            'request.args': request.args,
            'request.form': request.form,
            # silent 파라미터는 JSON parsing fail 에 대해서 None 처리 여부를 설정
            # True 로 주면 get_json() 호출시 에러가 나지 않고 None을 리턴한다.
            'request.json': request.get_json(silent=True) 
        })
    ```
    
    ![image](https://user-images.githubusercontent.com/46991314/228394293-c0756f07-2707-4c74-9799-ce4a23809661.png)
    
    ![image](https://user-images.githubusercontent.com/46991314/228394310-ffc3996e-46e0-4519-8bda-b216e51cec27.png)
    
    ![image](https://user-images.githubusercontent.com/46991314/228394337-e0c7d3a1-4d94-44aa-a88d-3c4be63f7183.png)
    

# 6. 요약

- Flask 기본적인 세팅과 Hello, World
- JSON은 무엇인지와 Flask에서 JSON으로 반환하는 방법(jsonify)
- 백엔드 체감해보기
    - 조회수 시스템
- 웹페이지(템플릿)도 띄울 수 있다.
- Postman 사용해보기
- RestAPI가 무엇인가
- Context Request, Request를 뜯어보자
