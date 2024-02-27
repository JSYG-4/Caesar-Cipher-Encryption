from caesar_cipher_method import caesar_cipher_encrypt
import os

stop = False
while not stop:
    os.system('cls')
    direct = input("Want to Encode or Decode messages?").lower()
    text = input("Type your message here:").lower()
    shift = int(input("shift amount:"))
    shift2 = shift % 26
    caesar_cipher_encrypt(encrypt_direction=direct, plain_text=text, shift_amount=shift2)
    again = input("Type 'yes' to repeat, 'no' to exit program?" ).lower()
    if again == "no":
        stop = True
    