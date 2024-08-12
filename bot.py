from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from pyromod import listen



bot = Client(
    "mo",
    api_id="9671629",
    api_hash="be5c84e9dc1ca0e2b53d54b71e575124",
    bot_token="7390916656:AAHpWUbR2v9v1ogI8EmrnkO1ujc8NXevp1s",
    plugins=dict(root="Maker")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    AFROTOO = "BDB0B"
    await bot.send_message("BDB0B", "**تم تشغيل ال صانع بنجاح عزيزي المطور ...🥀،**")
    print("[INFO]: تم تشغيل الصانع وارسال رسالة للمطور⚡🚦.")
    await idle()
