from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from handlers.decoder import vigenere_decoder, shift_decrypt, shift_decrypt_ASCII
from handlers.encoder import atbash_encrypt, atbash_encrypt_ASCII

decrypt_state = {}

ABC_RU = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

def decrypt_menu_markup():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Шифр Атбаш (Рус/Англ)", callback_data="decrypt_atbash")],
        [InlineKeyboardButton("Шифр Атбаш по ASCII", callback_data="decrypt_atbash_ascii")],
        [InlineKeyboardButton("Шифр Виженера", callback_data="decrypt_vigenere")],
        [InlineKeyboardButton("Шифр Цезаря (Рус)", callback_data="decrypt_caesar_ru")],
        [InlineKeyboardButton("Шифр Цезаря по ASCII", callback_data="decrypt_caesar_ascii")],
        [InlineKeyboardButton("Назад", callback_data="back_to_main")]
    ])

async def handle_decrypt_button(update, context):
    q = update.callback_query
    d = q.data
    cid = update.effective_chat.id

    if d == "decrypt_vigenere":
        decrypt_state[cid] = {"mode": d, "step": "key"}
        await q.edit_message_text("Введите ключ (только русские буквы):")
        return

    need_shift = d in {"decrypt_caesar_ru", "decrypt_caesar_ascii"}
    decrypt_state[cid] = {"mode": d, "step": "shift" if need_shift else "text"}
    await q.edit_message_text("Введите количество сдвигов:" if need_shift else "Введите текст:")

async def handle_decrypt_text(update, context):
    cid = update.effective_chat.id
    s = decrypt_state.get(cid)
    if not s:
        return

    mode = s["mode"]

    if s["step"] == "shift":
        try:
            s["shift"] = int(update.message.text)
        except ValueError:
            await update.message.reply_text("Введите целое число:")
            return
        s["step"] = "text"
        await update.message.reply_text("Введите текст:")
        return

    if s["step"] == "key":
        key = update.message.text.replace(" ", "")
        if not key:
            await update.message.reply_text("Ключ не может быть пустым. Введите ключ:")
            return
        if not all(ch.upper() in ABC_RU for ch in key):
            await update.message.reply_text("Ключ должен содержать только русские буквы (А-Я, Ё). Введите ключ снова:")
            return
        s["key"] = key
        s["step"] = "text"
        await update.message.reply_text("Введите текст:")
        return

    text = update.message.text

    try:
        if mode == "decrypt_atbash":
            res = atbash_encrypt(text)
        elif mode == "decrypt_atbash_ascii":
            res = atbash_encrypt_ASCII(text)
        elif mode == "decrypt_vigenere":
            res = vigenere_decoder(text, s["key"])
        elif mode == "decrypt_caesar_ru":
            res = shift_decrypt(text, s["shift"])
        elif mode == "decrypt_caesar_ascii":
            res = shift_decrypt_ASCII(text, s["shift"])
        else:
            res = "Неизвестный режим"
    except Exception as e:
        await update.message.reply_text(f"Ошибка при расшифровке: {e}")
        return

    await update.message.reply_text(f"Результат:\n{res}")
    decrypt_state.pop(cid, None)