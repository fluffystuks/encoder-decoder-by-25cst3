RUS_ALPHABET = [
    "А", "Б", "В", "Г", "Д", "Е", "Ё", "Ж", "З", "И", "Й", "К", "Л", "М",
    "Н", "О", "П", "Р", "С", "Т", "У", "Ф", "Х" "Ц", "Ч", "Ш", "Щ", "Ъ",
    "Ы", "Ь", "Э", "Ю", "Я"
]

def atbash_encrypt(text):
    result = ""
    for char in text:
        if char.upper() in RUS_ALPHABET:
            idx = RUS_ALPHABET.index(char.upper())
            new_char = RUS_ALPHABET[-(idx + 1)]
            if char.islower():
                result += new_char.lower()
            else:
                result += new_char
        else:
            result += char
    return result
  
  def vigenere_encoder(text, key, decrypt=False):
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
