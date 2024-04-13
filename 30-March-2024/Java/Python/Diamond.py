class Vehicle:
    def drive(self):
        print("In the  Vehicle")


class Car(Vehicle):
    def drive(self):
        print("In the Car")
        super().drive()

class Helicopter(Vehicle):
    def drive(self):
        print("In the Helicopter")
        super().drive()


#Method is being inherited from both of the classes below
class FlyingCar(Car,Helicopter):
    def drive(self):
        print("In the Flying Car")
        super().drive()



if __name__ == "__main__":
    fly=FlyingCar()
    fly.drive()

    #Mro -defines in the method clears all the doubt regarding the Diamond Problem
    # It is determjned by the C3 linearlisation algorithm 
#     Python's Guido van Rossum summarizes C3 superclass linearisation thus:[11]

# Basically, the idea behind C3 is that if you write down all of the ordering rules imposed by inheritance relationships in a complex class hierarchy, the algorithm will determine a monotonic ordering of the classes that satisfies all of them. 
# If such an ordering can not be determined, the algorithm will fail.

    print(FlyingCar.mro())
    print(FlyingCar.__mro__)