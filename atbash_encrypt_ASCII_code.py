
def atbash_encrypt_ASCII(text):
    result = ""
    for char in text:
        code = ord(char)
        if 32 <= code <= 126:
            new_code = 32 + (126 - code)
            result += chr(new_code)
        else:
            result += char
    return result
