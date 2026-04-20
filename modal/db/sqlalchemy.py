from abc import abstractmethod
from sqlalchemy.orm import Session, sessionmaker

from db_modal.database import engine,Base
from db_modal.user_db_modal import User,Course
#import DBInterface from modal.db.db_interface
from modal.db_interface import DBInterface
from sqlalchemy.orm import sessionmaker
class Sqlalchemy(DBInterface):
    def __init__(self,engine):
        self.engine=engine
        
    def registerNewUser(self, name, email, password,gender,role):
        Session = sessionmaker(bind=engine)
        session = Session()
        new_user = User(name=name, email=email, password=password,gender=gender,role=role)
       
        try:
            session.add(new_user)
            session.commit()
            return new_user.id
        except Exception as e:
            session.rollback()
            print("Error:", e)
        
        finally:
            session.close()
            
    def get_user(self,email):
        session=sessionmaker(bind=engine)
        session=session()
        user= session.query(User).filter(User.email == email).first()
        return user
        session.commit()
        session.close()
        
        
        
    def add_course(self,title,author,description):
        session = sessionmaker(bind=engine) 
        self.session=session()
        newCourse = Course(title=title,author=author,description=description)
        try:
            session.add(newCourse)
            session.commit()
            return newCourse
        
        except Exception as e:
            session.rollback()
            print("Error:", e)
            
        finally:
            session.close()
        
    
    def get_course(self):
        pass
  