class Car:
    def __init__(self, manf, model, make, trans, color):
        self.manf =manf
        self.model =model
        self.make =make
        self.trans =trans
        self.color =color
	
    def accelerate(self):
        print(self.manf + " " + self.model + " Started")

    def stop(self):
        print(self.manf + " " + self.model + " Stopped")

car1 = Car("Porsche", "911", "2019", "Auto", "yellow")	
car2 = Car("Audi", "Q8", "2017", "Auto", "White")	
car3 = Car("Toyota", "Fortuner", "2016", "Auto", "Brown")	
car1.accelerate()	
car1.stop()