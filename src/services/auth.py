import os


def get_valid_users() -> dict:
    """
    Load users from a single USERS env variable in the format:
    'user1:pass1,user2:pass2'
    Returns:
        A dictionary {username: password}
    """
    users_str = os.getenv("USERS", "")
    users = {}
    for pair in users_str.split(","):
        if ":" in pair:
            username, password = pair.strip().split(":", 1)
            users[username] = password
    return users


def authenticate_user(username: str, password: str) -> bool:
    """
    Validates username and password from the env-stored users.
    """
    valid_users = get_valid_users()
    return valid_users.get(username) == password
