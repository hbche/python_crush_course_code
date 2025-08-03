## 第 11 章 测试代码

### 11.1 使用 pip 安装 pytest

虽然 Python 通过标准库提供了⼤量的功能，但 Python 开发⼈员还是需要频繁⽤到第三⽅包。第三⽅包（third-party package）指的是独⽴于 Python 核⼼的库。有些深受欢迎的第三⽅包最终会被纳⼊标准库，并从此随 Python ⼀起被安装。通常，能被纳⼊标准库的包在消除最初的 bug 后不会发⽣太多变化，它们在被纳⼊后只能与 Python 语⾔同步演进。

然⽽，很多包并未被纳⼊标准库，因此得以独⽴于 Python 语⾔本⾝的更新计划。相较于纳⼊标准库，独⽴的第三⽅包的更新频率往往更⾼，pytest 和本书第⼆部分将使⽤的⼤部分库属于这种情况。虽然不应盲⽬信任所有的第三⽅包，但也不要因噎废⾷，因为很多重要的功能是使⽤第三⽅包实现的。

#### 11.1.1 更新 pip

Python 提供了⼀款名为 pip 的⼯具，可⽤来安装第三⽅包。因为 pip 帮我们安装来⾃外部的包，所以更新频繁，以消除潜在的安全问题。有鉴于此，我们先来更新 pip。

```bash
python -m install pip --upgrade pip
```

输出结果

```bash
Requirement already satisfied: pip in xxx
 (25.1.1)
Collecting pip
  Downloading pip-25.2-py3-none-any.whl.metadata (4.7 kB)
Downloading pip-25.2-py3-none-any.whl (1.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.8/1.8 MB 4.4 MB/s eta 0:00:00
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 25.1.1
    Uninstalling pip-25.1.1:
      Successfully uninstalled pip-25.1.1
Successfully installed pip-25.2
```

这个命令的第⼀部分（python -m pip）让 Python 运⾏ pip 模块；第⼆部分（install --upgrade）让 pip 更新⼀个已安装的包；⽽最后⼀部分（pip）指定要更新哪个第三⽅包。输出表明，当前的 pip 版本（25.1.1）​ 被替换成了最新的版本（25.2）

#### 11.1.2 安装 pytest

将 pip 升级到最新版本后，就可以安装 pytest 了：

```bash
python -m pip install --user pytest
```

这⾥使⽤的核⼼命令也是 pip install，但指定的标志不是 --upgrade，⽽是 --user。这个标志让 Python 只为当前⽤户安装指定的包。输出表明，成功地安装了最新版本的 pytest，以及 pytest 运⾏所需的多个其他包。

可使⽤下⾯的命令安装众多的第三⽅包：

```bash
python -m pip install [--user] package_name
```

注意：如果在执⾏这个命令时遇到⿇烦，可尝试在不指定标志 `--user` 的情况下再次执⾏它。

### 11.2 测试函数

```python name_function.py
def get_formatted_name(first_name, last_name, middle_name=''):
    """生成格式规范的姓名"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()
```

```python names.py
from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first_name = input('Please give me a first name:')
    if first_name == 'q':
        break
    last_name = input('Please give me a last name:')
    if last_name == 'q':
        break
    formatted_name = get_formatted_name(first_name, last_name)
    print(f"Neatly formatted name: {formatted_name}")
```

#### 11.2.1 单元测试和测试用例

软件的测试⽅法多种多样。⼀种最简单的测试是单元测试（unit test）​，⽤于核实函数的某个⽅⾯没有问题。测试⽤例（test case）是⼀组单元测试，这些单元测试⼀道核实函数在各种情况下的⾏为都符合要求。良好的测试⽤例考虑到了函数可能收到的各种输⼊，包含针对所有这些情况的测试。全覆盖（full coverage）测试⽤例包含⼀整套单元测试，涵盖了各种可能的函数使⽤⽅式。对于⼤型项⽬，要进⾏全覆盖测试可能很难。通常，最初只要针对代码的重要⾏为编写测试即可，等项⽬被⼴泛使⽤时再考虑全覆盖。

#### 11.2.2 可通过的测试

使⽤ pytest 进⾏测试，会让单元测试编写起来⾮常简单。我们将编写⼀个测试函数，它会调⽤要测试的函数，并做出有关返回值的断⾔。如果断⾔正确，表⽰测试通过；如果断⾔不正确，表⽰测试未通过。

这个针对 get_formatted_name() 函数的测试如下：

```python test_name_function.py
from name_function import get_formatted_name

def test_first_last_name():
    """能够正确地处理像 Janis Joplin 这样的姓名吗？"""

    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'
```

在这个测试⽂件中，⾸先导⼊要测试的 get*formatted_name() 函数。然后，定义⼀个测试函数 test_first_last_name()​。这个函数名⽐以前使⽤的都⻓，原因有⼆。第⼀，测试函数必须以 test* 打头。在测试过程中，pytest 将找出并运⾏所有以 test\_ 打头的函数。第⼆，测试函数的名称应该⽐典型的函数名更⻓，更具描述性。我们⾃⼰不会调⽤测试函数，⽽是由 pytest 替我们查找并运⾏它们。因此，测试函数的名称应⾜够⻓，让我们在测试报告中看到它们时，能清楚地知道它们测试的是哪些⾏为。

