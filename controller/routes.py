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
    result = ""
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        user,error = Services().getUser(email,password)
        if error:
            return render_template("login.html",result = error)
            
        if user and user.role == 'teacher':
            return redirect(url_for('routes.teacher_dashboard',result = user))
    return render_template('login.html',result=result)
 


@routes.route("/add_new_course",methods =["Get","Post"])
def addCourse():
    result=""
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        description = request.form.get("description")
        result=Services().add_New_course(title,author,description)
        
    return render_template("add_new_course.html", result=result)
    
    #------------------------------------------------
@routes.route("/addlec",methods=["Get","Post"])   
def addlec():
    result=""
    if request.method == "POST":
            title = request.form.get("title")
            description = request.form.get("description")
            video_url=request.form.get("video_url")
            result=Services().add_New_lecture(title,description,video_url)
        
    return render_template("add_lecture.html", result=result)
    
#--------------------------------------------
@routes.route("/cd")
def course_detail():
    lectures=""
    search = request.args.get("search", "").strip()
    if search:
        lectures=Services().searchlecture(search)
        print("search done")
    else:
        lectures=Services().get_all_lectures()
        print("no search")
    return render_template("course_detail.html",lectures=lectures)
    
@routes.route("/td")
def teacher_dashboard():
    courses=""
    search = request.args.get("search", "").strip()
    if search:
        courses=Services().searchcourse(search)
        print("search done")
    else:
        courses=Services().get_all_Courses()
        print("no search")
    return render_template("teacher_dashboard.html",courses=courses)