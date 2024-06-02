import bcrypt

def encrypt_password(password):
    #salt = bcrypt.gensalt()
    with open("src/config/password_salt_key.env") as file:
        salt = file.read().strip()
    try:
        return bcrypt.hashpw(password.encode('utf-8'), salt)
    except ValueError:
        return ""


def verify_password(input_password, hashed_password):
    try:
        return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password)
    except ValueError:
        return False
