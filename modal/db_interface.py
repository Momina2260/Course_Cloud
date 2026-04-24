from abc import ABC, abstractmethod
@abstractmethod
class DBInterface(ABC):
    @abstractmethod
    def registerNewUser(self, name, email, password , gender ,role):
        pass

    @abstractmethod
    def get_user(self,email):
        pass
    
    @abstractmethod
    def add_course(self,title,author,description):
        pass
    
    @abstractmethod
    def fetch_courses(self):
        pass
    
    @abstractmethod
    def search_courses(self,search):
        pass
    @abstractmethod
    def add_lecture(self,title,description,video_url):
        pass
    
    @abstractmethod
    def fetch_lectures(self):
        pass
    @abstractmethod
    def search_lec(self,search):
        pass