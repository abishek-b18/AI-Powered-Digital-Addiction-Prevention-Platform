from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
import pickle
import numpy as np

app = Flask(__name__)
app.secret_key = "digital_addiction"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))

class Activity(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    screen_time = db.Column(db.Float)
    social_media = db.Column(db.Float)
    gaming = db.Column(db.Float)
    sleep = db.Column(db.Float)

model = pickle.load(open("ml/addiction_model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == "POST":
        user = User(
            username=request.form['username'],
            password=request.form['password']
        )
        db.session.add(user)
        db.session.commit()
        return redirect('/login')
    return render_template("register.html")

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == "POST":
        user = User.query.filter_by(
            username=request.form['username'],
            password=request.form['password']
        ).first()

        if user:
            session['user'] = user.username
            return redirect('/dashboard')

    return render_template("login.html")

@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    prediction = ""

    if request.method == "POST":

        screen_time = float(request.form['screen_time'])
        social_media = float(request.form['social_media'])
        gaming = float(request.form['gaming'])
        sleep = float(request.form['sleep'])

        data = np.array([[screen_time,
                          social_media,
                          gaming,
                          sleep]])

        result = model.predict(data)

        if result[0] == 0:
            prediction = "Low Addiction Risk"
        elif result[0] == 1:
            prediction = "Moderate Addiction Risk"
        else:
            prediction = "High Addiction Risk"

        activity = Activity(
            username=session['user'],
            screen_time=screen_time,
            social_media=social_media,
            gaming=gaming,
            sleep=sleep
        )

        db.session.add(activity)
        db.session.commit()

    return render_template(
        "dashboard.html",
        prediction=prediction
    )

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)