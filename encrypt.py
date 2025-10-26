from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from handlers.encoder import atbash_encrypt, atbash_encrypt_ASCII, vigenere_encoder, shift_encrypt, shift_encrypt_ASCII

encrypt_state = {}

def encrypt_menu_markup():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("Шифр Атбаш (Рус/Англ)", callback_data="encrypt_atbash")],
        [InlineKeyboardButton("Шифр Атбаш по ASCII", callback_data="encrypt_atbash_ascii")],
        [InlineKeyboardButton("Шифр Виженера", callback_data="encrypt_vigenere")],
        [InlineKeyboardButton("Шифр Цезаря (Рус)", callback_data="encrypt_caesar_ru")],
        [InlineKeyboardButton("Шифр Цезаря по ASCII", callback_data="encrypt_caesar_ascii")],
        [InlineKeyboardButton("Назад", callback_data="back_to_main")]
    ])

async def handle_encrypt_button(update, context):
    q = update.callback_query
    d = q.data
    cid = update.effective_chat.id

    if d == "encrypt_vigenere":
        encrypt_state[cid] = {"mode": d, "step": "key"}
        await q.edit_message_text("Введите ключ (только русские буквы):")
        return

    need_shift = d in {"encrypt_caesar_ru", "encrypt_caesar_ascii"}
    encrypt_state[cid] = {"mode": d, "step": "shift" if need_shift else "text"}
    await q.edit_message_text("Введите количество сдвигов:" if need_shift else "Введите текст:")

async def handle_encrypt_text(update, context):
    cid = update.effective_chat.id
    s = encrypt_state.get(cid)
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
        s["key"] = update.message.text.replace(" ", "")
        s["step"] = "text"
        await update.message.reply_text("Введите текст:")
        return

    text = update.message.text
    if mode == "encrypt_atbash":
        res = atbash_encrypt(text)
    elif mode == "encrypt_atbash_ascii":
        res = atbash_encrypt_ASCII(text)
    elif mode == "encrypt_vigenere":
        res = vigenere_encoder(text, s["key"])
    elif mode == "encrypt_caesar_ru":
        res = shift_encrypt(text, s["shift"])
    elif mode == "encrypt_caesar_ascii":
        res = shift_encrypt_ASCII(text, s["shift"])

    await update.message.reply_text(f"Результат:\n{res}")
    encrypt_state.pop(cid, None)