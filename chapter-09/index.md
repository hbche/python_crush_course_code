## 第九章 类

在面向对象编程中，我们编写表示现实世界中的事物和情景的类(class)，并基于这些类来
创建对象(object)。在编写类时，我们要定义一批对象都具备的通用行为。在基于类创建对
象时，每个对象都自动具备这种通用行为。

### 9.1 创建和使用类

#### 9.1.1 声明 Dog 类

```python dog.py
class Dog:
    """一次模拟小狗的简单尝试"""


    def __init__(self, name, age):
        self.name = name
        self.age = age


    def sit(self):
        """模拟小狗收到命令时坐下"""
        print(f"{self.name} now is sitting.")


    def roll_over(self):
        """模拟小狗打滚"""
        print(f"{self.name} rolled over!")
```

类中的函数称为 **方法**。

1. **init**()方法: `__init__()`方法是一个特殊的方法，每当我们根据 Dog 类创建新实
   例时，Python 都会自动运行它。在这个方法的名称中，开头和结尾各有两个下划线，这
   是一种约定，旨在避免 Python 默认方法和普通方法存在名称冲突。
2.

#### 9.1.2 根据类创建实例

```python
my_dog = Dog('Alice', 3)
print(f"My dog's name is {my_dog.name}")
print(f"My dog's age is {my_dog.age}")
```

1. 访问属性

   要访问实例的属性，可使用点号。

2. 调用方法

   使用点好访问类实例上的任何方法。

3. 创建多个实例

   可按需求根据类创建任意数量的实例。

#### 9.1.3 动手试一试

```python
# 练习9.1：餐馆　创建一个名为Restaurant的类，为其__init__()方法设置两个属性：restaurant_name和cuisine_type。
# 创建一个名为describe_restaurant()的方法和一个名为open_restaurant()的方法，其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。
# 根据这个类创建一个名为restaurant的实例，分别打印其两个属性，再调用前述两个方法。

# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type


#     def describe_restaurant(self):
#         print(f"{self.restaurant_name} is {self.cuisine_type}")


#     def open_restaurant(self):
#         print(f"Restaurant is open now.")


# restaurant = Restaurant('Beijing Big Restaurant', 'Chinses food')
# print(f"The name of restaurant is: {restaurant.restaurant_name}, cuisine type is {restaurant.cuisine_type}.")
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# 练习9.2：三家餐馆　根据为练习9.1编写的类创建三个实例，并对每个实例调用describe_restaurant()方法。

# restaurant_01 = Restaurant('黄鹤楼酒店', '湖北菜')
# restaurant_02 = Restaurant('成都大酒店', '川菜')
# restaurant_03 = Restaurant('山东大酒店', '鲁菜')
# restaurant_01.describe_restaurant()
# restaurant_02.describe_restaurant()
# restaurant_03.describe_restaurant()

# 练习9.3：用户　创建一个名为User的类，其中包含属性first_name和last_name，还有用户简介中通常会有的其他几个属性。
# 在类User中定义一个名为describe_user()的方法，用于打印用户信息摘要。
# 再定义一个名为greet_user()的方法，用于向用户发出个性化的问候。
# 创建多个表示不同用户的实例，并对每个实例调用上述两个方法。
class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


    def describe_user(self):
        print(f"Fullname is {self.first_name.title()} {self.last_name.title()}.")


    def greet_user(self):
        print(f"Hello, {self.first_name}!")


user_01 = User('Lucy', 'Green')
user_01.describe_user()
user_02 = User('Sam', 'Alt')
user_02.describe_user()
```

### 9.2 使用类和实例

既可以直接修改实例的属性，也可以编写函数修改实例属性。

#### 9.2.1 Car 类

```python car.py
class Car:
    """一次模拟汽车的简单尝试"""


    def __init__(self, make, model, year):
        """初始化描述汽车的属性， 制造商、型号、生产年份"""
        self.make = make
        self.model = model
        self.year = year


    def get_descriptive_name(self):
        """返回格式规范的描述信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
```

#### 9.2.2 给属性指定默认值

有些属性无需通过参数来定义，可以在 `__init__()` 方法中为其指定默认值。

```python
class Car:
    """一次模拟汽车的简单尝试"""


    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        # 新增里程参数，并指定默认值为 0
        self.odometer_reading = 0


    def get_descriptive_name(self):
        """返回格式规范的描述信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name


    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")


my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
```

#### 9.2.3 修改属性的值

可以使用三种不同的方式修改属性值：直接通过实例修改，通过方法设置，以及通过方法递
增(增加特定的值)。

