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
python -m pip install django
```

pip 从各地下载资源，因此我们搭建新的虚拟环境之后，都最好更新下 pip。

#### 18.1.5 在 Django 中搭建项目

在虚拟环境 ll_env 处于激活状态下，同时安装了 django，我们可以运行以下命令来直接
创建 django 项目:

```bash
django-admin startproject ll_project .
```

执行完上述命令后，我们发现在当前目录下生成了一个 ll_project 文件夹，其中自动生成
了一些文件。

#### 18.1.6 创建数据库

在虚拟环境处于激活状态下执行以下命令创建数据库

```bash
python manage.py migrate
```
