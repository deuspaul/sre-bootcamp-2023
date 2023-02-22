from flask import Flask
from flask import jsonify
from flask import request
from methods import Token, Restricted
#from flask_sqlalchemy import SQLAlchemy
#from werkzeug.security import generate_password_hash,check_password_hash

app = Flask(__name__)
login = Token()
protected = Restricted()

#app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://secret:jOdznoyH6swQB9sTGdLUeeSrtejWkcw@sre-bootcamp-selection-challenge.cabf3yhjqvmq.us-east-1.rds.amazonaws.com:3306/bootcamp_tht'
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#db = SQLAlchemy(app)

# Just a health check
@app.route("/")
def url_root():
    return "OK"


# Just a health check
@app.route("/_health")
def url_health():
    return "OK"


# e.g. http://127.0.0.1:8000/login
@app.route("/login", methods=['POST'])
def url_login():
    username = request.form['username']
    password = request.form['password']
    res = {
        "data": login.generate_token(username, password)
    }
    print(res)
    #print(username)
    #print(password)
    #return 'received'
    return jsonify(res)


# # e.g. http://127.0.0.1:8000/protected
@app.route("/protected")
def url_protected():
    auth_token = request.headers.get('Authorization')
    print(auth_token)
    res = {
        "data": protected.access_data(auth_token)
    }
    return jsonify(res)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
