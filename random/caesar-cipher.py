alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt():
    cipherText = ""
    # Iterate through each letter in the text
    for letter in text:
        if letter in alphabet:
           position = alphabet.index(letter)
           # Position + Shift establishes new position 
           # Modulus keeps the range within 26 
           newPosition = (position + shift) % 26 
           newLetter = alphabet[newPosition]
           # Add newLetter to empty cipherText string
           # with each iteration of the for loop 
           cipherText += newLetter
    print(f'The encoded output is {cipherText}')

def decrypt():
    decipherText = ""
    for letter in text:
        if letter in text: 
            position = alphabet.index(letter)
            originalPosition = (position - shift) % 26
            originalLetter = alphabet[originalPosition]
            decipherText += originalLetter
    print(f'The decoded output is {decipherText}')

decrypt()