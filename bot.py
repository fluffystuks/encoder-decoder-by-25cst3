from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from telegram import BotCommand, MenuButtonCommands
from config import TOKEN
from handlers.start import start, handle_buttons

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
    app.run_polling()

if __name__ == "__main__":
    main()
