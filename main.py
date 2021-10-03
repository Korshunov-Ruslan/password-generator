import random
import string

print('How many passwords do you want?')
passwords_count = int(input())
print('What password length do you prefer?')
passwords_length = int(input())


LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation

PASSWORD_DICTIONARY = LETTERS+NUMBERS+PUNCTUATION


def password_generator():
    for i in range(passwords_count):
        password = ''
        for j in range(passwords_length):
            password += random.choice(PASSWORD_DICTIONARY)
        return password


def password_output():
    answer = f"Your password is ready: {password_generator()}"
    if passwords_length < 5:
        print('Are you sure? Thats to eassy? \nPlease, answer "Yes" or "No"')
        passwords_length_sure = (input())
        if passwords_length_sure == 'Yes':
            print(answer)
        else:
            print('See you next time')
    else:
        print(answer)


if __name__ == '__main__':
    password_generator()
    password_output()
