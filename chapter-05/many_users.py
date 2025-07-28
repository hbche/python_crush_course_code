users = {
    'Altman': {
        'first': 'Altman',
        'last': 'Sam',
        'location': 'Missouri'
    },
    "Rossum": {
        'first': 'Guido',
        'last': 'Rossum',
        'location': 'Gaithersburg'
    }
}
for username, user_info in users.items():
    print(f"\nUsername: {username.title()}")
    print(f"\tFullName: {user_info['first'].title()} {user_info['last'].title()}")
    print(f"\tLocation: {user_info['location']}")