1. 直接修改属性值

   ```python
   class Car:
   --skip--

   my_new_car = Car('audi', 'a4', 2024)
   print(my_new_car.get_descriptive_name())

   my_new_car.odometer_reading = 23
   my_new_car.read_odometer()
   ```

2. 通过方法修改属性的值

   ```python
   class Car:
   """一次模拟汽车的简单尝试"""


   def __init__(self, make, model, year):
       """初始化描述汽车的属性"""
       self.make = make
       self.model = model
       self.year = year
       # 里程
       self.odometer_reading = 0


   def get_descriptive_name(self):
       """返回格式规范的描述信息"""
       long_name = f"{self.year} {self.make} {self.model}"
        return long_name

   def read_odometer(self):
       """打印一条指出汽车行驶里程的消息"""
       print(f"This car has {self.odometer_reading} miles on it.")


   def update_odometer(self, mileage):
       """将里程表读数设置为指定的值，禁止将里程数往回调"""
       if mileage >= self.odometer_reading:
           self.odometer_reading = mileage
       else:
           print("You can't roll back an odometer!")

   my_new_car = Car('audi', 'a4', 2024)
   print(my_new_car.get_descriptive_name())
   my_new_car.read_odometer()
   my_new_car.update_odometer(200)
   my_new_car.read_odometer()
   ```

3. 通过方法让属性值递增

   ```python
   class Car:
   """一次模拟汽车的简单尝试"""


   def __init__(self, make, model, year):
       """初始化描述汽车的属性"""
       self.make = make
       self.model = model
       self.year = year
       # 里程
       self.odometer_reading = 0


   def get_descriptive_name(self):
       """返回格式规范的描述信息"""
       long_name = f"{self.year} {self.make} {self.model}"
       return long_name


   def read_odometer(self):
       """打印一条指出汽车行驶里程的消息"""
       print(f"This car has {self.odometer_reading} miles on it.")


   def update_odometer(self, mileage):
       """将里程表读数设置为指定的值，禁止将里程数往回调"""
       if mileage >= self.odometer_reading:
           self.odometer_reading = mileage
       else:
           print("You can't roll back an odometer!")


   def increase_odometer(self, miles):
       """让里程表读数增加指定的量"""
       if miles > 0:
           self.odometer_reading += miles
       else:
           print("You can't roll back an odometer!")
   ```

#### 9.2.4 动手试一试

```python
# 练习9.4：就餐人数　在为练习9.1编写的程序中，添加一个名为number_served的属性，并将其默认值设置为0。
# 根据这个类创建一个名为restaurant的实例。
# 打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印。
# 添加一个名为set_number_served()的方法，用来设置就餐人数。
# 调用这个方法并向它传递新的就餐人数，然后再次打印这个值。
# 添加一个名为increment_number_served()的方法，用来让就餐人数递增。
# 调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。

# class Restaurant:
#     """模拟一个餐厅"""


#     def __init__(self, restaurant_name, cuisine_type, desc):
#         """初始化餐厅属性，餐厅名称、烹饪风格、desc"""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.desc = desc
#         # 就餐人数，默认为 0
#         self.number_served =  0


#     def get_restaurant_desc(self):
#         print(f"{self.restaurant_name.title()} is {self.cuisine_type} reataurant.")
#         print(f"{self.desc}")


#     def describe_number_served(self):
#         """打印在这个餐厅就餐过的人数"""
#         print(f"This restaurant has served {self.number_served} customers.")


#     def set_number_served(self, number_served):
#         """更新就餐历史人数"""
#         if number_served >= self.number_served:
#             self.number_served = number_served
#         else:
#             print("You can't roll back the number served.")


#     def increment_number_served(self, increment_num):
#         if increment_num >= 0:
#             self.number_served += increment_num
#         else:
#             print("You can't roll back the number served.")


# restaurant = Restaurant('Quanjude', 'Chinese Roast Duck Cuisine（中式烤鸭料理）', '全聚德是北京极具代表性的老字号餐厅，创立于1864年，在国内外都享有盛誉。')
# restaurant.get_restaurant_desc()
# restaurant.describe_number_served()
# restaurant.set_number_served(100_000)
# restaurant.describe_number_served()
# restaurant.increment_number_served(100)
# restaurant.describe_number_served()

# 练习9.5：尝试登录次数　在为练习9.3编写的User类中，添加一个名为login_attempts的属性。
# 编写一个名为increment_login_attempts()的方法，用来将属性login_attempts的值加1。
# 再编写一个名为reset_login_attempts()的方法，用来将属性login_attempts的值重置为0。
# 根据User类创建一个实例，再调用increment_login_attempts()方法多次。
# 打印属性login_attempts的值，确认它正确地递增了。
# 然后，调用方法reset_login_attempts()，并再次打印属性login_attempts的值，确认它被重置为0。

class User:
    """模拟用户登录信息"""


    def __init__(self, first_name, last_name, login_attempts):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts


    def describe_login_attempts(self):
        print(f"You have attempted to log in {self.login_attempts} times.")


    def increment_login_attempts(self, login_attempts):
        self.login_attempts = login_attempts


    def reset_login_attempts(self):
        self.login_attempts = 0


user = User('Robin', 'Che', 0)
user.describe_login_attempts()
user.increment_login_attempts(10)
user.describe_login_attempts()
user.reset_login_attempts()
user.describe_login_attempts()
```

