# import rsa
#
# string = input()
#
# print(string.encode("utf-8"))
# str.decode("utf-8").replace(u"\u2022", "*")

# special = u"\u2022"
# abc = u'ABC•def'
# abc_new = abc.replace(special, 'X')
# print(abc_new)

# abc.encode().decode('unicode-escape')
# abc_new = abc.replace('•','something')
# print(abc_new)

# try:
#     with open('../../cs_1400_notes/common_errors.txt', 'r') as f:
#         ...
# except OSError:
#     # 'File not found' error message.
#     print("Fichier non trouvé")
#
# print(chr(977))
# print(chr(57344))
#
# bytes.decode()

alphabet = "abcdefghijklmnopqrstuvwxyz"
key = 5

def encrypt(message):
    """
    encrypts a message taken from user input. can only take in lowercase letters in the us alphabet
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
    encrypt_message = encrypt(input('enter the message: '))
    print(encrypt_message)
    decrypt_message = decrypt(encrypt_message)
    print(decrypt_message)

if __name__ == "__main__":
    main()

