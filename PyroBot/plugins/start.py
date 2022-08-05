from pyrogram import Client, filters
Import requests 
import detectlanguage

detectlanguage.configuration.api_key = "YOUR API KEY"

# Enable secure mode (SSL) if you are passing sensitive data
# detectlanguage.configuration.secure = True

@Client.on_message(filters.command(["start"]))
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text="Hello there!",
        reply_to_message_id=update.message_id
    )

#r = detectlanguage.detect(message)


#cleamimg
@Client.on_message(filters.regex("http") | filters.regex("t.me") | filters.regex("in") | filters.regex("youtu.be") | filters.regex("com") | filters.regex("https") | filters.regex("/" ) | filters.service)
async def delete(bot,message):
if detectlanguage.detect(message) == ar:
    await message.delete()
else:
    await bot.send_message("lmao")
