from restaurant import Restaurant

class BreakfastRestaurant(Restaurant):
    """模拟一家早餐店"""
    
    
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.number_served = 0