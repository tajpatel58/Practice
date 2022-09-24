class Vehicle:
    def __init__(self, colour: str, brand : str, top_speed : int):
        self.colour = colour
        self.brand = brand
        self.top_speed = top_speed
    

    def remap_speed(self, stage):
        self.top_speed = self.top_speed + 15 * stage
    

    def __repr__(self):
        attribute_dictionary = {'Colour' : self.colour, 'Brand' : self.brand, 'Top Speed' : self.top_speed}
        return str(attribute_dictionary)

    def __len__(self):
        return 10

class Cars(Vehicle):
    def __init__(self, colour, brand, top_speed, num_wheels):
        super().__init__(colour, brand, top_speed)
        self.num_wheels = num_wheels


a = Cars('Black', 'BMW', 150, 4)

print(a)
