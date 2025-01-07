alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(start_text,shift_amount,cipher_direction):
    end_text=""
    if cipher_direction=="decode":
        shift_amount*=-1
    for char in start_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position+shift_amount)%len(alphabet)#handling wrapping around of alphabet using modulo operator
            end_text+=alphabet[new_position]
        else:
            end_text+=char
    print(f"Here's the {cipher_direction}d result: {end_text}")    
from art_caesar_cipher import logo
print(logo)
choice="yes"
while choice=="yes":

    type=input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text= input("Type your message:\n").lower()
    shift=int(input("Type the shift number:\n"))
    
    caesar(text,shift,type)
    choice=input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
