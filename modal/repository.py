from db_modal.user_db_modal import User
from db_modal.database import engine
from .db_interface import DBInterface
class Repository:
    def __init__(self,db:DBInterface):
        self.__db=db 
    def registerNewUser(self, name, email, password,gender,role):
           return self.__db.registerNewUser(name,email,password,gender,role)
    def get_user_by_email(self,email):
            return self.__db.get_user(email)
        
    def new_course(self,title,author,description):
        return self.__db.add_course(title,author,description)
        
        
    def get_courses(self):
        return self.__db.fetch_courses()
   
   
    def searchCourses(self,search):
       return self.__db.search_courses(search)
   
   
    def new_lec(self,title,description,video_url):
       return self.__db.add_lecture(title,description,video_url)
   
    def get_lectures(self):
        return self.__db.fetch_lectures()
   
   
    def searchLec(self,search):
        return self.__db.search_lec(search)