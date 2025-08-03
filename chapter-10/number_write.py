from pathlib import Path
import json

path = Path('numbers.json')
contents = path.read_text()
contents = json.loads(contents)
print(contents)
