pizza = {
    # 
    'crust': 'thick',
    # 配料: 蘑菇、外加奶酪
    'toppings': ['mushrooms', 'extra cheese']
}
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppins:")
for topping in pizza['toppings']:
    print(f"\t{topping.title()}")