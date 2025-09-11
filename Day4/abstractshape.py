from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class rectangle:
    def area(self,length,breadth):
        return length*breadth
class circle:
    def area(self,rad):
        return 3.14*rad*rad