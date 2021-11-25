#### Caesar Cipher Implementation ####
import caesar_cipher_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# print logo
print(caesar_cipher_art.logo)

# caesar cipher implementation
def caesar_cipher(plain_text, shift_index, operation_type):
    caesar_cipher_text = ''
    index = 0
    for letter in plain_text:
        if operation_type == 'encode':
            # if the text is symbol or number then keep it intact
            if letter in alphabet:
                index = alphabet.index(letter) + shift_index
                # case when the index exceeds the 26 letters count
                if index > 25:
                    # subtracted the index value with 26 because the list starts with 0
                    index = index - 26
                caesar_cipher_text += alphabet[index]
            else:
                 caesar_cipher_text += letter        
        elif operation_type == 'decode':
            # if the text is symbol or number then keep it intact
            if letter in alphabet:
                index = alphabet.index(letter) - shift_index
                caesar_cipher_text += alphabet[index]
            else:
                caesar_cipher_text += letter
        else:
            print(f'You selected an incorrect caesar cipher operation.')
    print(f'The {operation_type}d result is: {caesar_cipher_text}')

user_choice = True
while(user_choice):
    user_wish = input('Type \'yes\' if you want to go again. ').lower()
    if user_wish == 'yes':
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar_cipher(plain_text=text, shift_index=shift, operation_type=direction)
    else:
        user_choice = False
