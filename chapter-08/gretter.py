
# 使用def 定义函数，函数体使用冒号还是，之后的缩进表示函数体
# def greeter():
# 函数文档说明使用三个双引号标注
#     """"显示简单的问候语"""
#     print("Hello!")

# greeter()

def greet_user(username):
    print(f"Hello {username.title()}!")
greet_user('Alice')