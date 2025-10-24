from telegram import InlineKeyboardButton, InlineKeyboardMarkup


async def start(update, context):
    keyboard = [
        [InlineKeyboardButton("Зашифровать", callback_data="encrypt")],
        [InlineKeyboardButton("Расшифровать", callback_data="decrypt")],
        [InlineKeyboardButton("Библиотека шифров", callback_data="library")]
    ]
    markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Выберите действие:",
        reply_markup =markup
    )


async def handle_buttons(update, context):
    query = update.callback_query
    await query.answer()

    data = query.data
    if data == "encrypt":
        await query.edit_message_text("Пустышка")
    elif data == "decrypt":
        await query.edit_message_text("Пустышка")
    elif data == "library":
        await query.edit_message_text("Пустышка")
    else:
        await query.edit_message_text("Пустышка")