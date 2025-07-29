# 练习8.9：消息　创建一个列表，其中包含一系列简短的文本消息。
# 将这个列表传递给一个名为show_messages()的函数，这个函数会打印列表中的每条文本消息。
# message_list = ["How are you?", "I'm fine. And you?", "How old are you?", "Whre are you from?"]
# def show_messages(messages):
#     print("Print messages:")
#     for message in messages:
#         print(message)
# show_messages(message_list)

# 练习8.10：发送消息　在为练习8.9编写的程序中，编写一个名为send_messages()的函数，将每条消息都打印出来并移到一个名为sent_messages的列表中。
# 调用send_messages()函数，再将两个列表都打印出来，确认把消息移到了正确的列表中。
# def send_messages(show_messages, sent_messages):
#     print("Print messages:")
#     while show_messages:
#         current_message = show_messages.pop()
#         print(f"Showing message: {current_message}")
#         sent_messages.append(current_message)
#     return sent_messages

# def show_messages(sent_messages):
#     print("\nThe following messages have been sent:")
#     for message in sent_messages:
#         print(message)

# message_list = ["How are you?", "I'm fine. And you?", "How old are you?", "Whre are you from?"]
# sent_messages = []
# send_messages(message_list[:], sent_messages)
# show_messages(sent_messages)

# 练习8.11：消息归档　修改为练习8.10编写的程序，在调用函数send_messages()时，向它传递消息列表的副本。
# 调用send_messages()函数后，将两个列表都打印出来，确认原始列表保留了所有的消息。

def send_messages(show_messages, sent_messages):
    print("Print messages:")
    while show_messages:
        current_message = show_messages.pop()
        print(f"Showing message: {current_message}")
        sent_messages.append(current_message)
    return sent_messages

def show_messages(sent_messages):
    print("\nThe following messages have been sent:")
    for message in sent_messages:
        print(message)

message_list = ["How are you?", "I'm fine. And you?", "How old are you?", "Whre are you from?"]
sent_messages = []
send_messages(message_list[:], sent_messages)
show_messages(sent_messages)
show_messages(message_list)