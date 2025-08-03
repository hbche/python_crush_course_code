## 第 10 章 文件与异常

学习处理文件和保存数据能让我们的程序更易于使用：用户能够选择输入什么样的数据以及在什么时候输入；用户使用程序做完一些工作后，可先将程序关闭，以后再接着往下做。学习处理异常可帮助我们应对文件不存在等情况，以及处理其他可能导致程序崩溃的问题。这让程序在面对错误的数据时更稳健—不管这些错误数据源自无意的错误，还是出于破坏程序的恶意企图。我们在本章学习的技能可提高程序的适用性、可用性和稳定性。

### 10.1 读取文件

要使用文本文件中的信息，首先需要将信息读取到内存中。既可以一次性读取文件的全部内容，也可以逐行读取。

#### 10.1.1 读取文件的全部内容

要读取文件，需要一个包含若干行文本的文件。下面来创建一个文件，它包含精确到小数点后 30 位的圆周率值，且在小数点后每 10 位处换行：

```pi_digits.txt
3.1415926535
  8979323846
  2643383279
```

下面的程序打开并读取这个文件，再将其内容显示到屏幕上：

```python file_reader.py
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
print(contents)
```

要使用文件的内容，需要将其路径告知 Python。路径(path)指的是*文件*或*文件夹*在系统中的准确位置。Python 提供了 pathlib 模块，让我们能够更轻松地在各种操作系统中处理文件和目录。提供特定功能的模块通常称为库(library)。这就是这个模块被命名为 pathlib 的原因所在。

这里首先从 pathlib 模块导入 Path 类。Path 对象指向一个文件，可用来做很多事情。例如，让我们在使用文件前核实它是否存在，读取文件的内容，以及将新数据写入文件。这里创建了一个表示文件 pi_digits.txt 的 Path 对象，并将其赋给了变量 path​。由于这个文件与当前编写的.py 文件位于同一个目录中，因此 Path 只需要知道其文件名就能访问它。

创建表示文件 pi_digits.txt 的 Path 对象后，使用 read_text()方法来读取这个文件的全部内容 ​。read_text()将该文件的全部内容作为一个字符串返回，而我们将这个字符串赋给了变量 contents。在打印 contents 的值时，将显示这个文本文件的全部内容：

```bash
3.1415926535
  8979323846
  2643383279

```

相比于原始文件，该输出唯一不同的地方是末尾多了一个空行。为何会多出这个空行呢？因为 read_text() 在到达文件末尾时会返回一个空字符串，而这个空字符串会被显示为一个空行。

要删除这个多出来的空行，可对字符串变量 contents 调用 rstrip()：

```python
from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
contents = contents.rstrip()
print(contents)
```

要在读取文件内容时删除末尾的换行符，可在调用 read_text()后直接调用方法 rstrip()：

```python
contents = path.read_text().rstrip()
```

这行代码先让 Python 对当前处理的文件调用 read_text() 方法，再对 read_text() 返回的字符串调用 rstrip() 方法，然后将整理好的字符串赋给变量 contents。这种做法称为方法*链式调用*(method chaining)，在编程时很常用。

#### 10.1.2 相对文件路径和绝对文件路径

当将类似于 pi_digits.txt 这样的简单文件名传递给 Path 时，Python 将在当前执行的文件（即.py 程序文件）所在的目录中查找。

根据我们组织文件的方式，有时可能要打开不在程序文件所属目录中的文件。例如，我们可能将程序文件存储在了文件夹 python_work 中，并且在文件夹 python_work 中创建了一个名为 text_files 的文件夹，用于存储程序文件要操作的文本文件。虽然文件夹 text_files 在文件夹 python_work 中，但仅向 Path 传递文件夹 text_files 中的文件的名称也是不可行的，因为 Python 只在文件夹 python_work 中查找，而不会在其子文件夹 text_files 中查找。要让 Python 打开不与程序文件位于同一个目录中的文件，需要提供正确的路径。

