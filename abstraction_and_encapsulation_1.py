from abc import ABC,abstractmethod
class car(ABC):
    @abstractmethod
    def mileage(self):
        pass
    

class audi(car):
    def mileage(self):
        print("90kmph")


class tesla(car):
    def mileage(self):
        print("120kmph")


a1=audi()
a1.mileage()
t1=tesla()
t1.mileage()
#c1=car()
#c1.mileage() #Can't instantiate abstract class car with abstract method mileage
#so we cannot create an object
