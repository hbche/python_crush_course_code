# 练习7.1：汽车租赁　编写一个程序，询问用户要租什么样的汽车，并打印一条消息，如下所示。　　
# Let me see if I can find you a Subaru.
# # 你想要什么品牌的汽车？
# prompt = "Which car brand are you looking for?"
# brand = input(prompt)
# print(f"Let me see if I can find you a {brand}.")

# 练习7.2：餐馆订位　编写一个程序，询问用户有多少人用餐。如果超过8个人，就打印一条消息，指出没有空桌；否则指出有空桌。
# prompt = "How many people will be dining?"
# people_num = int(input(prompt))
# if people_num > 8:
#     print("Sorry, we’re fully booked / no tables available at the moment.")
# else:
#     print("Yes, we have tables available.")

# 练习7.3: 10的整数倍　让用户输入一个数，并指出这个数是否是10的整数倍。
prompt = "Please enter an integer, and I’ll tell you whether it’s a multiple of 10."
num = int(input(prompt))
if num % 10 == 0:
    print(f"The number {num}, it’s a multiple of 10.")
else:
    print(f"The number {num}, it not is a multiple of 10.")