在编程中，指定路径的方式有两种。首先，相对文件路径让 Python 到相对于当前运行的程序所在目录的指定位置去查找。由于文件夹 text_files 位于文件夹 python_work 中，因此需要创建一个以 text_files 打头并以文件名结尾的路径，如下所示：

```python
path = Path('text_files/filename.txt')
```

其次，可以将文件在计算机中的准确位置告诉 Python，这样就不用管当前运行的程序存储在什么地方了。这称为*绝对文件路径*。在相对路径行不通时，可使用绝对路径。假如 text_files 并不在文件夹 python_work 中，则仅向 Path 传递路径'text_files/filename.txt'是行不通的，因为 Python 只在文件夹 python_work 中查找该位置。为了明确地指出希望 Python 到哪里去查找，需要提供绝对路径。

绝对路径通常比相对路径长，因为它们以系统的根文件夹为起点：

```python
path = Path('/home/eric/data_files/text_files/filename.txt')
```

使用绝对路径，可读取系统中任何地方的文件。就目前而言，最简单的做法是，要么将数据文件存储在程序文件所在的目录中，要么将其存储在程序文件所在目录下的一个文件夹（如 text_files）中。

#### 10.1.3 访问文件中的各行

在使用文件时，经常需要检查其中的每一行：可能要在文件中查找特定的信息，或者以某种方式修改文件中的文本。例如，在分析天气时，可能要遍历一个包含天气数据的文件，并使用天气描述中包含 sunny 字样的行；在新闻报道中，可能要查找包含标记<headline>的行，并按特定的格式改写它。

我们可以使用 `splitlines()` 方法将冗长的字符串转换为一系列行，再使用 for 循环以每次一行的方式检查文件中的各行：

```python file_reader.py
path = Path('pi_digits.txt')
lines = path.read_text().splitlines()
contents = ''
for line in lines:
    print(line)
```

与前面一样，首先读取文件的全部内容 ​。如果要处理文件中的各行，就无须在读取文件时删除任何空白。splitlines()方法返回一个列表，其中包含文件中所有的行，而我们将这个列表赋给了变量 lines​。然后，遍历这些行并打印它们：

#### 10.1.4 使用文件的内容

将文件的内容读取到内存中后，就能以任意方式使用这些数据了。下面以简单的方式使用圆周率的值。首先，创建一个字符串，它包含文件中存储的所有数字，不包含空格：

```python pi_string.py
from pathlib import Path

path = Path('pi_digits.txt')
lines = path.read_text().splitlines()
pi_string = ''
for line in lines:
    pi_string += line
print(pi_string)
print(len(pi_string))
```

像上一个示例一样，首先读取文件，并将其中的所有行都存储在一个列表中。然后，创建变量 pi_string，用于存储圆周率的值。接下来，使用循环将各行加入 pi_string​。最后，打印这个字符串及其长度：

```bash
3.1415926535  8979323846  2643383279
36
```

变量 pi_string 存储的字符串包含原来位于每行左端的空格。要删除这些空格，可对每行调用 lstrip()：

```python
from pathlib import Path

path = Path('pi_digits.txt')
lines = path.read_text().splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
print(pi_string)
print(len(pi_string))
```

这样就获得了一个字符串，其中包含准确到 30 位小数的圆周率值。这个字符串的长度是 32 个字符，因为它还包含整数部分的 3 和小数点：

```bash
3.141592653589793238462643383279
32
```

> 注意：在读取文本文件时，Python 将其中的所有文本都解释为字符串。如果读取的是数，并且要将其作为数值使用，就必须使用 **int()** 函数将其转换为整数，或者使用 **float()** 函数将其转换为浮点数。

#### 10.1.5 包含 100 万位的大型文件

尽管前面分析的都是一个只有三行的文本文件，但是这些代码示例也可以处理比它大得多的文件。如果一个文本文件包含精确到小数点后 1 000 000 位而不是 30 位的圆周率值，也可以创建一个包含所有这些数字的字符串。无须对前面的程序做任何修改，只需将这个文件传递给它即可。在这里，只打印到小数点后 50 位，以免终端花太多时间滚动显示全部的 1 000 000 位数字：

