alphabet = "abcdefghijklmnopqrstuvwxyz"
key = 5 # the amount of letters forward in the alphabet we will change each letter to

def encrypt(message):
    """
    Encrypts a message taken from user input. Can only take in lowercase letters in the English alphabet
    as a parameter
    :return: the encrypted message
    """
    encrypt_message = ""
    for i in message:
        position = alphabet.find(i)
        encrypt_position = (position + key) % 26
        encrypt_message = encrypt_message + alphabet[encrypt_position]

    return encrypt_message

def decrypt(encrypt_message):
    """
    decrypts a message
    :param encrypt_message: what is returned by the encrypt() function
    :return: the decrypted message
    """
    decrypt_message = ""
    for i in encrypt_message:
        position = alphabet.find(i)
        decrypt_position = (position - key) % 26
        decrypt_message = decrypt_message + alphabet[decrypt_position]

    return decrypt_message

def main():
    encrypt_message = encrypt(input('Enter your message. Only enter lowercase letters from the English alphabet: '))
    print('Your encrypted message is: ', encrypt_message)
    decrypt_message = decrypt(encrypt_message)
    print('Your decrypted message is: ', decrypt_message)

if __name__ == "__main__":
    main()

