# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print(f"Add {requested_topping}")


# requested_toppings = []
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Add {requested_topping}")
# else:
#     print("Are you sure you want to a plain pizza.")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fires', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping not in available_toppings:
        print(f"Sorry, we don't have {requested_topping}")
    else:
        print(f"Add {requested_topping}")
print("\nFinished making your pizza.")