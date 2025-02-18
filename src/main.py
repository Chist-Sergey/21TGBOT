import telegram.ext as tge
import telegram as tg
import os
import dotenv


async def reply_on_mention(
    update: tg.Update,
    context: tge.ContextTypes.DEFAULT_TYPE
) -> None:
    if context.bot.username in update.message.text:
        await context.bot.send_message(
            chat_id=update.effective_message.chat_id,
            text=f"Засунь {update.message.text} в очко.",
            reply_to_message_id=update.message.message_id
        )


if __name__ == '__main__':
    # bot's key can now be accessed via 'getenv'
    dotenv.load_dotenv()

    bot = tge.ApplicationBuilder().token(os.getenv('TOKEN')).build()
    bot.add_handler(tge.MessageHandler(tge.filters.TEXT, reply_on_mention))
    bot.run_polling(poll_interval=2.0)  # 'poll_interval' is in seconds
