def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            key_char = keyword[key_index % len(keyword)]
            if key_char.isupper():
                shift = ord(key_char) - ord("A")
            else:
                shift = ord(key_char) - ord("a")

            if char.isupper():
                new_pos = (ord(char) - ord("A") + shift) % 26
                new_char = chr(new_pos + ord("A"))
            else:
                new_pos = (ord(char) - ord("a") + shift) % 26
                new_char = chr(new_pos + ord("a"))

            ciphertext += new_char
        else:
            ciphertext += char
        key_index += 1
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            key_char = keyword[key_index % len(keyword)]
            if key_char.isupper():
                shift = ord(key_char) - ord("A")
            else:
                shift = ord(key_char) - ord("a")
            if char.isupper():
                new_pos = (ord(char) - ord("A") - shift) % 26
                new_char = chr(new_pos + ord("A"))
            else:
                new_pos = (ord(char) - ord("a") - shift) % 26
                new_char = chr(new_pos + ord("a"))
            plaintext += new_char
        else:
            plaintext += char
        key_index += 1
    return plaintext
