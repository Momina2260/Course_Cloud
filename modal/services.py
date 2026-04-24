from flask import session
from werkzeug.security import generate_password_hash, check_password_hash
import re
from modal.db.sqlalchemy import Sqlalchemy
from modal.repository import Repository
#import engine from db_modal.database
from db_modal.database import engine  

class Services:
    def __init__(self):
       
        self.db = Sqlalchemy(engine)
        self.__repo = Repository(self.db)
        
    def insertUser(self,name,email,password,confirm,gender,role):
        if  not name or not email or not password :
            return "please enter full cradentials"
        
        if len(password) < 8 :
            return "lenght of password must be atleast 8 char! "
        
        if not re.search(r"[A-Z]", password):   
            return "password must contain atleast one uppercase!"
        
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):  
            return "password must contain atleast one special"
        if password != confirm:
            return "passwords do not match!"
        if not gender :
            return "please select you gender!"
        if not role :
            return "please select role!"
        existing_user=self.__repo.get_user_by_email(email)  
           
        if existing_user:
            return "user already exist please login instead!"
        hashed_password = generate_password_hash(password)
        
        userId = self.__repo.registerNewUser(name,email, hashed_password,gender,role)
        
        if userId != None:
            return f"{name}: registered successfully!"
        else:
            return "registeration failed!"
        #__________________________________________________
        
    def getUser(self,email,password):
        if not email or not password:
            return None, "provide full cradentials!"
        
        user=self.__repo.get_user_by_email(email)  
        
        if user is None:
            return None,"no user with such cradentials!"
        
        if not check_password_hash(user.password, password):
            return None, "Wrong password"

        return user,"login successfull"
      #______________________________________________________
   
        
        
    def add_New_course(self,title,author,description):
        
        if not title or not author or not description:
            return "fill all the field!"
        
        courseId=self.__repo.new_course(title,author,description)
        
        if courseId != None:
            return f"{title}:{author}:{description}:added successfully"
        else:
            return "no course added!"
            
        
    def get_all_Courses(self):
        courses=self.__repo.get_courses()
        return courses
    
    def  searchcourse(self,search):
            s_course=self.__repo.searchCourses(search)
            return s_course
        
     #---------------------------------------------       
    def add_New_lecture(self,title,description,video_url):
        if not title or not description or not video_url:
            return "fill all the field"
        lecId = self.__repo.new_lec(title,description,video_url)
        
        if lecId != None:
            return "new lecture added successfully"
        else:
            return "no lecture added.something went wrong" 
    #--------------------------------------------
    def get_all_lectures(self):
        lectures=self.__repo.get_lectures()
        return lectures
    
    def  searchlecture(self,search):
            s_lecture=self.__repo.searchLec(search)
            return s_lecture
        
        