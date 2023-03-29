from flask import Flask

app = Flask(__name__)

'''
Hello, World!를 Json으로 보내보자(jsonify)
'''
from flask import jsonify

@app.route("/hello")
def hello():
    return jsonify(text="Hello World!")


'''
조회수 시스템을 만들어보자
'''
hit_count = 0

@app.route("/hits")
def hits():
    global hit_count # 함수 외부에서 선언된 변수를 global 키워드로 재선언하면 접근 가능
    hit_count += 1
    return jsonify(
        text="Hits",
        count=hit_count
    )


'''
Html 띄워보기(render_template)
'''
from flask import render_template

@app.route("/")
def home():
    return render_template("index.html")


'''
Request Context
'''
from flask import request

#@app.route('/test/method/<id>')
@app.route('/test/method/<id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
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


if __name__ == "__main__":
	app.run(debug=True)
