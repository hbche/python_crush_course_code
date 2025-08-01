# # 首先创建一个列表，其中包含一些要打印的设计
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# # 模拟打印每个设计，直到没有未打印的设计为止
# # 打印每个设计后，都将其移到列表 completed_designs 中
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

# def print_models(unprinted_designs, completed_models):
#     """模拟打印每个设计，直到没有未打印的设计为止。打印每个设计后，将其移到列表 completed_models 中"""
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)
#     return completed_models

# def show_completed_models(completed_models):
#     """显示打印好的所有模型"""
#     print("\nThe following models have been printed:")
#     for model in completed_models:
#         print(f"{model}")

from printing_functions import *

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

