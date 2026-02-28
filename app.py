from flask import Flask, render_template, redirect, url_for, request
from models import db, User, Bug
from flask_login import LoginManager, login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()

@app.route("/")
@login_required
def dashboard():
    bugs = Bug.query.all()
    return render_template("dashboard.html", bugs=bugs)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = generate_password_hash(request.form["password"])
        role = request.form["role"]

        new_user = User(username=username, password=password, role=role)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()
        if user and check_password_hash(user.password, request.form["password"]):
            login_user(user)
            return redirect(url_for("dashboard"))

    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/create", methods=["GET", "POST"])
@login_required
def create_bug():
    if request.method == "POST":
        bug = Bug(
            title=request.form["title"],
            description=request.form["description"],
            severity=request.form["severity"],
            assigned_to=request.form["assigned_to"]
        )
        db.session.add(bug)
        db.session.commit()
        return redirect(url_for("dashboard"))

    return render_template("create_bug.html")

if __name__ == "__main__":
    app.run(debug=True)