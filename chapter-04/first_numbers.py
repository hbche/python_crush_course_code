# # 给range函数传入两个参数，将生成[n1, n2)之间的整数列表
# for value in range(1, 5):
#     print(value)

# # 如果只给range函数传一个参数，则会生成从0到n[不含]之间整数
# for value in range(6):
#     print(value)

# # 利用range()的结果作为list函数的参数，生成对应的数值列表
# values = list(range(1, 5))
# print(values)

# 在使用range函数时，可指定第三个参数，该参数用于指定生成前两个参数之间数值列表的步长
# 例如下面生成1~10之间的偶数列表
for value in range(2, 11, 2):
    print(value)

# values = range(1, 5)
# print(values)
