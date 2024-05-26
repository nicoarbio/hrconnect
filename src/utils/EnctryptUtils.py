import bcrypt

def encrypt_password(password):
    #print(bcrypt.gensalt())
    with open("src/config/password_salt_key") as file:
        salt = file.read().strip()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def verify_password(input_password, hashed_password):
    return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password)