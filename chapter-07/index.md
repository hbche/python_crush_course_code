## 第七章用户输入和 while 循环

### 7.1 input()函数的工作原理

input()函数让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python 将其赋给一个变量，以便使用。

例如，下面的程序让用户输入一些文本，再将这些文本呈现给用户：

```python parrot.py
message = input("Tell me something, and I will repeat it back to you:")
print(message)
```

input()函数接受一个参数，即要向用户显示的提示(prompt)，让用户知道该输入什么样的信息。在这个示例中，当 Python 运行第一行代码时，用户将看到提示“Tell me something, and I will repeat it back to you:”​。程序等待用户输入，并在用户按回车键后继续运行。用户的输入被赋给变量 message，接下来的 print(message)将输入呈现给用户：

```bash
Tell me something, and I will repeat it back to you: Hello everyone!
Hello everyone!
```

#### 7.1.1 编写清晰的提示

每当使用 input()函数时，都应指定清晰易懂的提示，准确地指出希望用户提供什么样的信息—能指出用户应该输入什么信息的任何提示都行，如下所示：

```python greeter.py
name = input("Please enter your name:")
print(f"\nHello, {name}!")
```

通过在提示末尾（这里是冒号后面）添加一个空格，可将提示与用户输入分开，让用户清楚地知道其输入始于何处，如下所示：

```bash
Please Enter your name: Eric
Hello, Eric!
```

有时候，提示可能超过一行。例如，你可能需要指出获取特定输入的原因。在这种情况下，可先将提示赋给一个变量，再将这个变量传递给 input()函数。这样，即便提示超过一行，input()语句也会非常清晰。

```python greeter.py
prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")
```

这个示例演示了一种创建多行字符串的方式。第一行将消息的前半部分赋给变量 prompt。在第二行中，运算符+=在赋给变量 prompt 的字符串末尾追加一个字符串。

最终的提示占两行，且问号后面有一个空格，这也是为了使其更加清晰：

```bash
If you share your name, we can personalize the messages you see.
What is your first name? Eric

Hello, Eric!
```

#### 7.1.2 使用 input() 获取数值输入

在使用 input()函数时，Python 会将用户输入解读为字符串。请看下面让用户输入年龄的解释器会话：

```bash
>>> age = input("How old are you? ")
How old are you? 21
>>> age
'21'
```

用户输入的是数 21，但当我们请求 Python 提供变量 age 的值时，它返回的是'21'—用户输入的数值的字符串表示。我们怎么知道 Python 将输入解读成了字符串呢？因为这个数是用引号引起来的。如果只想打印输入，这一点儿问题都没有；但如果试图将输入作为数来使用，就会引发错误：

```bash
  >>> age = input("How old are you? ")
  How old are you? 21
❶ >>> age >= 18
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
❷ TypeError: '>=' not supported between instances of 'str' and 'int'
```

当试图将该输入用于数值比较时（见 ❶）​，Python 会报错，因为它无法将字符串和整数进行比较：不能将赋给 age 的字符串'21'与数值 18 进行比较（见 ❷）​。

为了解决这个问题，可使用函数 `int()` 将输入的字符串转换为数值，确保能够成功地执行比较操作：

```bash
  >>> age = input("How old are you? ")
  How old are you? 21
❶ >>> age = int(age)
  >>> age >= 18
  True
```

在这个示例中，当用户根据提示输入 21 后，Python 将这个数解读为字符串，但随后 int()将这个字符串转换成了数值表示（见 ❶）​。这样 Python 就能运行条件测试了：将变量 age（它现在表示的是数值 21）同 18 进行比较，看它是否大于或等于 18。测试结果为 True。

如何在实际程序中使用 int()函数呢？请看下面的程序，它判断一个人是否满足坐过山车的身高要求：
