# import string
# import random

# chars = " " + string.punctuation + string.digits + string.ascii_letters
# chars = list(chars)
# key = chars.copy()

# random.shuffle(key)

# print(f"Chars: {chars}")
# print(f"Key  : {key}")

# # Encrypt

# plain_text = input("Enter a message to encrypt:")
# cipher_text = ""

# for letter in plain_text:
#     index = chars.index(letter)
#     cipher_text += key[index]

# print(f"The original message :{plain_text}")
# print(f"The encrypted message:{cipher_text}")

# #decrypt
# cipher_text = input("Enter a message to decrypt:")
# plain_text = ""

# for letter in cipher_text:
#     index = key.index(letter)
#     plain_text += chars[index]

# print(f"The encrypted message:{cipher_text}")
# print(f"The original message :{plain_text}")            

arr = [1, 2, 3, 4, 5]

for i, num in enumerate(arr):
    print(i, num)