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
        
my_dog = Dog('Alice', 3)
print(f"My dog's name is {my_dog.name}")
print(f"My dog's age is {my_dog.age}")
# my_dog.sit()
# my_dog.roll_over()