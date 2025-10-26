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