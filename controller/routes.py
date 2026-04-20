from flask import Blueprint, render_template,request,redirect, session,url_for
from modal.services import Services


routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')


@routes.route("/register", methods=["Get","Post"])
def register():
    message = ""
    if request.method == "POST":
        print ("POST REQUEST RECEIVED")
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm= request.form.get("confirm-password")
        gender = request.form.get("gender")
        role = request.form.get("role")
        message = Services().insertUser(name,email,password,confirm,gender,role)
        
        #return redirect(url_for("routes.login"))
    return render_template('register.html',message=message)


@routes.route("/login",methods=["Get","Post"])
def login():
    message = ""
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        message = Services().getUser(email,password)
    return render_template('login.html',message=message)
 
@routes.route("/td")
def teacher_dashboard():
    courses=Services().getCourse()
    return render_template("teacher_dashboard.html")