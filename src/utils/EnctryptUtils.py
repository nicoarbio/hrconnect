import bcrypt


def encrypt_password(password):
    #salt = bcrypt.gensalt()
    with open("src/hrconnect/config/salt_key") as file:
        salt = file.read().encode('utf-8')
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')


def verify_password(input_password, hashed_password):
    return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password)
