# # 位置参数
# def describe_pet(animal_type, pet_name):
#     """打印宠物种类及名称"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# describe_pet('dog', 'cola')
# describe_pet('hamster', 'harry')

# def describe_pet(animal_type, pet_name):
#     """打印宠物的种类和名称"""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
# # 关键字参数
# describe_pet(pet_name='cola', animal_type='dog')

# 默认值，具有默认值的参数只能放在参数列表的后面
def describe_pet(pet_name, animal_type = 'dog'):
    """描述宠物"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('willie')
describe_pet(pet_name='harry', animal_type='hamster') # 仓鼠