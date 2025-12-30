from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root123@localhost/smallexercise'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit_name", methods=["POST"])
def submit_btn():
    data = request.get_json()
    user_name = data.get("name")

    if not user_name:
        return jsonify({"message": "Name is required!"}), 400

    new_user = User(name=user_name)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Name added successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
