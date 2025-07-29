# 练习8.6：城市名　编写一个名为city_country()的函数，它接受城市的名称及其所属的国家。
# 这个函数应返回一个格式类似于下面的字符串：
# "Santiago, Chile" # 圣地亚哥, 智力 # 圣地亚哥是智力的首都
# 至少使用三个城市至国家对调用这个函数，并打印它返回的值。
# def city_country(city, country):
#     result = f"{city}, {country}"
#     return result.title()
# print(city_country('Wuhan', 'China'))
# print(city_country(country = 'Japan', city = 'Tokyo'))
# print(city_country(country = 'Ottawa', city = 'Canada'))

# 练习8.7：专辑　编写一个名为make_album()的函数，它创建一个描述音乐专辑的字典。
# 这个函数应接受歌手名和专辑名，并返回一个包含这两项信息的字典。
# 使用这个函数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑的信息。
# 给make_album()函数添加一个默认值为None的可选形参，以便存储专辑包含的歌曲数。
# 如果调用这个函数时指定了歌曲数，就将这个值添加到表示专辑的字典中。调用这个函数，并至少在一次调用中指定专辑包含的歌曲数。
# def make_alnum(singer, alnum, count = None):
#     if count:
#         return {
#             'singer': singer,
#             'alnum': alnum,
#             'count': count
#         }
#     else:
#         return {
#             'singer': singer,
#             'alnum': alnum
#         }
# alnum_0 = make_alnum('jay Chou', 'Fantasy', 10)
# print(alnum_0)
# alnum_1 = make_alnum('JJ Lin', 'No.89757')
# print(alnum_1)
# alnum_2 = make_alnum('Eason Chen', 'U87')
# print(alnum_2)

# 练习8.8：用户的专辑　在为练习8.7编写的程序中，编写一个while循环，让用户输入歌手名和专辑名。
# 获取这些信息后，使用它们来调用make_album()函数并将创建的字典打印出来。
# 在这个while循环中，务必提供退出途径。

def make_alnum(singer, alnum):
    return {
        'singer': singer,
        'alnum': alnum
    }
active = True
while active:
    print("\nPlease input your favorite singer and alnum:")
    print("Enter 'q' at any time to quit.")
    singer = input("Please input the name of singer:")
    if singer == 'q':
        break
    alnum = input("Please input alnum:")
    if alnum == 'q':
        break
    print("Your favirote singer and his/her alnum is:")
    print(make_alnum(singer, alnum))