# 练习6.1：人　使用一个字典来存储一个人的信息，包括名、姓、年龄和居住的城市。该字典应包含键first_name、last_name、age和city。将存储在该字典中的每项信息都打印出来。
# person_info = {
#     'first_name': 'Robin',
#     'last_name': 'Che',
#     'age': 29,
#     'city': 'Wuhan'
# }
# print(person_info)

# 练习6.2：喜欢的数1　使用一个字典来存储一些人喜欢的数。请想出5个人的名字，并将这些名字用作字典中的键。再想出每个人喜欢的一个数，并将这些数作为值存储在字典中。打印每个人的名字和喜欢的数。为了让这个程序更有趣，通过询问朋友确保数据是真实的。
# favorite_nums = {
#     'Jack': 9,
#     'Tom': 5,
#     "Alice": 8,
#     'Lucy': 1,
#     'Bob': 6
# }
# print(f"Jack's favorite number is {favorite_nums['Jack']}")
# print(f"Tom's favorite number is {favorite_nums['Tom']}")
# print(f"Alice's favorite number is {favorite_nums['Alice']}")
# print(f"Lucy's favorite number is {favorite_nums['Lucy']}")
# print(f"Bob's favorite number is {favorite_nums['Bob']}")

# 练习6.3：词汇表1　Python字典可用于模拟现实生活中的字典。为避免混淆，我们将后者称为词汇表。
# • 想出你在前面学过的5个编程术语，将它们用作词汇表中的键，并将它们的含义作为值存储在词汇表中。
# • 以整洁的方式打印每个术语及其含义。为此，既可以先打印术语，在它后面加上一个冒号，再打印其含义；也可以先在一行里打印术语，再使用换行符(\n)插入一个空行，然后在下一行里以缩进的方式打印其含义。
word_list = {
    '==': 'equality operator: returns True if the values of two operands are equal',
    'in': 'membership operator: returns True if a value is found in a sequence (string, list, tuple, dict, set, etc.)',
    'not in': 'negated membership operator: returns True if a value is NOT found in a sequence',
    'and': 'logical AND operator: returns True only if both operands are truthy',
    'or' : 'logical OR operator: returns True if at least one operand is truthy'
}
print(f"The mean of '==' is: {word_list['==']}")
print(f"The mean of 'in' is: {word_list['in']}")
print(f"The mean of 'not in' is: {word_list['not in']}")
print(f"The mean of 'and' is: {word_list['and']}")
print(f"The mean of 'or' is: {word_list['or']}")
