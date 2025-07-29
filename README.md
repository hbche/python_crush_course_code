# Python 编程: 从入门到实践代码

记录阅读《Python 编程: 从入门到实践代码》时的示例和练习的代码

## 第三章

## 第四章

## 第五章

## 第六章

## 第七章

## 第八章 函数

### 8.1 定义函数

#### 8.1.1 响函数传递信息

#### 8.1.2 实参和形参

### 8.2 传递参数

#### 8.2.1 位置实参

```python
# 位置参数
def describe_pet(animal_type, pet_name):
    """打印宠物种类及名称"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('dog', 'cola')
describe_pet('hamster', 'harry')
```

1. 多次调用函数
2. 位置实参的顺序很重要

#### 8.2.2 关键字实参

```python
def describe_pet(animal_type, pet_name):
    """打印宠物的种类和名称"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
# 关键字参数
describe_pet(pet_name='cola', animal_type='dog')
```

#### 8.2.3 默认值

```python
# 默认值，具有默认值的参数只能放在参数列表的后面
def describe_pet(pet_name, animal_type = 'dog'):
    """描述宠物"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('willie')
describe_pet(pet_name='harry', animal_type='hamster') # 仓鼠
```

> 当使用默认值时，必须在形参列表中先列出没有默认值的形参，再列出有默认值的形参。
> 这让 Python 依然能够正确地解读位置实参。

#### 8.2.4 等效的函数调用

鉴于可混合使用位置实参、关键字实参和默认值，通常有多种等效的函数调用方式。

```python
#一条名为Willie的小狗
describe_pet('willie')
describe_pet(pet_name='willie')

#一只名为Harry的仓鼠
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
```

#### 8.2.5 避免实参错误

### 8.3 返回值

在函数中，可以使用 `return` 语句将值返回到调用函数的哪行代码。

#### 8.3.1 返回简单的值

```python
def get_formatted_name(first_name, last_name):
    """返回标准格式的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name("jimi", 'hendrix')
print(musician)
```

#### 8.3.2 让实参变成可选的

有时候，需要让实参变成可选的，以便使用函数的人只在必要时才提供额外的信息。可以使
用默认值来让实参变成可选的。

```python
def get_formatted_name(first_name, medium_name, last_name):
    full_name = f"{first_name} {medium_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)
```

将上述函数中的 medium_name 变为可选参数

```python
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
```

#### 8.3.3 返回字典

函数可以返回任意类型的值，包括列表和字典等较为复杂的数据结构。

```python
# 定义函数，返回一个字典
def build_person(first_name, last_name):
    """返回一个字典，其中包含一个人的信息"""
    person_info = {
        'first_name': first_name,
        'last_name': last_name
    }
    return person_info
musician = build_person('jimi', 'hendrix')
print(musician)
```

增加可选参数，返回更为丰富的字典。

```python
# 定义age参数有默认值的函数，返回字段
def build_person(first_name, last_name, age = None):
    person_info = {
        'first_name': first_name.title(),
        'last_name': last_name.title()
    }
    if age:
        person_info['age'] = age
    return person_info
musician = build_person('jimi', 'hendrix', 27)
print(musician)
```

可将 None 视为占位符，在条件测试中，None 相等于 False。

#### 8.3.3 结合使用函数和 while 循环

```python
def get_formatted_name(first_name, last_name):
    """返回规范格式的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
# 这是一个无限循环！
while True:
    print("Please tell me your name:")
    first_name = input("Input your first name:")
    last_name = input("Input your last name:")
    print(f"{get_formatted_name(first_name, last_name)}")
```

解决无限循环，增加提示语，判断用户输入是否为 q ，从而决定循环是否继续

```python
def get_formatted_name(first_name, last_name):
    """返回规范格式的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("Please tell me your name:")
    print("Enter 'q' at any time to quit.")
    first_name = input("Input your first name:")
    if first_name == 'q':
        break
    last_name = input("Input your last name:")
    if last_name == 'q':
        break
    print(f"{get_formatted_name(first_name, last_name)}")
```

### 8.4 传递列表

#### 8.4.1 在函数中修改列表

#### 8.4.2 禁止函数修改列表

```python
function_name(list_name[:])
print_models(unprinted_designs[:], completed_models)
```

### 8.5 传递任意数量的实参

#### 8.5.1 结合使用位置实参和任意数量的实参

#### 8.5.2 使用任意数量的关键字实参

## 第九章
