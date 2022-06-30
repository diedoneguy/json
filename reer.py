import secrets
import string

pasword = string.digits+string.ascii_letters
generate = ''.join(secrets.choice(pasword)for i in range(8))

login = input('write login: ')
print(generate)
password = input('write password: ')

