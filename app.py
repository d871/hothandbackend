from datetime import datetime

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
# try appliaction
application = Flask(__name__)
app = application

application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)
password = "2@asfizkg4fas?r"


class HotHandDatabase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    l_pressed = db.Column(db.String(2000))
    r_pressed = db.Column(db.String(2000))
    u_pressed = db.Column(db.String(2000))
    d_pressed = db.Column(db.String(2000))
    l_top = db.Column(db.String(400))
    r_top = db.Column(db.String(400))
    u_top = db.Column(db.String(400))
    d_top = db.Column(db.String(400))
    score = db.Column(db.String(4))
    settings = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default=datetime.now)


@application.route('/', methods=['POST', 'GET'])
def mojefunkce():
    if request.method == 'POST':
        if request.json["password"] == password:
            print("password was cool")
            req = request.json
            hot = HotHandDatabase(
                l_pressed=str(req["l_pressed"]),
                r_pressed=str(req["r_pressed"]),
                u_pressed=str(req["u_pressed"]),
                d_pressed=str(req["d_pressed"]),
                l_top=str(req["l_top"]),
                r_top=str(req["r_top"]),
                u_top=str(req["u_top"]),
                d_top=str(req["d_top"]),
                score=str(req["score"]),
                settings=str(req["settings"])
            )
            db.session.add(hot)
            db.session.commit()
            return {"status": "ok"}
        # print(request.json)
        # print(type(request.json))
        # print(request.json["l_pressed"])
        # user = User(first=str(request.json), second="nic")
        # db.session.add(user)
        # db.session.commit()
        else:
            return {"status": "not ok"}
    else:
        print("hello world")
        return{"status": "ok"}


# if __name__ == '__main__':
#     app.run(debug=True)
