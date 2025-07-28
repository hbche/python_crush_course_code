favorite_languages = {
    'Lucy': ['python'],
    'Semen': ['c', 'rust'],
    'Tom': ['python', 'go'],
    'Jack': ['rust']
}

for name in favorite_languages:
    if len(favorite_languages[name]) == 1:
        print(f"{name.title()}'s favorite language is {favorite_languages[name][0].title()}")
    else:
        print(f"{name.title()}'s favorate languages are: ")
        for language in favorite_languages[name]:
            print(f"\t{language.title()}")