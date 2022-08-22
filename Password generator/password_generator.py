import random
import string

length = int(input("Length of password: "))


def password_generator(size=length, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits
                       + string.punctuation):
    return "".join(random.choice(chars) for _ in range(size))


print(password_generator(length))
