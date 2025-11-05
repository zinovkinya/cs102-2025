def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    ord_A = ord("A")
    ord_a = ord("a")

    for i in plaintext:
        if i.isupper():
            ciphertext += chr((ord(i) - ord_A + shift) % 26 + ord_A)
        elif i.islower():
            ciphertext += chr((ord(i) - ord_a + shift) % 26 + ord_a)
        else:
            ciphertext += i

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    ord_A = ord("A")
    ord_a = ord("a")
    for i in ciphertext:
        if i.isupper():
            plaintext += chr((ord(i) - ord_A - shift) % 26 + ord_A)
        elif i.islower():
            plaintext += chr((ord(i) - ord_a - shift) % 26 + ord_a)
        else:
            plaintext += i

    return plaintext
