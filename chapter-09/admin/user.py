class User:
    """模拟用户信息"""


    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    
    def full_name(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.title()