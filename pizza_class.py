import re

class Pizza:
    def __init__(self, toppings_dict, size, crust_type):
        self.pizza_dict = toppings_dict
        self.pizza_dict['Size'] = size 
        self.pizza_dict['Crust_Type'] = crust_type


default_topping_count = {'Jalapenos' : 20, 'Mushroom' : 20, 'Chicken' : 1}

toppings_input = input('Enter Toppings: ')
size = input('Enter Pizza Size: ')
crust = input('Enter Crust Type: ')

pattern = "[A-Za-z]+"

regex_pattern = re.compile(pattern)

toppings_list = regex_pattern.findall(toppings_input)

toppings_dict = {topping:default_topping_count[topping] for topping in toppings_list}

my_pizza = Pizza(toppings_dict, size, crust)