from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(20), unique=True, nullable=False)
    user_name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)

# 3306이면 따로 포트 명시 안해도 됨.
hostname = "localhost:3307"
username = "root"
password = "password"
db_name = "flaskclass"
uri = "mysql+pymysql://"+username+":"+password+"@"+hostname+"/"+db_name+"?charset=utf8"
app.config['SQLALCHEMY_DATABASE_URI'] = uri

# DB INIT
db.init_app(app)
migrate.init_app(app, db)


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

if __name__ == "__main__":
    app.run(debug=True)