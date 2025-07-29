# def make_pizza(*toppings):
#     """打印顾客点的所有配料"""
#     print(toppings)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 任意数量的实参
# def make_pizza(*toppings):
#     """概述只做pizza的配料"""
#     print("\nMaking a pizza with the following toppings:")
#     for topping in toppings:
#         print(f"- {topping}")

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 结合使用位置参数和任意数量的实参
def make_pizza(size, *toppings):
    print(f"\nMaking a {size} inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')