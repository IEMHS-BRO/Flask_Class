# 1. 인증?

> 인증(Authentication)
> 

사용자가 자신이 주장하는 사람이 맞는지 확인하는 과정

예를 들어, 우리가 로그인을 할 때 아이디와 비밀번호를 입력하는 과정이 인증 과정에 해당

### HTTP 통신에서 인증이 왜 필요한가요?

웹 서비스는 HTTP 프로토콜을 통해 클라이언트와 서버가 정보를 주고 받음

HTTP는 기본적으로 상태를 유지하지 않는 특성을 가지고 있기 때문에, 서버는 같은 사용자가 연속적인 요청을 보내더라도 각 요청이 독립적인 것으로 인식합니다.

이 때문에 인증이 필요하게 됩니다. 사용자가 서비스를 이용하는 동안 계속해서 자신을 증명해야 하는 것이죠.

# 2. 토큰 기반 인증은 무엇인가요?

토큰 기반 인증은 인증 정보를 토큰 형태로 저장하고 이를 활용하는 방식입니다. 사용자가 로그인을 하면 서버는 해당 사용자의 정보를 암호화한 토큰을 생성하고 이를 사용자에게 전달합니다. 그리고 사용자는 이 토큰을 이용해 인증을 진행합니다.

### HTTP 통신에서 토큰 기반 인증을 왜 사용하나요?

HTTP의 상태 비저장 특성 때문에 서버는 클라이언트에게서 들어오는 요청이 어떤 사용자로부터 왔는지 알 수 없습니다. 이를 해결하기 위해 세션 기반 인증 방식이 등장했지만, 이는 서버에 부담을 주고 확장성을 제한하는 문제가 있었습니다. 반면 토큰 기반 인증은 서버가 상태를 유지하지 않아도 되므로 이런 문제를 해결할 수 있습니다.

# 3. JWT와 OAuth

### JWT는 무엇인가요?

JWT(JSON Web Token)는 웹 표준(RFC 7519)으로, 두 개체에서 JSON 객체를 사용하여 정보를 안전하게 전송하기 위한 간결하고 독립적인 방법입니다. JWT는 자체적으로 정보를 검증할 수 있습니다.

### OAuth는 무엇인가요?

OAuth(Open Authorization)는 사용자가 특정 애플리케이션에게 특정 권한만을 부여할 수 있게 하는 인증 방식입니다. 예를 들어, 사용자가 페이스북이나 구글 계정을 통해 다른 서비스에 로그인하는 것이 OAuth를 활용한 예입니다.

### JWT와 OAuth 차이가 뭔가요? 언제 사용하나요?

JWT와 OAuth를 한 번에 접하게 되면 두 가지의 개념을 명확하게 정리하고 싶어진다.

둘 다 인증에 관한 기술로 

- JWT는 토큰의 종류
- OAuth는 토큰을 발급하고 인증하는 오픈 스탠다드 프로토콜

언제 사용하는가?

- JWT는 주로 사용자의 신원을 확인하고, 그 사용자에 대한 정보를 안전하게 전송하는 데 사용
    - JWT는 주로 회원인증(명확한 정보를 가진 토큰)
- OAuth는 사용자가 자신의 계정 정보를 직접 공유하지 않고도 다른 애플리케이션에서 특정 권한을 허용하도록 하는 데 사용
    - OAuth는 모호한 토큰. 어떠한 사용자의 정보 등과 같은 중요한 정보가 있는 명확한 정보를 가지고 있는 토큰이 아님. 랜덤한 수(포인터 같은 느낌)

### 사용자에게 발급해준 토큰, DB에 저장해야하나요?

- 일반적으로 액세스 토큰은 서버 측에서 발급하고, 클라이언트에게 전달
- 이렇게 발급된 액세스 토큰이 DB에 저장될 필요가 없다
- 이는 서버가 사용자의 인증 정보를 토큰에 포함시키고 이를 암호화하기 때문
- 액세스 토큰은 클라이언트 측에서 API 호출할 때 사용, 서버 측에서 유효성 검사를 하여 인증이 되는 것.
- 따라서 서버는 클라이언트로부터 받은 토큰을 해독하여 사용자를 인증할 수 있습니다.

**→ 토큰에 정보가 포함되어있는 것!**

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8acb7df2-9420-407a-bc83-9895f013b222/Untitled.png)

# 4. 실습해보자(JWT)

### 0. Flask-JWT-Extended

- Flask에서 JWT를 쉽게 구현할 수 있게 도와주는 패키지
- 설치 필요
    
    ```bash
    pip install flask-jwt-extended
    ```
    