```python pi_string.py
from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines[0:52]:
    pi_string += line.lstrip()

print(f"{pi_string[0:52]}...")
print(len(pi_string))
```

输出表明，创建的字符串确实包含精确到小数点后 1 000 000 位的圆周率值：

```bash
3.14159265358979323846264338327950288419716939937510...
1000002
```

在可处理的数据量方面，Python 没有任何限制。只要系统的内存足够大，我们想处理多少数据就可以处理多少数据。

#### 10.1.6 圆周率中包含你的生日吗

下面来扩展刚才编写的程序，以确定某个人的生日是否包含在圆周率值的前 1 000 000 位中。为此，可先将生日表示为一个由数字组成的字符串，再检查这个字符串是否在 pi_string 中：

```python pi_birthday.py
from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()

birthday = input("Enter your birthday, in the form mmddyy:")
if birthday in contents:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
```

首先提示用户输入其生日，再检查这个字符串是否在 pi_string 中。运行这个程序：

```bash
Enter your birthday, in the form mmddyy:121195
Your birthday appears in the first million digits of pi!
```

> 动手试一试
>
> 练习 10.1: Python 学习笔记　在文本编辑器中新建一个文件，写几句话来总结一下你至此学到的 Python 知识，其中每一行都以“In Python you can”打头。将这个文件命名为 learning_python.txt，并存储到为完成本章练习而编写的程序所在的目录中。编写一个程序，读取这个文件，并将你所写的内容打印两次：第一次打印时读取整个文件；第二次打印时先将所有行都存储在一个列表中，再遍历列表中的各行。
>
> 练习 10.2: C 语言学习笔记　可使用 replace()方法将字符串中的特定单词替换为另一个单词。下面是一个简单的示例，演示了如何将句子中的'dog'替换为'cat'：
>
> \>>> message = "I really like dogs."
>
> \>>> message.replace('dog', 'cat')
>
> 'I really like cats.'
>
> 读取你刚创建的文件 learning_python.txt 中的每一行，将其中的 Python 都替换为另一门语言的名称，如 C。将修改后的各行都打印到屏幕上。
>
> 练习 10.3：简化代码　本节前面的程序 file_reader.py 中使用了一个临时变量 lines，来说明 splitlines()的工作原理。可省略这个临时变量，直接遍历 splitlines()返回的列表：
>
> for line in contents.splitlines():
>
> 对于本节的每个程序，都删除其中的临时变量，让代码更简洁。

### 10.2 写入文件

保存数据的最简单的方式之一是将其写入文件。通过将输出写入文件，即便关闭包含程序输出的终端窗口，这些输出也依然存在：既可以在程序结束运行后查看这些输出，也可以与他人共享输出文件，还可以编写程序来将这些输出读取到内存中并进行处理。

#### 10.2.1 写入一行

定义一个文件的路径后，就可使用 write_text()将数据写入该文件了。为明白其中的工作原理，下面将一条简单的消息存储到文件中，而不将其打印到屏幕上：

```python write_message.py
from pathlib import Path

path = Path('programming.txt')
path.write_text('I love programming.')
```

write_text()方法接受单个实参，即要写入文件的字符串。这个程序没有终端输出，但如果我们打开文件 programming.txt，将看到如下一行内容：

```txt
I love programming.
```

> 注意：Python 只能将字符串写入文本文件。如果要将数值数据存储到文本文件中，必须先使用函数 `str()` 将其转换为字符串格式。

#### 10.2.1 写入多行

write_text()方法会在幕后完成几项工作。首先，如果 path 变量对应的路径指向的文件不存在，就创建它。其次，将字符串写入文件后，它会确保文件得以妥善地关闭。如果没有妥善地关闭文件，可能会导致数据丢失或受损。

要将多行写入文件，需要先创建一个字符串（其中包含要写入文件的全部内容）​，再调用 write_text()并将这个字符串传递给它。下面将多行内容写入文件 programming.txt：