接下来，调⽤要测试的函数 ​。像运⾏ names.py 时⼀样，这⾥在调⽤ get_formatted_name() 函数时向它传递了实参 'janis' 和'joplin'。将这个函数的返回值赋给变量 formatted_name。

最后，做出⼀个断⾔ ​。断⾔（assertion）就是声称满⾜特定的条件：这⾥声称 formatted_name 的值为 'Janis Joplin'。

#### 11.2.3 运行测试

如果直接运⾏⽂件 test_name_function.py，将不会有任何输出，因为我们没有调⽤这个测试函数。相反，应该让 pytest 替我们运⾏这个测试⽂件。

为此，打开⼀个终端窗⼝，并切换到这个测试⽂件所在的⽂件夹。在终端窗⼝中执⾏命令 pytest，我们将看到如下输出：

```bash
pytest
```

以下是输出：

```bash
========================================================== test session starts ==========================================================
platform win32 -- Python 3.13.5, pytest-8.4.1, pluggy-1.6.0
rootdir: E:\python_crush_course_code\chapter-11
collected 1 item

test_name_function.py .                                                                                                            [100%]

=========================================================== 1 passed in 0.02s ===========================================================
```

> 注意：如果出现⼀条消息，提⽰没有找到命令 pytest，请执⾏命令 `python -m pytest`。

#### 11.2.4 未通过的测试

我们来修改 get_formatted_name，使其支持还有 middle_name 的姓名：

```python name_function.py
def get_formatted_name(first_name, middle_name, last_name):
    """生成格式规范的姓名"""
    full_name = f"{first_name} {middle_name} {last_name}"

    return full_name.title()
```

我们再次运行测试用例，发现它不再处理只有 first_name 和 last_name 的场景。
这次的运行结果如下：

```bash
python -m pytest
========================================================== test session starts ==========================================================
platform win32 -- Python 3.13.5, pytest-8.4.1, pluggy-1.6.0
rootdir: E:\python_crush_course_code\chapter-11
collected 1 item

test_name_function.py F                                                                                                            [100%]

=============================================================== FAILURES ================================================================
_________________________________________________________ test_first_last_name __________________________________________________________

    def test_first_last_name():
        """能够正确地处理像 Janis Joplin 这样的姓名吗？"""

>       formatted_name = get_formatted_name('janis', 'joplin')
                         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
E       TypeError: get_formatted_name() missing 1 required positional argument: 'last_name'

test_name_function.py:6: TypeError
======================================================== short test summary info ========================================================
FAILED test_name_function.py::test_first_last_name - TypeError: get_formatted_name() missing 1 required positional argument: 'last_name'
=========================================================== 1 failed in 0.13s ===========================================================
```

这⾥的信息很多，因为在测试未通过时，需要我们知道的事情可能有很多。⾸先，输出中有⼀个字⺟ F​，表明有⼀个测试未通过。然后是 FAILURES 部分 ​，这是关注的焦点，因为在运⾏测试时，通常应该关注未通过的测试。接下来，指出未通过的测试函数是 test_first_last_name()​。右尖括号指出了导致测试未能通过的代码⾏。下⼀⾏中的 E 指出了导致测试未通过的具体错误：缺少必不可少的位置实参 'last'，导致 TypeError。在末尾的简短⼩结中，再次列出了最重要的信息。这样，即使我们运⾏了很多测试，也可快速获悉哪些测试未通过以及测试未通过的原因。

#### 11.2.5 在测试未通过时怎么办

在测试未通过时，该怎么办呢？如果检查的条件没错，那么测试通过意味着函数的⾏为是对的，⽽测试未通过意味着你编写的新代码有错。因此，在测试未通过时，不要修改测试。因为如果你这样做，即便能让测试通过，像测试那样调⽤函数的代码也将突然崩溃。相反，应修复导致测试不能通过的代码：检查刚刚对函数所做的修改，找出这些修改是如何导致函数⾏为不符合预期的。

在这个⽰例中，get_formatted_name() 以前只需要名和姓这两个实参，但现在要求提供名、中间名和姓，⽽且新增的中间名参数是必不可少的。这导致 get_formatted_name() 的⾏为与原来不同。就这⾥⽽⾔，最佳的选择是让中间名变为可选的。这样，不仅在使⽤类似于 Janis Joplin 的姓名进⾏测试时可以通过，⽽且这个函数还能接受中间名。下⾯来修改 get_formatted_name()，将中间名设置为可选的，然后再次运⾏这个测试⽤例。如果通过，就接着确认这个函数是否能够妥善地处理中间名。

要将中间名设置为可选的，可在函数定义中将形参 middle 移到形参列表末尾，并将其默认值指定为⼀个空字符串。还需要添加⼀个 if 测试，以便根据是否提供了中间名相应地创建姓名：

