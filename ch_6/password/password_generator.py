import random


def create_password_generator(string):
    def generate_password(length):
        return "".join(random.choices(string, k=length))

    return generate_password


alpha_password = create_password_generator("abcdef")
print(alpha_password(5))
