from pathlib import Path

path = Path('programming.txt')
messages = 'I love programming.\n'
messages += 'I love creating new games.\n'
messages += 'I also love working with data.\n'
path.write_text(messages)