### 9.3 继承

在编写类时，并非总是要从头开始。如果要编写的类是一个既有的类的特殊版本，可使用继
承(inheritance)。当一个类继承另一个类时，将自动获得后者的所有属性和方法。原有的
类称为父类(parent class)，而新类称为子类(child class)。子类不仅继承了父类的所有
属性和方法，还可定义自己的属性和方法。

#### 9.3.1 子类的`__init__()`方法

在既有的类的基础上编写新类，通常要调用父类的**init**()方法。这将初始化在父类
的**init**()方法中定义的所有属性，从而让子类也可以使用这些属性。

```python electric_car.py
class Car:
    """模拟一辆汽车"""


    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


    def read_odometer(self):
        """打印一个句子，显示汽车的行驶里程"""
        print(f"The car has {self.odometer_reading} miles on it.")


    def update_odometer(self, miles):
        """将里程表读数设置为指定的值"""
        if miles >= self.odometer_reading:
            self.odometer_reading = miles
        else:
            print("You can't roll back an odometer.")


    def increment_odometer(self, miles):
        """让里程表读数增加给定的值"""
        self.odometer_reading += miles


class ElectricCar(Car):
    """模拟一辆电动汽车"""


    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
```

`super()`是一个特殊的函数，让我们能够调用父类的方法。这行代码让 Python 调用 Car
类的`__init__()`方法，从而让 ElectricCar 实例包含这个方法定义的所有属性。

#### 9.3.2 给子类定义属性和方法

让一个类继承另一个类后，就可以添加区分子类和父类所需的新属性和新方法了。

```python electric_car.py
class Car:
    """模拟一辆汽车"""


    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


    def read_odometer(self):
        """打印一个句子，显示汽车的行驶里程"""
        print(f"The car has {self.odometer_reading} miles on it.")


    def update_odometer(self, miles):
        """将里程表读数设置为指定的值"""
        if miles >= self.odometer_reading:
            self.odometer_reading = miles
        else:
            print("You can't roll back an odometer.")


    def increment_odometer(self, miles):
        """让里程表读数增加给定的值"""
        self.odometer_reading += miles


class ElectricCar(Car):
    """模拟一辆电动汽车"""


    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        # 添加电动汽车特有的属性
        self.battery_size = 40


    def describe_battery(self):
        """打印一条消息，描述电池的容量"""
        print(f"This car has {self.battery_size}-kWh battery.")


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
```

#### 9.3.3 重写父类中的方法

在使用子类模拟的实物的行为时，如果父类中的一些方法不能满足子类的需求，就可以用下
面的办法重写：在子类中定义一个与要重写的父类方法同名的方法。这样，Python 将忽略
这个父类方法，只关注你在子类中定义的相应方法。

假设 Car 类有一个 `fill_gas_tank` 的方法，但是电动汽车不需要油箱。

```python
class Car:
    """模拟一辆汽车"""


    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


    def read_odometer(self):
        """打印一个句子，显示汽车的行驶里程"""
        print(f"The car has {self.odometer_reading} miles on it.")


    def update_odometer(self, miles):
        """将里程表读数设置为指定的值"""
        if miles >= self.odometer_reading:
            self.odometer_reading = miles
        else:
            print("You can't roll back an odometer.")


    def increment_odometer(self, miles):
        """让里程表读数增加给定的值"""
        self.odometer_reading += miles


    def fill_gas_tank(self):
        """汽车有油箱，此处强调加满一箱油"""
        print("This car has a gas tank! Please get a full tank of gas.")


class ElectricCar(Car):
    """模拟一辆电动汽车"""


    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        # 添加电动汽车特有的属性
        self.battery_size = 40


    def describe_battery(self):
        """打印一条消息，描述电池的容量"""
        print(f"This car has {self.battery_size}-kWh battery.")


    def fill_gas_tank(self):
        """重写父类的方法，电动汽车没有油箱"""
        print("This car doesn't have a gas tank!")


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
my_leaf.fill_gas_tank()
```

