# from pathlib import Path

# path = Path('pi_digits.txt')
# lines = path.read_text().splitlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.lstrip()
# print(pi_string)
# print(len(pi_string))

from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines[0:52]:
    pi_string += line.lstrip()

print(f"{pi_string[0:52]}...")
print(len(pi_string))