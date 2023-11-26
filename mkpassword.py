import string
import secrets


length = 15
# Choose wide set of characters, but consider what your system can handle
alphabet = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(alphabet) for i in range(length))
print(f"You new password is: {password}")