现在，如果有人对电动汽车调用 `fill_gas_tank()` 方法，Python 将忽略 Car 类中的
`fill_gas_tank()` 方法，转而运行上述代码。在使用继承时，可让子类保留从父类那里继
承的“精华”​，重写不需要的“糟粕”​。

#### 9.3.4 将实例用作属性

在使用代码模拟实物时，你可能会发现自己给类添加了太多细节：属性和方法越来越多，文
件越来越长。在这种情况下，可能需要将类的一部分提取出来，作为一个独立的类。将大型
类拆分成多个协同工作的小类，这种方法称为组合(composition)。

```python electric_car.py
class Car:
    """模拟一辆汽车"""


    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


    def read_odometer(self):
        """打印一个句子，显示汽车的行驶里程"""
        print(f"The car has {self.odometer_reading} miles on it.")


    def update_odometer(self, miles):
        """将里程表读数设置为指定的值"""
        if miles >= self.odometer_reading:
            self.odometer_reading = miles
        else:
            print("You can't roll back an odometer.")


    def increment_odometer(self, miles):
        """让里程表读数增加给定的值"""
        self.odometer_reading += miles


    def fill_gas_tank(self):
        """汽车有油箱，此处强调加满一箱油"""
        print("This car has a gas tank! Please get a full tank of gas.")


class Battery:
    """模拟电动车电池"""


    def __init__(self, battery_size = 40):
        """初始化电池的属性"""
        self.battery_size = battery_size


    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")


class ElectricCar(Car):
    """模拟一辆电动汽车"""


    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        # 添加电动汽车特有的属性
        self.battery = Battery()


    def fill_gas_tank(self):
        """重写父类的方法，电动汽车没有油箱"""
        print("This car doesn't have a gas tank!")


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
```

给 Battery 类新增一个 `get_range()` 方法，打印电量对应的行驶里程。

```python
class Car:
    """模拟一辆汽车"""


    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


    def read_odometer(self):
        """打印一个句子，显示汽车的行驶里程"""
        print(f"The car has {self.odometer_reading} miles on it.")


    def update_odometer(self, miles):
        """将里程表读数设置为指定的值"""
        if miles >= self.odometer_reading:
            self.odometer_reading = miles
        else:
            print("You can't roll back an odometer.")


    def increment_odometer(self, miles):
        """让里程表读数增加给定的值"""
        self.odometer_reading += miles


    def fill_gas_tank(self):
        """汽车有油箱，此处强调加满一箱油"""
        print("This car has a gas tank! Please get a full tank of gas.")


class Battery:
    """模拟电动车电池"""


    def __init__(self, battery_size = 40):
        """初始化电池的属性"""
        self.battery_size = battery_size


    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")


    def get_range(self):
        if self.battery_size == 40:
            range = 150
        if self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """模拟一辆电动汽车"""


    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        # 添加电动汽车特有的属性
        self.battery = Battery()


    def fill_gas_tank(self):
        """重写父类的方法，电动汽车没有油箱"""
        print("This car doesn't have a gas tank!")


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
```

#### 9.3.5 模拟实物

在模拟较复杂的事物（如电动汽车）时，需要思考一些有趣的问题。续航里程是电池的属性
还是汽车的属性呢？如果只描述一辆汽车，将 get_range()方法放在 Battery 类中也许是
合适的，但如果要描述一家汽车制造商的整条产品线，也许应该将 get_range()方法移到
ElectricCar 类中。在这种情况下，get_range()依然根据电池容量来确定续航里程，但报
告的是一款汽车的续航里程。也可以这样做：仍将 get_range()方法留在 Battery 类中，
但向它传递一个参数，如 car_model。此时，get_range()方法将根据电池容量和汽车型号
报告续航里程。这让你进入了程序员的另一个境界：在解决上述问题时，从较高的逻辑层面
（而不是语法层面）思考。你考虑的不是 Python，而是如何使用代码来表示实际事物。达
到这种境界后，你会经常发现，对现实世界的建模方法没有对错之分。有些方法的效率更高
，但要找出效率最高的表示法，需要一定的实践。只要代码能够像你希望的那样运行，就说
明你已经做得很好了！即便发现自己不得不多次尝试使用不同的方法来重写类，也不必气馁
。要编写出高效、准确的代码，这是必经之路。

#### 9.3.6 动手试一试

