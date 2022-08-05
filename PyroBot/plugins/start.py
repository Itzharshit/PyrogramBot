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
@Client.on_message(filters.reply & filters.text & ~filters.private & ~filters.edited)
async def delete(bot,message):
if detectlanguage.simple_detect(message) == ar:
    await message.delete()
else:
    print("fine")
