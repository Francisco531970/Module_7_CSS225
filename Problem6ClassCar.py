# Francisco Sanchez
# 11/09/23

class car:
    def __init__(self, model, year, color, car_type, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.type = car_type  # New attribute
        self.manufacturer = manufacturer  # New attribute

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_type(self):  # New method
        return self.type

    def get_manufacturer(self):  # New method
        return self.manufacturer

    def fullspecs(self):
        return f"{self.manufacturer} {self.model} {str(self.year)} {self.color} {self.type}"

# Creating instances of the Car class
car1 = car("Sports", 2012, "Blue", "Convertible", "XYZ Motors")
car2 = car("Sedan", 2020, "Black", "Sedan", "ABC Cars")

# Printing attribute values using methods
print(car1.get_color())
print(car1.get_model())
print(car1.get_type())  # New line
print(car1.get_manufacturer())  # New line

# Printing full specifications including the new attributes
print(car1.fullspecs())
print(car2.fullspecs())