```python
# 练习9.6：冰激凌小店　冰激凌小店是一种特殊的餐馆。
# 编写一个名为IceCreamStand的类，让它继承你为练习9.1或练习9.4编写的Restaurant类。
# 这两个版本的Restaurant类都可以，挑选你更喜欢的那个即可。
# 添加一个名为flavors的属性，用于存储一个由各种口味的冰激凌组成的列表。
# 编写一个显示这些冰激凌口味的方法。创建一个IceCreamStand实例，并调用这个方法。

# class Restaurant:
#     """模拟一个餐饮店"""


#     def __init__(self, restaurant_name, cuisine_type):
#         """初始化餐饮店的属性"""
#         self.restaurant_name = restaurant_name
#         self.cusine_type = cuisine_type
#         self.number_served = 0

#     def get_number_served(self):
#         print(f"This restaurant served about {self.number_served} people every!")


#     def set_number_served(self, number_served):
#         self.set_number_served = number_served


# class IceCreamStand(Restaurant):

#     def __init__(self, restaurant_name, cuisine_type):
#         super().__init__(restaurant_name, cuisine_type)
#         self.flavors = ['Vanilla', 'Mint Chocolate Chip', 'Tiramisu']


#     def describe_flavors(self):
#         print(f"This ice cream stand has {len(self.flavors)} flavors:")
#         for flavor in self.flavors:
#             print(f"-{flavor}")


# ice_cream_stand = IceCreamStand('Mixue Ice Cream & Tea', 'Fast - food style drinks and desserts')
# ice_cream_stand.describe_flavors()

# 练习9.7：管理员　管理员是一种特殊的用户。
# 编写一个名为Admin的类，让它继承你为练习9.3或练习9.5完成编写的User类。
# 添加一个名为privileges的属性，用来存储一个由字符串（如"can add post"、"can delete post"、"can ban user"等）组成的列表。
# 编写一个名为show_privileges()的方法，显示管理员的权限。
# 创建一个Admin实例，并调用这个方法。

# class User:
#     """模拟一个用户类"""

#     def __init__(self, first_name, last_name):
#         """初始化用户信息"""
#         self.first_name = first_name
#         self.last_name = last_name


#     def get_full_name(self):
#         """打印一条消息展示用户全名"""
#         return f"{self.first_name} {self.last_name}"


# class Admin(User):
#     """模拟管理员用户"""


#     def __init__(self, first_name, last_name):
#         """初始化用户和管理员用户属性"""
#         super().__init__(first_name, last_name)
#         self.privileges = ['can add post', 'can delete post', 'can ban user']


#     def show_privileges(self):
#         """打印一条消息展示管理员用户拥有的权限"""
#         print(f"{self.get_full_name()} have some privileges:")
#         for privilege in self.privileges:
#             print(f"-{privilege}")


# admin = Admin('Robin', 'Che')
# admin.show_privileges()

# 练习9.8：权限　编写一个名为Privileges的类，它只有一个属性privileges，其中存储了练习9.7所述的字符串列表。
# 将方法show_privileges()移到这个类中。
# 在Admin类中，将一个Privileges实例用作其属性。
# 创建一个Admin实例，并使用方法show_privileges()来显示权限。
# class User:
#     """模拟一个用户类"""

#     def __init__(self, first_name, last_name):
#         """初始化用户信息"""
#         self.first_name = first_name
#         self.last_name = last_name


#     def get_full_name(self):
#         """打印一条消息展示用户全名"""
#         return f"{self.first_name} {self.last_name}"


# class Admin(User):
#     """模拟管理员用户"""


#     def __init__(self, first_name, last_name):
#         """初始化用户和管理员用户属性"""
#         super().__init__(first_name, last_name)
#         self.privileges = Privileges()

# class Privileges:
#     """模拟权限"""


#     def __init__(self):
#         """初始化权限信息"""
#         self.privileges = ['can add post', 'can delete post', 'can ban user']


#     def show_privileges(self):
#         print("Privileges: ")
#         for privilege in self.privileges:
#             print(f"-{privilege}")


# admin = Admin('Robin', 'Che')
# admin.privileges.show_privileges()

# 练习9.9：电池升级　在本节最后一个electric_car.py版本中，给Battery类添加一个名为upgrade_battery()的方法。
# 这个方法检查电池容量，如果电池容量不足65，就设置为65。
# 创建一辆电池容量为默认值的电动汽车，调用方法get_range()，然后对电池进行升级，并再次调用get_range()。
# 你将看到这辆汽车的续航里程增加了。

class Battery:

    def __init__(self, battery_size=40):
        self.battery_size = battery_size


    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65


    def get_range(self):
        if self.battery_size == 40:
            range = 150
        if self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")

class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

class ElectricCar(Car):


    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

electric_car = ElectricCar('audi', 'a4', 2024)
electric_car.battery.get_range()
electric_car.battery.upgrade_battery()
electric_car.battery.get_range()
```

