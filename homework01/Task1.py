def encrypt_atbash(plaintext: str) -> str:
    rus_lower = [chr(i) for i in range(1072, 1104)]
    rus_lower = rus_lower[:6] + ["ё"] + rus_lower[6:]

    rus_upper = [chr(i) for i in range(1040, 1072)]
    rus_upper = rus_upper[:6] + ["Ё"] + rus_upper[6:]

    alphabet_lower = "".join(rus_lower)
    alphabet_upper = "".join(rus_upper)

    mapping = {}
    for i in range(33):
        mapping[alphabet_lower[i]] = alphabet_lower[32 - i]
        mapping[alphabet_upper[i]] = alphabet_upper[32 - i]

    result = ""
    for char in plaintext:
        result += mapping.get(char, char)

    return result
