# name = input("Please input your name:")
# print(f"Hello {name}!")

# # 多行提示，使用变量存储
# prompt = "If you share your name, we can personalize the messages you see."
# prompt += "\nWhat is your first name?"
# name = input(prompt)
# print(f"\nHello {name}!")

age = int(input("How old are you?"))
# input获取的用户输入会自动转成字符串，即使输入的是数字，也会被input转成数字值的字符串，如果需要获取数值输入，可以使用int()函数将输入的字符串转成数值
if age > 18:
    print("You are adult!")