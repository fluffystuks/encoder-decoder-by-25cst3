def vigenere_decoder(text, key, decrypt=True):
    abc = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    res = ""
    for i, ch in enumerate(text.upper()):
        if ch not in abc:
            res += ch
            continue
        t = abc.index(ch)
        k = abc.index(key[i % len(key)].upper())
        res += abc[(t - k if decrypt else t + k) % len(abc)]
    return res

def shift_encrypt_ASCII(text, shift):
    result = ""
    for char in text:
        code = ord(char)
        if 32 <= code <= 126:
            if code + shift > 126:
                new_code = 32 + ((code + shift) - 127)
            elif code + shift < 32:
                new_code = 127 - (32 - (code + shift))
            else:
                new_code = code + shift
            result += chr(new_code)
        else:
            result += char
    return result
