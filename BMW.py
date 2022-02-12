class Car:
    def __init__(brand, Name, Color, Body, Number_of_doors, Fuel_Type ):
        brand.Name = Name
        brand.color = Color
        brand.Body = Body
        brand.Number_of_doors = Number_of_doors
        brand.Fuel_type = Fuel_Type

    def Car_Warning(brand):
        print('my' + brand.Name +"is reversing, please beware")

Owner1= Car('BMW','Black','Steel',4, 'Diesel')

Owner1.Name= "Range Rover"
del Owner1.Fuel_type

Owner1.Car_Warning()





