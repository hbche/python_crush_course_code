favorite_language = {
    'Lucy': 'python',
    'Semen': 'c',
    'Tom': 'python',
    'Jack': 'rust'
}

# for name, language in favorite_language.items():
#     # print(f"\nKey: {name}")
#     # print(f"Value: {language}")
#     print(f"{name.title()}'s favorite language is {language.title()}")

# for name in favorite_language.keys():
#     print(name)

# for name in favorite_language:
#     print(name)


# friends = ['Tom', 'Lucy']
# for name in favorite_language:
#     print(f"Hi {name.title()}!")
#     if name not in friends:
#         print(f"\t{name.title()}, I see you love {favorite_language[name].title()}!")
# if 'erin' not in favorite_language: # 等同 if 'erin' not in favorite_language.keys():
#     print("Erin, please take our poll!") # 请参与我们的投票

# # for name in sorted(favorite_language.keys()):
# for name in sorted(favorite_language):
#     print(f"{name.title()}'s favorite language is {favorite_language[name].title()}.")

print("The following language have been mentioned:")
# for language in favorite_language.values():
#     print(language.title())
for language in set(favorite_language.values()):
    print(language.title())

# 手动创建集合
languages = {'python', 'c', 'rust', 'python'}
print(languages) # {'python', 'rust', 'c'}