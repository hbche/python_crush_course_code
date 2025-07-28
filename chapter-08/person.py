# 定义函数，返回一个字典
# def build_person(first_name, last_name):
#     """返回一个字典，其中包含一个人的信息"""
#     person_info = {
#         'first_name': first_name,
#         'last_name': last_name
#     }
#     return person_info
# musician = build_person('jimi', 'hendrix')
# print(musician)

# 定义age参数有默认值的函数，返回字段
# def build_person(first_name, last_name, age = None):
#     person_info = {
#         'first_name': first_name.title(),
#         'last_name': last_name.title()
#     }
#     if age:
#         person_info['age'] = age
#     return person_info
# musician = build_person('jimi', 'hendrix', 27)
# print(musician)

def get_formatted_name(first_name, last_name):
    """定义函数，接收名和姓，返回全名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
prompt = "Please tell me your name:"
prompt += "\nEnter 'q' at any time to quit."
while True:
    print(prompt)
    first_name = input("First Name:")
    if first_name == 'q':
        break
    last_name = input('Last Name:')
    if last_name == 'q':
        break
    full_name = get_formatted_name(first_name, last_name)
    print(f"\nHello, {full_name}!")