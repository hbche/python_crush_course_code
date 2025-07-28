# dimensions = (200, 50)
# print(dimensions[0])
# print(dimensions[1])

# # 元组元素是不可修改的，如果修改则会出发Python类型错误
# dimensions[0] = 300

# 给元组变量重新赋值
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)