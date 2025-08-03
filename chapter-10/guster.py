# 练习10.4：访客　编写一个程序，提示用户输入其名字。在用户做出响应后，将其名字写入文件guest.txt。
from pathlib import Path

path = Path('gust.txt')
username = input("Please input your name:")
path.write_text(username)