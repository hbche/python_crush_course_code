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

```python
def greet_users(users):
    """向列表中的每个用户发送简单的问候"""
    for user in users:
        message = f"Hello, {user.title()}!"
        print(f"{message}")

users = ['alice', 'lucy', 'sam']

greet_users(users)
```

#### 8.4.1 在函数中修改列表

```python
# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 模拟打印每个设计，直到没有未打印的设计为止
# 打印每个设计后，都将其移到列表 completed_designs 中
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
```

将上述逻辑拆分成两个函数调用：

```python
def print_models(unprinted_designs, completed_models):
    """模拟打印每个设计，直到没有未打印的设计为止。打印每个设计后，将其移到列表 completed_models 中"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
    return completed_models

def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for model in completed_models:
        print(f"{model}")

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```

#### 8.4.2 禁止函数修改列表

为了防止函数修改原始列表数据，可以在调用函数时，利用列表切片，传递列表的副本进去，避免修改原列表

```python
function_name(list_name[:])
print_models(unprinted_designs[:], completed_models)
```

### 8.5 传递任意数量的实参

有时候预先不知道函数需要多少个参数，好在 Python 允许函数从调用语句中收集任意数量的实参。

```python
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

形参名\*toppings 中的星号让 Python 创建一个名为 toppings 的元组，该元组包含函数收到的所有实参。

```python
def make_pizza(*toppings):
    """概述只做pizza的配料"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

#### 8.5.1 结合使用位置实参和任意数量的实参

如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。Python 先匹配位置实参和关键字实参，再将余下的实参都收集在最后一个形参中。

```python
# 结合使用位置参数和任意数量的实参
def make_pizza(size, *toppings):
    print(f"\nMaking a {size} inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

#### 8.5.2 使用任意数量的关键字实参

有时候，需要接受任意数量的实参，但是预先不知道传递给函数的会是什么样的信息。在这种情况下，可将函数编写成能够接受任意数量的键值对-调用语句提供多少就接受多少。

```python
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们直到的有关用户的一切"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')
print(user_profile)
```

参数 \*\*user_info 中的两个星号让 Python 创建一个名为 user_info 的字典，该字典包含函数收到的其他所有名值对。在这个函数中，可以像访问其他字典那样访问 user_info 中的名值对。

### 8.6 将函数存储在模块中

将函数存储在称为 **模块** 的独立文件中，再将模块导入到主程序。import 语句可以让你在当前运行的程序中使用模块中的代码。

#### 8.6.1 导入整个模模块

要让函数是可导入的，得先创建模块。**模块** 是扩展名为.py 的文件，包含要导入函数的代码。

创建一个 pizza.py 文件，代码如下：

```python
def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print(f"\nMaking a {size} inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
```

在同级目录下创建一个 making_pizzas.py 的程序，代码如下：

```python
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

这是一种导入方法：只需要编写一条 import 语句并在其中指定模块名，就可在程序中使用该模块中的所有函数。如果使用这种 import 语句导入名为 module_name.py 的整个模块，就可使用下面的语法来使用其中的任意一个函数：

```python
import module_name
module_name.function_name()
```

#### 8.6.2 导入特定的函数

还可以导入模块中的特定函数：

```python
from module_name import function_name
```

用逗号分隔函数名，可根据需要从模块中导入任意数量的函数：

```python
from module_name import function_0, function_1, function_2
```

上面示例改写如下：

```python
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

#### 8.6.3 使用 as 给函数指定别名

如果要导入的函数名称太长或者与程序中的既有函数名冲突，可指定简短而独一无二的别名：函数的另一个名称，类似外号。关键字 `as` 可在导入函数时给函数指定一个别名：

```python
from pizza import make_pizza as map

map(16, 'pepperoni')
map(12, 'mushrooms', 'green peppers', 'extra cheese')
```

指定别名的语法如下：

```python
from module_name import function_name as function_alias
```

#### 8.6.4 使用 as 给模块指定别名

还可以使用 as 给模块指定别名。

```python
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

给模块指定别名的语法如下：

```python
import module_name as module_alias
```

#### 8.6.5 导入模块中的所有函数

使用星号运算符 **\*** 可让 Python 导入模块中的所有函数。

```python
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

导入模块中所有函数的语法如下：

```python
from module_name import *
```

最佳的做法是，要么只导入使用到的函数，要么导入整个模块并使用点号。

### 8.7 函数编写指南

1. 函数名只能使用小写字母加下划线，指定描述性名称。
2. 每个函数应该包含简要阐述其功能的注释。
3. 在给函数参数指定默认值时，等号两侧不要留空格；函数调用关键字实参也需要尊选该规则。
   ```python
    def function_name(parameter_0, parameter_1='default value')
    function_name(parameter_1=value_1, parameter_0=value_0)
   ```
4. 如果模块中存在多个函数，函数声明之间使用两行空白行分隔。。
5. 所有 import 语句应该都放在文件开头。唯一的例外是需要在文件开头使用注释来描述整个模块。

#### 8.7.1 动手练一练

```python
# 练习8.15：打印模型　将示例printing_models.py中的函数放在一个名为printing_functions.py的文件中。
# 在printing_models.py的开头编写一条import语句，并修改这个文件以使用导入的函数。


# 练习8.16：导入　选择一个你编写的且只包含一个函数的程序，将这个函数放在另一个文件中。
# 在主程序文件中，使用下述各种方法导入这个函数，再调用它：
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

# 练习8.17：函数编写指南　选择你在本章编写的三个程序，确保它们遵循了本节介绍的函数编写指南。
```

## 第九章
