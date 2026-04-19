from abc import ABC, abstractmethod
@abstractmethod
class DBInterface(ABC):
    @abstractmethod
    def registerNewUser(self, name, email, password , gender ,role):
        pass

   
    def get_user(email):
        pass