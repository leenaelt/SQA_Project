def login(username, password):
    # stored credentials (simulate database)
    correct_username = "admin"
    correct_password = "1234"

    if not username or not password:
        raise ValueError("Username and password cannot be empty")

    if username == correct_username and password == correct_password:
        return True
    else:
        return False
