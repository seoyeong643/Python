def login(database, username, password):
    print()
    if username in database.keys():
        if password == database[username]:
            print(f"{username} is logged in.")
            return username
        else:
            print(f"Password failed for username: {username}")
            return ""

    else:
        print(f"Invalid username: {username}. Please try again.")
        return ""

def register(database, username):
    print()
    if username not in database.keys():
        return username
    else:
        print("Username is already registered.")
        return ""