```python
from pathlib import Path

path = Path('programming.txt')
messages = 'I love programming.\n'
messages += 'I love creating new games.\n'
messages += 'I also love working with data.\n'
path.write_text(messages)
```

首先定义变量 contents，用于存储要写入文件的所有内容。接下来，使用运算符+=在该变量中追加这个字符串。可根据需要执行这种操作任意多次，以创建任意长度的字符串。这里在每行末尾都添加了换行符，让每个句子都占一行。

如果运行这个程序，再打开文件 programming.txt，将发现上述每一行都在这个文本文件中：

```txt
I love programming.
I love creating new games.
I also love working with data.

```

也可以通过添加空格、制表符和空行来设置输出的格式，就像处理基于终端的输出那样。对于字符串的长度没有任何限制。计算机生成的很多文件就是这样创建的。

> 注意：在对 path 对象调用 write_text()方法时，务必谨慎。如果指定的文件已存在，write_text()将删除其内容，并将指定的内容写入其中。本章后面将介绍如何使用 pathlib 检查指定的文件是否存在。

> 动手试一试
>
> 练习 10.4：访客　编写一个程序，提示用户输入其名字。在用户做出响应后，将其名字写入文件 guest.txt。
>
> 练习 10.5：访客簿　编写一个 while 循环，提示用户输入其名字。收集用户输入的所有名字，将其写入 guest_book.txt，并确保这个文件中的每条记录都独占一行。

### 10.3 异常

Python 使用称为异常(exception)的特殊对象来管理程序执行期间发生的错误。每当发生让 Python 不知所措的错误时，它都会创建一个异常对象。如果我们编写了处理该异常的代码，程序将继续运行；如果我们未对异常进行处理，程序将停止，并显示一个 traceback，其中包含有关异常的报告。

异常是使用 try-except 代码块处理的。try-except 代码块让 Python 执行指定的操作，同时告诉 Python 在发生异常时应该怎么办。在使用 try-except 代码块时，即便出现异常，程序也将继续运行：显示我们编写的友好的错误消息，而不是令用户迷惑的 traceback。

#### 10.3.1 处理 ZeroDivisionError 异常

下面来看一种导致 Python 引发异常的简单错误。我们可能知道不能将数除以 0，但还是让 Python 试试看吧：

```python division_calculator.py
print(5/0)
```

Python 无法这样做，因此我们将看到一个 traceback：

```bash
Traceback (most recent call last):
  File "division_calculator.py", line 1, in <module>
    print(5/0)
          ~^~
ZeroDivisionError: division by zero
```

在上述 traceback 中，错误 ZeroDivisionError 是个异常对象 ​。Python 在无法按我们的要求做时，就会创建这种对象。在这种情况下，Python 将停止运行程序，并指出引发了哪种异常，而我们可根据这些信息对程序进行修改。下面将告诉 Python，在发生这种错误时该怎么办。这样，如果再次发生这样的错误，我们就有所准备了。

#### 10.3.2 使用 try-except 代码块

当我们认为可能发生错误时，可编写一个 try-except 代码块来处理可能引发的异常。我们让 Python 尝试运行特定的代码，并告诉它如果这些代码引发了指定的异常，该怎么办。

处理 ZeroDivisionError 异常的 try-except 代码块类似于下面这样：

```python division_calculator.py
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

这里将导致错误的代码行 print(5/0)放在一个 try 代码块中。如果 try 代码块中的代码运行起来没有问题，Python 将跳过 except 代码块；如果 try 代码块中的代码导致错误，Python 将查找与之匹配的 except 代码块并运行其中的代码。

在这个示例中，try 代码块中的代码引发了 ZeroDivisionError 异常，因此 Python 查找指出了该怎么办的 except 代码块，并运行其中的代码。这样，用户看到的是一条友好的错误消息，而不是 traceback：

```bash
You can't divide by zero!
```

如果 try-except 代码块后面还有其他代码，程序将继续运行，因为 Python 已经知道了如何处理错误。下面来看一个在捕获错误后让程序继续运行的示例。

#### 10.3.3 使用异常避免崩溃

如果在错误发生时，程序还有工作没有完成，妥善地处理错误就显得尤其重要。这种情况经常出现在要求用户提供输入的程序中。如果程序能够妥善地处理无效输入，就能提示用户提供有效输入，而不至于崩溃。

下面来创建一个只执行除法运算的简单计算器：

```python division_calculator.py
print("Give me two numbers, i'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input('\nFirst number:')
    if first_number == 'q':
        break
    second_number = input("\nSecond number:")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)
