from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from encrypt import encrypt_menu_markup, handle_encrypt_button
from decrypt import decrypt_menu_markup, handle_decrypt_button

async def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Зашифровать", callback_data="encrypt")],
        [InlineKeyboardButton("Расшифровать", callback_data="decrypt")]
    ]
    await update.message.reply_text("Выберите действие:", reply_markup=InlineKeyboardMarkup(keyboard))

async def handle_buttons(update, context):
    q = update.callback_query
    await q.answer()
    d = q.data

    if d == "encrypt":
        await q.edit_message_text("Выберите тип шифрования:", reply_markup=encrypt_menu_markup())
        return
    if d == "decrypt":
        await q.edit_message_text("Выберите тип расшифровки:", reply_markup=decrypt_menu_markup())
        return

    if d.startswith("encrypt_"):
        await handle_encrypt_button(update, context)
        return
    if d.startswith("decrypt_"):
        await handle_decrypt_button(update, context)
        return

    if d == "back_to_main":
        keyboard = [
            [InlineKeyboardButton("Зашифровать", callback_data="encrypt")],
            [InlineKeyboardButton("Расшифровать", callback_data="decrypt")]
        ]
        await q.edit_message_text("Выберите действие:", reply_markup=InlineKeyboardMarkup(keyboard))
        return