- freeze도 하자
    
    ```bash
    pip freeze > requirements.txt
    ```
    

[Basic Usage — flask-jwt-extended 4.4.4 documentation](https://flask-jwt-extended.readthedocs.io/en/stable/basic_usage/)

### 1. 기본 세팅

```python
# app.py

from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

if __name__ == "__main__":
    app.run()
```

### 2. 코드 작성

1. app.config에 jwt 토큰을 만들 secretkey를 등록하고
    
    ```python
    app = Flask(__name__)
    
    from flask_jwt_extended import JWTManager
    app.config["JWT_SECRET_KEY"] = "super-secret"
    jwt = JWTManager(app)
    ```
    
2. 로그인 API를 만든다.
    - 성공하면 200 및 토큰을 발행
        - create_access_token(identity=username)
    - 실패하면 401 반환
    
    ```python
    from flask_jwt_extended import create_access_token
    
    @app.route("/login", methods=["POST"])
    def login():
        username = request.json.get("username", None)
        password = request.json.get("password", None)
        if username != "test" or password != "test":
            return jsonify({"msg": "Bad username or password"}), 401
    
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    ```
    
3. 토큰을 필요로하는 API를 만든다.
    - `jwt_required()`사용
        - 헤더에 토큰이 있으면 200 및 현재 사용자 정보 추출
        - 없으면 401 반환
    
    ```python
    from flask_jwt_extended import jwt_required
    from flask_jwt_extended import get_jwt_identity
    
    @app.route("/protected", methods=["GET"])
    @jwt_required()
    def protected():
        # Access the identity of the current user with get_jwt_identity
        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), 200
    ```
    

### 3. `jwt_required()`추가 내용

[API Documentation — flask-jwt-extended 4.4.4 documentation](https://flask-jwt-extended.readthedocs.io/en/stable/api/#flask_jwt_extended.jwt_required)

- Flask JWT Extended에서 제공하는 **데코레이터**
- 이 데코레이터를 사용하면, 해당 API 엔드포인트에 접근하기 전에 JWT의 유효성을 검증하게 됩니다.
- **`jwt_required()`** 데코레이터를 API 엔드포인트 함수 위에 사용하면, 클라이언트가 해당 API를 호출할 때 JWT를 제공해야만 인증이 통과됩니다. JWT가 유효하지 않을 경우, 401 Unauthorized 응답이 반환됩니다.
- 이를 통해 JWT 기반 인증 시스템에서 특정 API 엔드포인트의 접근을 제한할 수 있다.

### 생각해보면 로그인할 때마다 토큰말고 아이디 비밀번호 던져도 되는거 아니야?
토큰 쓰는 이유가 뭐야?

로그인할 때마다 아이디와 비밀번호를 전송하여 인증을 수행할 수도 있습니다. 그러나 토큰 기반 인증을 사용하는 이유에는 몇 가지 이점이 있습니다:

1. 보안성: 아이디와 비밀번호를 매번 전송하는 대신에 토큰을 사용하면, 중요한 인증 정보를 매번 노출시키지 않아도 됩니다. 토큰은 일정 기간 동안 유효하며, 암호화되어 있어서 보안성이 높습니다. 따라서 토큰이 노출되더라도 악용하기 어렵습니다.
2. 성능: 토큰을 사용하면 로그인 요청마다 서버에서 ID와 비밀번호를 검증하는 작업을 수행할 필요가 없어집니다. 대신에 토큰을 검증하면 되므로, 서버 부하가 줄어들고 성능이 향상됩니다.
3. 확장성: 토큰 기반 인증은 다양한 클라이언트와 서비스 간의 상호 운용성을 제공합니다. 클라이언트는 발급받은 토큰을 사용하여 여러 서비스에 접근할 수 있으며, 서버는 토큰의 유효성을 검증하여 인증을 수행합니다. 이는 분산 시스템이나 멀티플랫폼 환경에서 유용합니다.
4. 사용자 경험: 토큰을 사용하면 로그인 후에도 계속 인증을 유지할 수 있습니다. 클라이언트는 토큰을 저장하여 이후 요청에 사용하므로, 매번 로그인을 다시 수행할 필요가 없습니다. 이는 사용자 경험을 향상시키고, 로그인 장벽을 낮추는 데 도움이 됩니다.

따라서, 토큰 기반 인증은 보안성, 성능, 확장성, 사용자 경험 등의 이점을 제공하여 많은 웹 애플리케이션에서 사용되고 있습니다.
