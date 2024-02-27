from letter import alphabet
def caesar_cipher_encrypt(encrypt_direction, plain_text, shift_amount):
  messages = ""
  if encrypt_direction == "decode":
    shift_amount *= -1
  for char in plain_text:
    if char in alphabet:
      alphabet_index = alphabet.index(char)
      alphabet_shift_up = alphabet_index + shift_amount
      messages += alphabet[alphabet_shift_up]
    else:
      messages += char
  print(f"The {encrypt_direction}d is {messages}")

