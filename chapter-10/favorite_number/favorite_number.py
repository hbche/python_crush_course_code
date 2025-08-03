from pathlib import Path
import json

def get_favorite_number(path):
    """获取最喜欢的数字"""
    if path.exists():
        contents = path.read_text()
        favorite_number = json.loads(contents)
        return favorite_number
    else:
        return False

def input_favorite_number(path):
    """录入并存储用户喜欢的数字"""
    favorite_number = input("Input your favorite number:")
    try:
        contents = json.dumps(int(favorite_number))
        path.write_text(contents)
    except ValueError:
        print("Please input integer!")
    else:
        print(f"I will remember your favorite number {favorite_number}, when you come back.")

def show_favorite_number():
    """展示用户最喜欢的数字"""
    path = Path('favorite_number.json')
    favorite_number = get_favorite_number(path)
    if not favorite_number:
        favorite_number = input_favorite_number(path)
        print(f"I know your favorite number! It's {favorite_number}!")
    else:
        print(f"I know your favorite number! It's {favorite_number}!")
    

show_favorite_number()