```python
def get_formatted_name(first_name, last_name, middle_name=''):
    """生成格式规范的姓名"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"

    return full_name.title()
```

#### 11.2.6 添加新测试

确定 get_formatted_name() ⼜能正确地处理简单的姓名后，我们再编写⼀个测试，⽤于测试包含中间名的姓名。为此，在⽂件 test_name_function.py 中添加⼀个测试函数：

```python
from name_function import get_formatted_name

def test_first_last_name():
    """能够正确地处理像 Janis Joplin 这样的姓名吗？"""

    formatted_name = get_formatted_name('janis', 'joplin')
    assert formatted_name == 'Janis Joplin'

def test_first_middle_last_name():
    """能够正确地处理像 Wolfgang Amadeus Mozart 这样的姓名吗？"""

    formatted_name = get_formatted_name('Wolfgang', middle_name='Amadeus', last_name='Mozart')
    assert formatted_name == 'Wolfgang Amadeus Mozart'
```

我们将这个新函数命名为 test*first_last_middle_name()。记住，函数名必须以 test*打头，这样该函数才会在我们运⾏ pytest 时⾃动运⾏。这个函数名清楚地指出了它测试的是 get_formatted_name() 的哪个⾏为，如果该测试未通过，我们就能⻢上知道受影响的是哪种类型的姓名。

为测试 get_formatted_name() 函数 ​。再次运⾏ pytest，两个测试都通过了：

```bash
========================================================== test session starts ==========================================================
platform win32 -- Python 3.13.5, pytest-8.4.1, pluggy-1.6.0
rootdir: E:\python_crush_course_code\chapter-11
collected 2 items

test_name_function.py ..                                                                                                           [100%]

=========================================================== 2 passed in 0.01s ===========================================================
```

太好了！现在我们知道，这个函数⼜能正确地处理像 Janis Joplin 这样的姓名了，⽽且确定它也能够正确地处理像 Wolfgang Amadeus Mozart 这样的姓名。

> 动手试一试
>
> 练习 11.1：城市和国家   编写⼀个函数，它接受两个形参：⼀个城市名和⼀个国家名。这个函数返回⼀个格式为 City, Country 的字符串，如 Santiago, Chile。将这个函数存储在⼀个名为 city_functions.py 的模块中，并将这个⽂件存储在⼀个新的⽂件夹中，以免 pytest 在运⾏时，尝试运⾏之前编写的测试。
>
> 创建⼀个名为 test_cities.py 的程序，对刚编写的函数进⾏测试。编写⼀个名为 test_city_country() 的函数，核实在使⽤类似于'santiago' 和 'chile' 这样的值来调⽤该函数时，得到的字符串是正确的。运⾏测试，确认 test_city_country() 通过了。
>
> 练习 11.2：⼈⼝数量   修改前⾯的函数，使其包含第三个必不可少的形参 population，并返回⼀个格式为 City, Country -population xxx 的字符串，如 Santiago, Chile -population 5000000。运⾏测试，确认 test_city_country()未通过。
>
> 修改上述函数，将形参 population 设置为可选的。再次运⾏测试，确认 test_city_country() ⼜通过了。
>
> 再编写⼀个名为 test_city_country_population() 的测试，核实可以使⽤类似于'santiago'、'chile' 和'population=5000000' 这样的值来调⽤这个函数。再次运⾏测试，确认 test_city_country_population() 通过了。

### 11.3 测试类

很多程序会⽤到类，因此证明类能够正确地⼯作⼗分必要。如果针对类的测试通过了，你就能确信对类所做的改进没有意外地破坏其原有的⾏为。

#### 11.3.1 各种断言

到⽬前为⽌，我们只介绍了⼀种断⾔：声称⼀个字符串变量取预期的值。在编写测试时，可做出任何可表⽰为条件语句的断⾔。如果该条件确实成⽴，你对程序⾏为的假设就得到了确认，可以确信其中没有错误。如果你认为应该满⾜的条件实际上并不满⾜，测试就不能通过，让你知道代码存在需要解决的问题。下表中列出了一些有用的断言类型。

| 断言                       | 用途                                  |
| -------------------------- | ------------------------------------- |
| assert a == b              | 断言两个值相等                        |
| assert a != b              | 断言两个值不相等                      |
| assert a                   | 断言 a 的布尔求值为 True              |
| assert not a               | 断言 a 的布尔求值为 False             |
| assert element in list     | 断言元素 element 是否在列表 list 中   |
| assert element not in list | 断言元素 element 是否不在列表 list 中 |

这⾥列出的只是九⽜⼀⽑，测试能包含任意可⽤条件语句表⽰的断⾔。

#### 11.3.2 一个要测试的类

类的测试与函数的测试相似，所做的⼤部分⼯作是测试类中⽅法的⾏为。然⽽，⼆者还是存在⼀些不同之处。下⾯来编写⼀个要测试的类，这是⼀个帮助管理匿名调查的类：

```python

```

#### 11.3.3 测试 AnonymousSurvey 类

#### 11.3.4 使用夹具

## 11.4 小结
