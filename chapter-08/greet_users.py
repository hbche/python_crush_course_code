def greet_users(users):
    """向列表中的每个用户发送简单的问候"""
    for user in users:
        message = f"Hello, {user.title()}!"
        print(f"{message}")

users = ['alice', 'lucy', 'sam']

greet_users(users)