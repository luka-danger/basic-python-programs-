alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt():
    cipherText = ""
    for letter in text: 
     position = alphabet.index(letter)
     newPosition = position + shift 
     if newPosition > 26:
        newLetter = alphabet[0 + shift]
        cipherText += newLetter
     else:
       newLetter = alphabet[newPosition]
       cipherText += newLetter
    print(f'The encoded output is {cipherText}')

# There is a bug in the code. encrypyt() works, but if it reaches a letter past 
# 'z', rather than starting over and iterating through the alphabet again, 
# it breaks and throws an out of range error 
    
encrypt()


    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

#TODO-3: Call the encrypt function and pass in the user inputs. 
# You should be able to test the code and encrypt a message. 