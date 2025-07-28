# 练习8.1：消息　编写一个名为display_message()的函数，让它打印一个句子，指出本章的主题是什么。调用这个函数，确认显示的消息正确无误。
# def display_message():
#     """打印本章的主题"""
#     print("Function define.")

# display_message()
# 练习8.2：喜欢的书　编写一个名为favorite_book()的函数，其中包含一个名为title的形参。让这个函数打印一条像下面这样的消息。　　One of my favorite books is Alice in Wonderland.调用这个函数，并将一本书的书名作为实参传递给它。

def favorite_book(title):
    """打印喜欢的书"""
    print(f"One of my favorite books is {title.title()}.")
favorite_book('Alice in Wonderland')