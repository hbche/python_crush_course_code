
# 使用def 定义函数，函数体使用冒号还是，之后的缩进表示函数体
# def greeter():
# 函数文档说明使用三个双引号标注
#     """"显示简单的问候语"""
#     print("Hello!")

# greeter()


# def greet_user(username):
#     print(f"Hello {username.title()}!")
# greet_user('Alice')


def get_formatted_name(first_name, last_name):
    """返回规范格式的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("Please tell me your name:")
    print("Enter 'q' at any time to quit.")
    first_name = input("Input your first name:")
    if first_name == 'q':
        break
    last_name = input("Input your last name:")
    if last_name == 'q':
        break
    print(f"{get_formatted_name(first_name, last_name)}")
