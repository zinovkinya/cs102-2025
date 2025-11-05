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
    ord_A = ord("A")
    ord_a = ord("a")
    for key_index, char in enumerate(plaintext):
        if char.isalpha():
            key_char = keyword[key_index % len(keyword)]
            if key_char.isupper():
                shift = ord(key_char) - ord_A
            else:
                shift = ord(key_char) - ord_a

            if char.isupper():
                new_pos = (ord(char) - ord_A + shift) % 26
                new_char = chr(new_pos + ord_A)
            else:
                new_pos = (ord(char) - ord_a + shift) % 26
                new_char = chr(new_pos + ord_a)

            ciphertext += new_char
        else:
            ciphertext += char
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
    ord_A = ord("A")
    ord_a = ord("a")
    for key_index, char in enumerate(ciphertext):
        if char.isalpha():
            key_char = keyword[key_index % len(keyword)]
            if key_char.isupper():
                shift = ord(key_char) - ord_A
            else:
                shift = ord(key_char) - ord_a
            if char.isupper():
                new_pos = (ord(char) - ord_A - shift) % 26
                new_char = chr(new_pos + ord_A)
            else:
                new_pos = (ord(char) - ord_a - shift) % 26
                new_char = chr(new_pos + ord_a)
            plaintext += new_char
        else:
            plaintext += char
        key_index += 1
    return plaintext
