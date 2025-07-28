# 学舌
# # input 函数暂停程序运行，等待用户输入。获取用户输入后，将其付给一个变量
# # input 接受一个参数，用于提示用户输入什么信息
# message = input("Tell me something, I will repeat back to you: ")
# print(message)

# 循环
# prompt = "Tell me something, I will repeat back to you:"
# prompt += "\nEnter 'quit' to end the program."
# message = ''
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)

# # 优化，新增标志位，通过判断和更新标志位，判断while是否继续循环
# prompt = "Tell me something, I will repeat back to you:"
# prompt += "\nEnter 'quit' to end the program."
# message = ""
# active = True
# while active:
#     message = input(prompt)
#     if message != 'quit':
#         print(message)
#     else:
#         active = False

# 使用break语句提前终止循环
prompt = "Tell me something, I will repeat back to you:"
prompt += "\nEnter 'quit' to end the program."
message = ""
while True:
    message = input(prompt)
    if message == 'quit':
        break
    else:
        print(message)