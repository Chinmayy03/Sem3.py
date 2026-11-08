class Car:
    def __init__(self, make, model, year , color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def details(self):
        print("This "+self.make+" "+self.model+" was manufactured in "+self.year+" and the color is "+self.color)