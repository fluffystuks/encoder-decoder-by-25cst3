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
