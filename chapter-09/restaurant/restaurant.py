class Restaurant:
    """模拟一家餐饮店"""
    
    
    def __init__(self, restaurant_name, cuisine_type):
        """初始化餐饮店的名称和风味"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    
    def get_descriptive_name(self):
        """返回一句描述这家餐饮店名称、饮食特色的消息"""
        # 这里有一家餐饮店，店名是蔡明纬，它的风格是Hubei cuisine。
        long_name = f"There is a restaurant, it's name is {self.restaurant_name} and it's cuisine type is {self.cuisine_type}"
        return long_name