```

对出发运算增加 try_except 代码块

```python
print("Give me two numbers, i'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input('\nFirst number:')
    if first_number == 'q':
        break
    second_number = input("\nSecond number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
        print(answer)
    except ZeroDivisionError:
        print("You can't divide by zero!")
```

#### 10.3.4 else 代码块

通过将可能引发错误的代码放在 try-except 代码块中，可提高程序抵御错误的能力。因为错误是执行除法运算的代码行导致的，所以需要将它放到 try-except 代码块中。这个示例还包含一个 else 代码块，只有 try 代码块成功执行才需要继续执行的代码，都应放到 else 代码块中：

```python
print("Give me two numbers, i'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input('\nFirst number:')
    if first_number == 'q':
        break
    second_number = input("\nSecond number:")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)
```

只有可能引发异常的代码才需要放在 try 语句中。有时候，有一些仅在 try 代码块成功执行时才需要运行的代码，这些代码应放在 else 代码块中。except 代码块告诉 Python，如果在尝试运行 try 代码块中的代码时引发了指定的异常该怎么办。

通过预测可能发生错误的代码，可编写稳健的程序。它们即便面临无效数据或缺少资源，也能继续运行，不受无意的用户错误和恶意攻击的影响。

#### 10.3.5 处理 FileNotFoundError 异常

在使用文件时，一种常见的问题是找不到文件：要查找的文件可能在其他地方，文件名可能不正确，或者这个文件根本就不存在。对于所有这些情况，都可使用 try-except 代码块来处理。

我们来尝试读取一个不存在的文件。下面的程序尝试读取文件 alice.txt 的内容，但这个文件并没有被存储在 alice.py 所在的目录中：

```python alice.py
from pathlib import Path

path = Path('alice.txt')
contents = path.read_text(encoding='utf-8')
```

请注意，这里使用 read_text()的方式与前面稍有不同。**如果系统的默认编码与要读取的文件的编码不一致，参数 encoding 必不可少。**如果要读取的文件不是在我们的系统中创建的，这种情况更容易发生。

Python 无法读取不存在的文件，因此引发了一个异常：

```bash
Traceback (most recent call last):
  File "E:\python_crush_course_code\chapter-10\alice.py", line 4, in <module>
    contents = path.read_text(encoding='utf-8')
  File "C:\Users\hbche\AppData\Local\Programs\Python\Python313\Lib\pathlib\_local.py", line 546, in read_text
    return PathBase.read_text(self, encoding, errors, newline)
           ~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\hbche\AppData\Local\Programs\Python\Python313\Lib\pathlib\_abc.py", line 632, in read_text
    with self.open(mode='r', encoding=encoding, errors=errors, newline=newline) as f:
         ~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\hbche\AppData\Local\Programs\Python\Python313\Lib\pathlib\_local.py", line 537, in open
    return io.open(self, mode, buffering, encoding, errors, newline)
           ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
```

为了处理这个异常，应将 traceback 指出的存在问题的代码行放到 try 代码块中。这里，存在问题的是包含 read_text()的代码行：

```python
from pathlib import Path

path = Path('alice.txt')
try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Sorry, the file {path} not exist.")
```

在这个示例中，try 代码块中的代码引发了 FileNotFoundError 异常，因此要编写一个与该异常匹配的 except 代码块 ​。这样，当找不到文件时，Python 将运行 except 代码块中的代码，从而显示一条友好的错误消息，而不是 traceback：

```bash
Sorry, the file alice.txt not exist.
```

如果文件不存在，这个程序就什么也做不了，因此上面就是这个程序的全部输出。下面来扩展这个示例，看看当我们使用多个文件时，异常处理可提供什么样的帮助。

#### 10.3.6 分析文本

我们可以分析包含整本书的文本文件。很多经典文学作品是以简单的文本文件的方式提供的，因为它们不受版权限制。本节使用的文本来自古登堡计划，该计划提供了一系列不受版权限制的文学作品。如果我们要在编程项目中使用文学文本，这是一个很不错的资源。

下面来提取童话 Alice in Wonderland（​《爱丽丝漫游奇境记》​）的文本，并尝试计算它包含多少个单词。我们将使用 split()方法，它默认以空白为分隔符将字符串分拆成多个部分：

#### 10.3.7 使用多个文件

下面多分析几本书。

```python word_count.py
from pathlib import Path

def count_words(path):
    """计算一个文件大致包含多少个单词"""

    try:
        contents = Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

path = Path('alice.txt')
count_words(path)
```

现在可以编写一个简短的循环，计算要分析的任何文本包含多少个单词了。为此，我们把要分析的文件的名称存储在一个列表中，然后对列表中的每个文件都调用 count_words()。

```python
from pathlib import Path

def count_words(path):
    """计算一个文件大致包含多少个单词"""

    try:
        # contents = Path(path).read_text(encoding="utf-8")
        contents = Path(path).read_text()
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt']
for filename in filenames:
    count_words(Path(filename))
```

```bash
The file alice.txt has about 26442 words.
The file siddhartha.txt has about 41278 words.
The file moby_dick.txt has about 214422 words.
```

#### 10.3.8 静默失败

并非每次捕获异常都需要告诉用户，我们有时候希望程序在发生异常时保持静默，就像什么都没有发生一样继续运行。要让程序静默失败，可像通常那样编写 try 代码块，但在 except 代码块中明确地告诉 Python 什么都不要做。Python 有一个 pass 语句，可在代码块中使用它来让 Python 什么都不做：

```python
from pathlib import Path

def count_words(path):
    """计算一个文件大致包含多少个单词"""

    try:
        # contents = Path(path).read_text(encoding="utf-8")
        contents = Path(path).read_text()
    except FileNotFoundError:
        # 静默失败，什么都不做
        pass
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little woman.txt']
for filename in filenames:
    count_words(Path(filename))
```

相比于上一个程序，这个程序唯一的不同之处是，except 代码块包含一条 pass 语句。现在，当出现 FileNotFoundError 异常时，虽然仍将执行 except 代码块中的代码，但什么都不会发生。当这种错误发生时，既不会出现 traceback，也没有任何输出。用户将看到存在的每个文件包含多少个单词，但没有任何迹象表明有一个文件未找到：

```bash
The file alice.txt has about 26442 words.
The file siddhartha.txt has about 41278 words.
The file moby_dick.txt has about 214422 words.
```

#### 10.3.8 决定报告哪些错误

该在什么情况下向用户报告错误？又该在什么情况下静默失败呢？如果用户知道要分析哪些文件，他们可能希望在有文件未被分析时出现一条消息来告知原因。如果用户只想看到结果，并不知道要分析哪些文件，可能就无须在有些文件不存在时告知他们。向用户显示他们不想看到的信息可能会降低程序的可用性。Python 的错误处理结构让我们能够细致地控制与用户共享错误信息的程度，要共享多少信息由我们决定。

编写得很好且经过恰当测试的代码不容易出现内部错误，如语法错误和逻辑错误，但只要程序依赖于外部因素，如用户输入、是否存在指定的文件、是否有网络连接，就有可能出现异常。凭借经验可判断该在程序的什么地方包含异常处理块，以及出现错误时该向用户提供多少相关的信息。

> 动手练一练
>
> 练习 10.6：加法运算　在提示用户提供数值输入时，常出现的一个问题是，用户提供的是文本而不是数。在这种情况下，当你尝试将输入转换为整数时，将引发 ValueError 异常。编写一个程序，提示用户输入两个数，再将它们相加并打印结果。在用户输入的任意一个值不是数时都捕获 ValueError 异常，并打印一条友好的错误消息。对你编写的程序进行测试：先输入两个数，再输入一些文本而不是数。
>
> 练习 10.7：加法计算器　将为练习 10.6 编写的代码放在一个 while 循环中，让用户在犯错（输入的是文本而不是数）后能够继续输入数。
>
> 练习 10.8：猫和狗　创建文件 cats.txt 和 dogs.txt，在第一个文件中至少存储三只猫的名字，在第二个文件中至少存储三条狗的名字。编写一个程序，尝试读取这些文件，并将其内容打印到屏幕上。将这些代码放在一个 try-except 代码块中，以便在文件不存在时捕获 FileNotFoundError 异常，并显示一条友好的消息。将任意一个文件移到另一个地方，并确认 except 代码块中的代码将正确地执行。
>
> 练习 10.9：静默的猫和狗　修改你在练习 10.8 中编写的 except 代码块，让程序在文件不存在时静默失败。
>
> 练习 10.10：常见单词　访问古登堡计划，找一些你想分析的图书。下载这些作品的文本文件或将浏览器中的原始文本复制到文本文件中。
>
> 可以使用方法 count()来确定特定的单词或短语在字符串中出现了多少次。例如，下面的代码计算'row'在一个字符串中出现了多少次：
>
> \>>> line = "Row, row, row your boat"
>
> \>>> line.count('row')
>
> 2
> \>>> line.lower().count('row')
>
> 3
>
> 请注意，通过使用 lower()将字符串转换为全小写的，可捕捉要查找的单词的各种格式，而不管其大小写如何。
>
> 编写一个程序，读取你在古登堡计划中获取的文件，并计算单词'the'在每个文件中分别出现了多少次。这里计算得到的结果并不准确，因为诸如'then'和'there'等单词也被计算在内了。请尝试计算'the'（包含空格）出现的次数，看看结果相差多少。

### 10.4 存储数据

模块 json 让我们能够将简单的 Python 数据结构转换为 JSON 格式的字符串，并在程序再次运⾏时从⽂件中加载数据。我们还可以使⽤ json 在 Python 程序之间共享数据。更重要的是，JSON 数据格式并不是 Python 专⽤的，这让我们能够将以 JSON 格式存储的数据与使⽤其他编程语⾔的⼈共享。这是⼀种轻量级数据格式，不仅很有⽤，也易于学习。

#### 10.4.1 使用 json.dumps() 和 json.loads()

json.dumps() 函数接受⼀个实参，即要转换为 JSON 格式的数据。这个函数返回⼀个字符串，这样我们就可将其写⼊数据⽂件了：

```python number_write.py
from pathlib import Path
import json

numbers = [1, 3, 5, 7, 9]
path = Path('number.json')
contents = json.dumps(numbers)
path.write_text(contents)
```

⾸先导⼊模块 json，并创建⼀个数值列表。然后选择⼀个⽂件名，指定要将该数值列表存储到哪个⽂件中 ​。通常使⽤⽂件扩展名 .json 来指出⽂件存储的数据为 JSON 格式。接下来，使⽤ json.dumps() 函数⽣成⼀个字符串，它包含我们要存储的数据的 JSON 表⽰形式。⽣成这个字符串后，像本章前⾯⼀样，使⽤ write_text() ⽅法将其写⼊⽂件。

下⾯再编写⼀个程序，使⽤ json.loads() 将这个列表读取到内存中：

```python
from pathlib import Path
import json

path = Path('numbers.json')
contents = path.read_text()
contents = json.loads(contents)
print(contents)
```

#### 10.4.2 保存和读取用户生成的数据

使⽤ json 保存⽤户⽣成的数据很有必要，因为如果不以某种⽅式进⾏存储，⽤户的信息就会在程序停⽌运⾏时丢失。

```python
from pathlib import Path
import json

username = input("What is your name?")
path = Path('usernames.json')
path.write_text(json.dumps(username))
print(f"We will remember you when you come back, {username}!")
```

现在再编写⼀个程序，向名字已被存储的⽤户发出问候：

```python greet_user.py
from pathlib import Path
import json

path = Path('usernames.json')
contents = path.read_text()
username = json.loads(contents)
print(f"Welcome come back, {username}!")
```

将这两个程序合并到⼀个程序（remember_me.py）中

```python remember_me.py
from pathlib import Path
import json

path = Path('usernames.json')
if not path.exists():
    username = input("What is your name?\n")
    print(f"I will remember you when you come back, {username}!")
    contents = json.dumps(username)
    path.write_text(contents)
else:
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
```

Path 类提供了很多很有⽤的⽅法。如果指定的⽂件或⽂件夹存在，exists() ⽅法返回 True，否则返回 False。这⾥使⽤ path.exists() 来确定是否存储了⽤户名 ​。如果⽂件 username.json 存在，就加载其中的⽤户名，并向⽤户发出个性化问候。如果⽂件 username.json 不存在 ​，就提⽰⽤户输⼊⽤户名，并存储⽤户输⼊的值。此外，还会打印⼀条消息，指出当⽤户再回来时我们还会记得他。

#### 10.4.3 重构

我们经常会遇到这样的情况：虽然代码能够正确地运⾏，但还可以将其划分为⼀系列完成具体⼯作的函数来进⾏改进。这样的过程称为重构。重构让代码更清晰、更易于理解、更容易扩展。

重写 remember_me.py

```python
from pathlib import Path
import json

def get_stored_username(path):
    """如果存在用户名就获取它"""

    if not path.exists():
        return False
    else:
        contents = path.read_text()
        username = json.loads(contents)
        return username


def get_new_username(path):
    """提示用户输入用户名"""

    username = input("What is your name?")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """问候用户，并指出名字"""

    path = Path('usernames.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"I will remember you when you come back, {username}!")


greet_user()
```

> 动手试一试
>
> 喜欢的数   编写⼀个程序，提⽰⽤户输⼊⾃⼰喜欢的数，并使⽤ json.dumps() 将这个数存储在⽂件中。再编写⼀个程序，从⽂件中读取这个值，并打印如下消息。
>
> I know your favorite number! It's **\_**.
>
> 练习 10.12：记住喜欢的数   将你在完成练习 10.11 时编写的两个程序合⽽为⼀。如果存储了⽤户喜欢的数，就向⽤户显⽰它，否则提⽰⽤户输⼊⾃⼰喜欢的数并将其存储在⽂件中。运⾏这个程序两次，看看它是否像预期的那样⼯作。
>
> 练习 10.13：⽤户字典   ⽰例 remember_me.py 只存储了⼀项信息—⽤户名。请扩展该⽰例，让⽤户同时提供另外两项信息，再将收集到的所有信息存储到⼀个字典中。使⽤ json.dumps() 将这个字典写⼊⽂件，并使⽤ json.loads() 从⽂件中读取它。打印⼀条摘要消息，指出程序记住了有关⽤户的哪些信息。
>
> 练习 10.14：验证⽤户   最后⼀个 remember_me.py 版本假设⽤户要么已输⼊其⽤户名，要么是⾸次运⾏该程序。我们应修改这个程序，以防当前⽤户并⾮上次运⾏该程序的⽤户。
>
> 为此，在 greet_user() 中打印欢迎⽤户回来的消息之前，询问他⽤户名是否是对的。如果不对，就调⽤ get_new_username() 让⽤户输⼊正确的⽤户名。

### 10.5 小结

在本章中，我们⾸先学习了如何使⽤⽂件，包括如何读取整个⽂件，如何读取⽂件中的各⾏，以及如何根据需要将任意数量的⽂本写⼊⽂件。然后学习了异常，以及如何处理程序可能引发的异常。最后，我们学习了如何存储 Python 数据结构，以保存⽤户提供的信息，避免让⽤户在每次运⾏程序时都重新提供。
