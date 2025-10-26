from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters
from config import TOKEN
from handlers.start import start, handle_buttons
from encrypt import handle_encrypt_button, handle_encrypt_text
from decrypt import handle_decrypt_button, handle_decrypt_text

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_encrypt_button, pattern=r"^encrypt_"))
    app.add_handler(CallbackQueryHandler(handle_decrypt_button, pattern=r"^decrypt_"))
    app.add_handler(CallbackQueryHandler(handle_buttons))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_decrypt_text), group=0)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_encrypt_text), group=1)
    app.run_polling()

if __name__ == "__main__":
    main()
