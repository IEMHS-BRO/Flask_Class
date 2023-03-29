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
