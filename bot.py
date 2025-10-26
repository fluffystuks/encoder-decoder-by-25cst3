from telegram.ext import Application, CommandHandler, CallbackQueryHandler,MessageHandler,filters
from telegram import BotCommand, MenuButtonCommands
from config import TOKEN
from handlers.start import start, handle_buttons
from encrypt import handle_encrypt_text, handle_encrypt_button
from decrypt import handle_decrypt_text, handle_decrypt_button

async def post_init(app):
    await app.bot.set_my_commands([BotCommand("start", "Запустить бота")])
    await app.bot.set_chat_menu_button(menu_button=MenuButtonCommands())

def main():
    app = (
        Application.builder()
        .token(TOKEN)
        .post_init(post_init)
        .build())
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_buttons))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_encrypt_text))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_decrypt_text))
    app.run_polling()

if __name__ == "__main__":
    main()
