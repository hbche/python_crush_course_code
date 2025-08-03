# 练习10.5：访客簿　编写一个while循环，提示用户输入其名字。
# 收集用户输入的所有名字，将其写入guest_book.txt，并确保这个文件中的每条记录都独占一行。
from pathlib import Path

path = Path('gust_book.txt')

active = True
contents = ''
while active:
    username = input("Please your name:")
    if username == 'q':
        active = False
    else:
        contents += f"{username}.\n"

path.write_text(contents)