from pathlib import Path
import json

def get_username(path):
    """获取用户名字典"""
    if not path.exists():
        return None
    else:
        contents = path.read_text()
        username = json.loads(contents)
        return username
    
def input_name(path):
    print("What is your name?")
    first_name = input("Please input your first name:")
    last_name = input("Please input your last name:")
    username = {
        'first_name': first_name,
        'last_name': last_name
    }
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    path = Path('usernames.json')
    username = get_username(path)
    if username:
        print(f"Hello, {username['first_name'].title()} {username['last_name'].title()}!")
    else:
        input_name(path)

greet_user()