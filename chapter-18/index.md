## 第 18 章 Django 入门

### 18.1 创立项目

#### 18.1.1 制定规范

#### 18.1.2 创建虚拟环境

```bash
python -m venv ll_env
```

ll_env 中 ll 是 learning_log 的缩写；

##### 18.1.2.1 什么是虚拟环境

Python 虚拟环境是一个独立的 Python 运行环境，允许在同一台机器上为不同的项目创建
隔离的 Python 运行环境。每个 Python 虚拟环境都有以下几个组成部分：

- 解释器
- 安装包
- 环境变量

##### 18.1.2.2 为什么需要虚拟环境

1. 项目隔离：不同项目可能需要不同版本的 python 或第三方库
2. 避免冲突：防止全局 Python 环境被污染
3. 依赖管理：方便记录和分享项目的依赖关系
4. 测试环境：可以安全地测试新包而不影响其他项目

##### 18.1.2.3 场景举例

- 项目 A 需要 Django 3.2 版本
- 项目 B 需要 Django 4.0 版本
- 如果在系统全局安装，两个版本会冲突

#### 18.1.3 激活虚拟环境

```bash
.\ll_env\Scripts\Activate.ps1
```

激活虚拟环境之后，命令行提示符前面会有 `(ll_env)` 的展示。

#### 18.1.4 安装 Django

激活虚拟环境之后，我们首先更新 pip，在安装 Django

```bash
python -m pip install --upgrade pip
```

更新完 pip 之后，可以通过 pip 安装 django 了

```bash
pip install django
```

pip 从各地下载资源，因此我们搭建新的虚拟环境之后，都最好更新下 pip。

#### 18.1.5 在 Django 中搭建项目

在虚拟环境 ll_env 处于激活状态下，同时安装了 django，我们可以运行以下命令来直接
创建 django 项目:

```bash
django-admin startproject ll_project .
```

执行完上述命令后，我们发现在当前目录下生成了一个 ll_project 文件夹，其中自动生成
了一些文件，同时自动生成了一个 manage.py 文件。

#### 18.1.6 创建数据库

在虚拟环境处于激活状态下执行以下命令创建数据库

```bash
python manage.py migrate
```

执行完上述命令之后，我们发现在当前目录下生成了一个 db.sqlite3 的文件。

#### 18.1.7 查看项目

下面来核实 Django 正确创建了项目。为此可以使用 runserver 来查看项目的状态：

```bash
python manage.py runserver
```

### 18.2 创建应用程序

Django 项目由一系列应用程序组成，它们协同工作让项目成为一个整体。

将目录切换到 manage.py 同级目录下，激活虚拟环境，执行以下命令：

```bash
python manage.py startapp learning_logs
```

命令行 startapp appname 让 Django 搭建应用程序所需的基础设施。

#### 18.2.1 定义模型

模型告诉 Django 如何处理应用程序中存储的数据。模型就是一个类，它包含属性和方法。

接下来我们在 learning_logs 目录下的 models.py 文件中声明我们的数据模型：

```python
from django.db imort models

class Topic(models.Model):
    text = models.ChartField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text
```

其中 Model 类是 Django 中定义了模型基本功能的类。为此我们集成该类，声明两个属性
：text 和 date_added。

属性 text 是一个 ChartField 由字符组成的数据。在定义 ChartField 时必须告诉
Django 该在数据库中预留多少空间，这里将 text 限制在 200 个字符。

属性 date_added 是一个 DateTimeField —— 记录日期和时间的数据。我们传递实参
auto_now_add=True，每当用户创建一个新主题时，Django 都会将这个属性自动设置为当前
的日期和时间。

如果模型有 `__str__` 方法，那么每当需要生成表示模型实例的输出时，Django 豆浆调用
这个方法。我们声明的 Topic 类实现了 `__str__` 方法，返回 text 属性。

#### 18.2.2 激活模型

为了使用这些模型，需要告诉 Django 将前述应用程序包含到项目中。因此我们需要修改当
前项目下的 settings.py，从而告诉 Django 哪些应用程序要安装到项目中。

```python settings.py
--snip--
# Application definition

INSTALLED_APPS = [
    # 我们的应用，需要在Django默认应用前面，以免被默认应用覆盖
    'learning_logs',

    # Django默认添加的应用
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
--snip--
```

接下来，需要让 Django 修改数据库，使其能够存储于模型 Topic 相关的信息。为此，我
们需要执行以下命令：

```bash
python manage.py makemigrations learning_logs
```

命令 makemigrations 让 Django 确定该如何修改数据库，使其能够存储与前面定义的新模
型相关联的数据。输出表明 Django 创建了一个名为 0001_initial.py 的迁移文件，这个
文件将在数据库中为模型 Topic 创建一个表。

下面应用这种迁移，让 Django 替我们修改数据库：

```bash
python manage.py migrate
```

执行完之后需要检查的是最后一行输出，其中 Django 指出在为 learning_logs 应用迁移
时一切正常。

后面每当新增模型时，都采取以下三个步骤：修改 models.py，对 learning_logs 项目调
用 makemigrations，以及执行 migrate 让 Django 迁移项目。

#### 18.2.3 Django 管理网站