### 9.4 导入类

Python 允许我们将类声明在模块中，然后在主程序中导入所需的模块。

#### 9.4.1 导入单个类

将 Car 类的声明抽取到 car.py 模块中，我们在给使用 Car 类的程序单独声明一个
my_car.py 的文件，并在 my_car.py 中导入 car 模块中的 Car 类：

```python car.py
class Car:
    """一次模拟汽车的简单尝试"""


    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        # 里程
        self.odometer_reading = 0


    def get_descriptive_name(self):
        """返回格式规范的描述信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name


    def read_odometer(self):
        """打印一条指出汽车行驶里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")


    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值，禁止将里程数往回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


    def increase_odometer(self, miles):
        """让里程表读数增加指定的量"""
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")
```

```python my_car.py
from car import Car

my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
# my_new_car.odometer_reading = 23
# my_new_car.update_odometer(100)
my_new_car.increase_odometer(10)
my_new_car.read_odometer()
```

import 语句让 Python 打开模块 car 并导入其中的 Car 类。这样我们就可以使用 Car 类
了。

#### 9.4.2 在一个模块中存储多个类

尽管同一个模块中的类之间应该存在某种相关性，但其实可以根据需要在一个模块中存储任
意数量的类。

```python car.py
"""一组用于表示燃油汽车和电动汽车的类"""

class Car:
    """一次模拟燃油汽车的简单尝试"""


    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        # 里程
        self.odometer_reading = 0


    def get_descriptive_name(self):
        """返回格式规范的描述信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name


    def read_odometer(self):
        """打印一条指出汽车行驶里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")


    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值，禁止将里程数往回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


    def increase_odometer(self, miles):
        """让里程表读数增加指定的量"""
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")



class Battery:
    """一次模拟电池的简单尝试"""


    def __init__(self, battery_size=40):
        """初始化电池的信息"""
        self.battery_size = battery_size


    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"The car has {self.battery_size}-kWh battery.")


    def get_range(self):
        """打印一条描述电池续航里程的消息"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 60:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """一次对电动汽车的简单模拟"""


    def __init__(self, make, model, year):
        """先初始化父类的属性，再初始化电动汽车特有的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()
```

新建 my_electric_car.py 程序，并在该程序中从 car 模块中导入 ElectricCar 类。

```python
from car import ElectricCar

my_electric_car = ElectricCar('Nissan', 'leaf', 2024)
print(my_electric_car.get_descriptive_name())
my_electric_car.battery.describe_battery()
my_electric_car.battery.get_range()
```

#### 9.4.3 从一个模块中导入多个类

可以根据需要在程序文件中导入任意数量的类。

```python my_cars.py
from car import Car, ElectricCar

my_car = Car('audi', 'a4', 2024)
print(my_car.get_descriptive_name())
my_electric_car = ElectricCar('Nissan', 'leaf', 2024)
print(my_electric_car.get_descriptive_name())
```

当从一个模块中导入多个类时，用逗号分隔各个类。导入必要的类后，就可根据需要创建每
个类的任意数量的实例了。

#### 9.4.4 导入整个模块

还可以先导入整个模块，再使用点号访问需要的类。这种导入方法很简单，代码也易读。由
于创建类实例的代码都包含模块名，因此不会与当前文件使用的任何名称发生冲突。

```python my_cars.py
# 导入整个模块
import car

my_car = car.Car('audi', 'a4', 2024)
print(my_car.get_descriptive_name())
my_electric_car = car.ElectricCar('Nissan', 'leaf', 2024)
print(my_electric_car.get_descriptive_name())
```

首先，导入整个 car 模块 ​。接下来，使用语法 module_name.classname 访问需要的类。

#### 9.4.5 导入模块中的所有类

要导入模块中的每个类，可使用下面的语法：

```python
from module_name import *
```

不推荐这种导入方式，原因有二。第一，最好只需要看一下文件开头的 import 语句，就能
清楚地知道程序使用了哪些类。但这种导入方式没有明确地指出使用了模块中的哪些类。第
二，这种导入方式还可能引发名称方面的迷惑。如果不小心导入了一个与程序文件中的其他
东西同名的类，将引发难以诊断的错误。这里之所以介绍这种导入方式，是因为虽然不推荐
，但你可能在别人编写的代码中见到它。

