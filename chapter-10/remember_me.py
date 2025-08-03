from pathlib import Path
import json

def get_stored_username(path):
    """如果存在用户名就获取它"""

    if not path.exists():
        return False    
    else:
        contents = path.read_text()
        username = json.loads(contents)
        return username


def get_new_username(path):
    """提示用户输入用户名"""

    username = input("What is your name?")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """问候用户，并指出名字"""

    path = Path('usernames.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"I will remember you when you come back, {username}!")


greet_user()