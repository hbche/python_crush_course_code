from pathlib import Path

# path = Path('pi_digits.txt')
# contents = path.read_text()
# contents = contents.rstrip()

# 绝对路径
# path = Path('E:/python_crush_course_code/chapter-10/python_work/pi_digits.txt')
# 相对路径
# path = Path('./python_work/pi_digits.txt')
# contents = path.read_text().rstrip()

path = Path('pi_digits.txt')
lines = path.read_text().splitlines()
contents = ''
for line in lines:
    print(line)