当需要从一个模块中导入很多类时，还是最好在导入整个模块之后使用
module_name.classname 语法来访问这些类。这样，虽然文件开头并没有列出用到的所有类
，但是你清楚地知道在程序的哪些地方使用了导入的模块。此外，这还避免了导入模块中的
每个类可能引发的名称冲突。

#### 9.4.6 在一个模块中导入另一个模块

有时候，需要将类分散到多个模块中，以免模块太大或者在同一个模块中存储不相关的类。
在将类存储在多个模块中时，你可能会发现一个模块中的类依赖于另一个模块中的类。在这
种情况下，可在前一个模块中导入必要的类。

```python car.py
class Car:
    """一次模拟燃油汽车的简单尝试"""


    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        # 里程
        self.odometer_reading = 0


    def get_descriptive_name(self):
        """返回格式规范的描述信息"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name


    def read_odometer(self):
        """打印一条指出汽车行驶里程的消息"""
        print(f"This car has {self.odometer_reading} miles on it.")


    def update_odometer(self, mileage):
        """将里程表读数设置为指定的值，禁止将里程数往回调"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


    def increase_odometer(self, miles):
        """让里程表读数增加指定的量"""
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")



class Battery:
    """一次模拟电池的简单尝试"""


    def __init__(self, battery_size=40):
        """初始化电池的信息"""
        self.battery_size = battery_size


    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"The car has {self.battery_size}-kWh battery.")


    def get_range(self):
        """打印一条描述电池续航里程的消息"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 60:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """一次对电动汽车的简单模拟"""


    def __init__(self, make, model, year):
        """先初始化父类的属性，再初始化电动汽车特有的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()
```

```python electric_car.py
# 从 car 模块中导入 Car 类
from car import Car

class Battery:
    """模拟电动车电池"""


    def __init__(self, battery_size = 40):
        """初始化电池的属性"""
        self.battery_size = battery_size


    def describe_battery(self):
        """打印一条描述电池容量的消息"""
        print(f"This car has a {self.battery_size}-kWh battery.")


    def get_range(self):
        if self.battery_size == 40:
            range = 150
        if self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """模拟一辆电动汽车"""


    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        # 添加电动汽车特有的属性
        self.battery = Battery()


    def fill_gas_tank(self):
        """重写父类的方法，电动汽车没有油箱"""
        print("This car doesn't have a gas tank!")
```

```python my_cars.py
# 导入整个模块
from car import Car
from electric_car import ElectricCar

my_car = Car('audi', 'a4', 2024)
print(my_car.get_descriptive_name())
my_electric_car = ElectricCar('Nissan', 'leaf', 2024)
print(my_electric_car.get_descriptive_name())
```

#### 9.4.7 使用别名

第 8 章说过，当使用模块来组织项目代码时，别名能发挥很大的作用。在导入类时，也可
以给它指定别名。

```python
from electric_car import ElectricCar as EC

my_leaf = EC('Nissan', 'leaf', 2024)
```

还可以给模块指定别名。

```python
import electric_car as ec

my_leaf = ec.ElectricCar('Nissan', 'leaf', 2024)
```

#### 9.4.8 找到合适的工作流程

如你所见，在组织大型项目的代码方面，Python 提供了很多选项。熟悉所有这些选项很重
要，这样才能确定哪种项目组织方式是最佳的，才能理解别人开发的项目。

一开始应让代码结构尽量简单。首先尝试在一个文件中完成所有的工作，确定一切都能正确
运行后，再将类移到独立的模块中。如果你喜欢模块和文件的交互方式，可在项目开始时就
尝试将类存储到模块中。先找出让你能够编写出可行代码的方式，再尝试让代码更加整洁。

#### 9.4.9 动手试一试

练习 9.10：导入 Restaurant 类　将最新的 Restaurant 类存储在一个模块中。
在另一个文件中导入 Restaurant 类，创建一个 Restaurant 实例，并调用 Restaurant 的一个方法，以确认 import 语句正确无误。

练习 9.11：导入 Admin 类　以为完成练习 9.8 而做的工作为基础。
将 User 类、Privileges 类和 Admin 类存储在一个模块中，再创建一个文件，在其中创建一个 Admin 实例并对其调用 show_privileges()方法，以确认一切都能正确地运行。

练习 9.12：多个模块　将 User 类存储在一个模块中，并将 Privileges 类和 Admin 类存储在另一个模块中。
再创建一个文件，在其中创建一个 Admin 实例并对其调用 show_privileges()方法，以确认一切依然能够正确地运行。

### 9.5 Python 标准库

