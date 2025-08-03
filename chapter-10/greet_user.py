from pathlib import Path
import json

path = Path('usernames.json')
contents = path.read_text()
username = json.loads(contents)
print(f"Welcome come back, {username}!")