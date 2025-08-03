from pathlib import Path

def read_pets_file(path):
    """读取对应宠物文件的内容"""

    try:
        contents = path.read_text(encoding="utf-8")
        lines = contents.splitlines()
        for line in lines:
            print(line)
    except FileNotFoundError:
        print(f"{path} not exist.")


read_pets_file(Path('cats.txt'))
read_pets_file(Path('dogs.txt'))

# def input_pets():
#     pets = []
#     active = True
#     while active:
#         animal = input("Please enter you favorite pet:")
#         if animal == 'q':
#             break
#         else:
#             pets.append(animal)

#     return pets


# def generate_pets_file(path):
#     """生成对应的文件"""

#     pets = input_pets()
#     print(f"The pets will be wrote into the {path} file.") 
#     contents = ""
#     for pet in pets:
#         contents += f"{pet.title()} is your favorite pet.\n"
#     path.write_text(contents, encoding="utf-8")


# generate_pets_file(Path('dogs.txt'))