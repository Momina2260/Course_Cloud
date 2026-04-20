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
    def add_course(self):
        pass
    
    @abstractmethod
    def fetch_courses(self):
        pass