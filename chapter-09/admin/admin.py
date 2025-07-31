from user import User


class Privilege:
    """模拟权限信息"""


    def __init__(self):
        self.privileges = ['can login', 'can add user', 'can ban user']

    
    def show_privileges(self):
        """打印用户权限列表"""
        print("You have some privileges:")
        for privilege in self.privileges:
            print(f"-{privilege}")


class Admin(User):
    """模拟管理员"""


    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privilege()