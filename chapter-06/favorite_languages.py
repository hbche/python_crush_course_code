# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python'
# }
# # favorite_language = favorite_languages['sarah'].title()
# # print(f"Sarah's favorite language is {favorite_language}.")
# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language}")

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python'
# }

# for name in favorite_languages.keys():
#     print(name.title())

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python'
# }
# friends = ['phil', 'sarah']

# for name in favorite_languages.keys():
#     print(f"Hi {name.title()}!")
#     if name in friends:
#         language = favorite_languages[name].title()
#         print(f"\t {name.title()}, I see you love {language}!")


# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python'
# }
# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for talking the poll.")

# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'rust',
#     'phil': 'python'
# }
# print("The following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#     print(language.title())


favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell']
}
for name, languages in favorite_languages.items():
    print(f"{name.title()}'s favorite language are: ")
    for language in languages:
        print(f"\t{language}")