Python 标准库是一组模块，在安装 Python 时已经包含在内。我们可以使用标准库中的任何函数和类，只需在程序开头添加一条简单的
import 语句即可。

`randint()` 函数接收两个整数作为参数，并随机返回一个位于这两个整数之间(包含)的整数。

```python
from random import randint

print(randint(1, 100))
```

`choice` 是 `random` 模块中的另一个方法，用于在列表或元组中随机选择一项作为返回值

```python
from random import choice

result1 = choice(('Watermelon', 'Mango', 'Pineapple', 'Lychee', 'Longan', 'Peach'))
print(result1)
result2 = choice(['Watermelon', 'Mango', 'Pineapple', 'Lychee', 'Longan', 'Peach'])
print(result2)
```

#### 9.5.1 动手试一试

练习 9.13：骰子　创建一个 Die 类，它包含一个名为 sides 的属性，该属性的默认值为 6。编写一个名为 roll_die()的方法，它打印位于 1 和骰子面数之间的随机数。创建一个 6 面的骰子并掷 10 次。
创建一个 10 面的骰子和一个 20 面的骰子，再分别掷 10 次。

```python

# 练习 9.13：骰子　创建一个 Die 类，它包含一个名为 sides 的属性，该属性的默认值为 6。
# 编写一个名为 roll_die()的方法，它打印位于 1 和骰子面数之间的随机数。
# 创建一个 6 面的骰子并掷 10 次。
# 创建一个 10 面的骰子和一个 20 面的骰子，再分别掷 10 次。
from random import randint

class Die:
    """模拟骰子"""


    def __init__(self, sides = 6):
        self.sides = sides


    def roll_die(self):
        """根据当前骰子的面数进行掷骰子"""
        print(f"Current side is {randint(1, self.sides)}.")

die_0 = Die(6)
die_1 = Die(10)
die_2 = Die(20)
def roll_dies(die):
    """掷指定轮数的骰子"""
    print(f"\nAre you ready? I'm going to roll an {die.sides}-sided die {10} times.")
    for i in range(0, 10):
        die.roll_die()

roll_dies(die_0)
roll_dies(die_1)
roll_dies(die_2)
```

练习 9.14：彩票　创建一个列表或元素，其中包含 10 个数和 5 个字母。
从这个列表或元组中随机选择 4 个数或字母，并打印一条消息，指出只要彩票上是这 4 个数或字母，就中大奖了。
练习 9.15：彩票分析　可以使用一个循环来理解中前述彩票大奖有多难。
为此，创建一个名为 my_ticket 的列表或元组，再编写一个循环，不断地随机选择数或字母，直到中大奖为止。
请打印一条消息，报告执行多少次循环才中了大奖。

```python
from random import choice

char_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e']

# 中奖码
winning_num = []
for i in range(0, 4):
    winning_num.append(choice(char_list))

print(f"Winning number is {winning_num}")

def draw_numbers(char_list):
    """模拟抽奖"""
    result = []
    for i in range(0, 4):
        result.append(choice(char_list))
    equal = True

    for i in range(0, 4):
        if result[i] != winning_num[i]:
            equal = False

    return equal

def total_draw():
    count = 0
    is_won = False
    while not is_won:
        is_won = draw_numbers(char_list)
        count += 1
        if is_won:
            print("Wow, congratulations on your big win!")
        else:
            print("We regret to announce that your numbers didn't match the winning combination.")

    return count

print(f"You have draw {total_draw()} count.")
```

练习 9.16: Python 3 Module of the Week 　要了解 Python 标准库，一个很不错的资源是网站 Python 3 Module of the Week。请访问该网站并查看其中的目录，找一个你感兴趣的模块进行探索，从模块 random 开始可能是个不错的选择。

### 9.6 类的编程风格

类名应采用驼峰命名法，即将类名中的每个单词的首字母都大写，并且不使用下划线。实例名和模块名都采用全小写格式，并在单词之间加上下划线。

对于每个类，都应在类定义后面紧跟一个文档字符串。这种文档字符串简要地描述类的功能，你应该遵循编写函数的文档字符串时采用的格式约定。每个模块也都应包含一个文档字符串，对其中的类可用来做什么进行描述。

可以使用空行来组织代码，但不宜过多。在类中，可以使用一个空行来分隔方法；而在模块中，可以使用两个空行来分隔类。

当需要同时导入标准库中的模块和你编写的模块时，先编写导入标准库模块的 import 语句，再添加一个空行，然后编写导入你自己编写的模块的 import 语句。在包含多条 import 语句的程序中，这种做法让人更容易明白程序使用的各个模块来自哪里。
