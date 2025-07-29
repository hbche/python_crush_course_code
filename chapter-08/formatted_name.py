# 定义函数，同时设置返回值

# def get_formatted_name(first_name, last_name):
#     """返回标准格式的姓名"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
# musician = get_formatted_name("jimi", 'hendrix')
# print(musician)

# def get_formatted_name(first_name, medium_name, last_name):
#     full_name = f"{first_name} {medium_name} {last_name}"
#     return full_name.title()

# musician = get_formatted_name('john', 'lee', 'hooker')
# print(musician)

def get_formatted_name(first_name, last_name, medium_name = ''):
    # Python会将非空字符转换成True
    if medium_name:
        full_name = f"{first_name} {medium_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)