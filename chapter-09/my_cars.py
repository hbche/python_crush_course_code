# 导入整个模块
from car import Car
from electric_car import ElectricCar

my_car = Car('audi', 'a4', 2024)
print(my_car.get_descriptive_name())
my_electric_car = ElectricCar('Nissan', 'leaf', 2024)
print(my_electric_car.get_descriptive_name())