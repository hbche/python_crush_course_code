from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()

birthday = input("Enter your birthday, in the form mmddyy:")
if birthday in contents:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")