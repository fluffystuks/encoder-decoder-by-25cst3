def shift_encrypt(text,shift):
    result = 
    for char in text:
        if char.upper() in RUS_ALPHABET:
            idx = RUS_ALPHABET.index(char.upper())
            new_char = RUS_ALPHABET[(idx+shift)%len(RUS_ALPHABET)]
            if char.islower():
                result+=new_char.lower()
            else:
                result+=new_char
        else:
            result += char
    return result
