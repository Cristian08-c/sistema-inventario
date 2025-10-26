from passlib.context import CryptContext

pwd = CryptContext(schemes="bcrypt")

def hash_password(StringPassword:str):
    return pwd.hash(StringPassword)


def verifypassword(StringPassword:str, PwdPassword:str):
    return pwd.verify(StringPassword,PwdPassword)