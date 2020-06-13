from string import ascii_uppercase


def encrypt(plain_text, repeating_key):
    """
    This function will encrypt a message with Vigenère Cipher

    @param:
        - plain_text: the message to be encrypt [STRING]
        - repeating_key : the key with whom we encrypt & decrypt the message [STRING]

    @return:
        - encrypted message [STRING]
    """

    # Remove characters that are not upper-cases
    plain_text = ''.join(letter for letter in plain_text if letter.isupper())

    # Reduce spaces
    plain_text = plain_text.replace(" ", "")

    # Duplicate the key so that it will be in the length of the text
    repeating_key = repeating_key * (len(plain_text) // len(repeating_key) + 1)

    # Encrypt each letter from the message with the key
    return "".join(map(lambda mi, ki: chr(((ord(mi) - 65 + ord(ki) - 65) % 26) + 65), plain_text, repeating_key))


def decrypt(cipher_text, repeating_key):
    """
    This function will decrypt a message with Vigenère Cipher

    @param:
        - cipher_text   : encrypted message [STRING]
        - repeating_key : the key with whom we encrypt & decrypt the message [STRING]
    @return:
        - The original message we encrypt [STRING]
    """

    # Duplicate the key so that it will be in the length of the text
    repeating_key = repeating_key * (len(cipher_text) // len(repeating_key) + 1)

    # Decrypt each letter from the message with the key
    return "".join(map(lambda mi, ki: chr(((ord(mi) - 65 - ord(ki) - 65) % 26) + 65), cipher_text, repeating_key))


print(encrypt("HELLO WORLD", "POPOD"))
print(decrypt("WSAZRLCGZG", "POPOD"))