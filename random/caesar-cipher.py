alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2'
,'3', '4', '5', '6', '7', '8', '9', '0', '!', '@', '$', '?', ' ', '#', '*', '%']

def encrypt():
    cipherText = ""
    # Iterate through each letter in the text
    for letter in text:
        if letter in alphabet:
           position = alphabet.index(letter)
           # Position + Shift establishes new position 
           # Modulus keeps the range within 26 
           newPosition = (position + shift) % 44 
           newLetter = alphabet[newPosition]
           # Add newLetter to empty cipherText string
           # with each iteration of the for loop 
           cipherText += newLetter
    print(f'The encoded output is {cipherText}\n')

def decrypt():
    decipherText = ""
    for letter in text:
        if letter in text: 
            position = alphabet.index(letter)
            originalPosition = (position - shift) % 44
            originalLetter = alphabet[originalPosition]
            decipherText += originalLetter
    print(f'The decoded output is {decipherText}\n')

while True: 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").casefold()
    if direction == "encode":
        text = input("Type your message:\n").casefold()
        try: 
            shift = int(input("Type the shift number:\n"))
        # Prevent code from breaking if a non-integer is entered 
        except ValueError: 
                print("Please enter an integer and try again.")
                break
        encrypt()
    elif direction == "decode":
        text = input("Enter a message to decode:\n").casefold()
        try: 
            shift = int(input("Type the shift number:\n"))
        except ValueError: 
                print("Please enter an integer and try again.")
                break
        decrypt()
    else:
        print("Please enter a valid input.\n")