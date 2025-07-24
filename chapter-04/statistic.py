# # 简单的列表统计
# values = []
# for value in range(1, 11):
#     values.append(value ** 2)

# print(values)
# print(f"The max number of values is: {max(values)}")
# print(f"The sum of values is: {sum(values)}")
# print(f"The min number of values is: {min(values)}")

values = [value ** 2 for value in range(2, 11, 2)]
print(values)