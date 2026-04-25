from abc import abstractmethod
from sqlalchemy.orm import Session, sessionmaker
from db_modal.database import engine,Base
from db_modal.user_db_modal import User,Course,Lecture
#import DBInterface from modal.db.db_interface
from modal.db_interface import DBInterface
from sqlalchemy.orm import sessionmaker
class Sqlalchemy(DBInterface):
    def __init__(self,engine):
        self.engine=engine
        
        self.Session = sessionmaker(bind=engine)
    def registerNewUser(self, name, email, password,gender,role):
        db_session = self.Session()
        new_user = User(name=name, email=email, password=password,gender=gender,role=role)
       
        try:
            db_session.add(new_user)
            db_session.commit()
            return new_user.id
        except Exception as e:
            db_session.rollback()
            print("Error:", e)
        
        finally:
            db_session.close()
            
    def get_user(self,email):
        try:
            db_session=self.Session()
            user= db_session.query(User).filter(User.email == email).first()
            return user
        finally:
         db_session.close()
 
    def getUser_by_id(self,userId):
        db_session=self.Session()
        try:
            user=db_session.query(User).filter(User.id==userId).all()
            return user
        finally:
            db_session.close()
    def add_course(self,title,author,description): 
        db_session=self.Session()
        newCourse = Course(title=title,author=author,description=description)
        try:
            db_session.add(newCourse)
            db_session.commit()
            return newCourse
            print(f"{newCourse} :courseID")
        
        except Exception as e:
            db_session.rollback()
            print("Error:", e)
            
        finally:
            
            db_session.close()
        
    
    def fetch_courses(self):
        db_session = self.Session()
        try:
            courses = db_session.query(Course).all()
            return courses
           
        finally:
            db_session.close()
        
    def search_courses(self,search):
        session = self.Session()
        try:
            searched_course = session.query(Course).filter(Course.title.ilike(f"%{search}%")).all()
            return searched_course
        finally:
            session.close()
        
    def add_lecture(self, title, description,video_url):
        db_session=self.Session()
        lecture = Lecture(title= title,description=description,video_url=video_url)
        try:
            db_session.add(lecture)
            db_session.commit()
            return lecture
        except Exception as e:
            db_session.rollback()
            print("Error:", e)
            
        finally:
            db_session.close()
            
    def fetch_lectures(self):
        db_session = self.Session()
        try:
             lectures = db_session.query(Lecture).all()
             return lectures
        finally:
            db_session.close()
    def  search_lec(self,search):
        db_session = self.Session()
        try:
            searched_lecture = db_session.query(Lecture).filter(Lecture.title.ilike(f"%{search}%")).all()
            return searched_lecture
        finally:
             db_session.close()