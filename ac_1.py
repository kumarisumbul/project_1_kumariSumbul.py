from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def tyres(self):
        pass

    @abstractmethod
    def rear_view_mirror(self):
        pass

class MarutiSuzukiCar(Car):

    def tyres(self):
        print("this is maruti tyres")

    def rear_view_mirror(self):
        print("this is maruti mirror")


class BMWCar(Car):

    def tyres(self):
        print("this is BMW tyre")

    def rear_view_mirror(self):
        print("this is BMW mirror")


mycar = MarutiSuzukiCar()
mycar.tyres()
mycar.rear_view_mirror()
mysecondcar = BMWCar()
mysecondcar.tyres()
mysecondcar.rear_view_mirror()