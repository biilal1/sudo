from pyrogram import Client, idle
from config import API_ID, API_HASH, BOT_TOKEN
from pyromod import listen



bot = Client(
    "mo",
    api_id="15837209",
    api_hash="fe081df6989a4d79c1004903bb4f23e6",
    bot_token="7458575860:AAF7p06f6BtVVdDGuhWrNQIP-O5TQNzWc1A",
    plugins=dict(root="Maker")
    )

async def start_bot():
    print("[INFO]: STARTING BOT CLIENT")
    await bot.start()
    AFROTOO = "N_7_K"
    await bot.send_message("N_M_7_U", "**تم تشغيل ال صانع بنجاح عزيزي المطور ...🥀،**")
    print("[INFO]: تم تشغيل الصانع وارسال رسالة للمطور⚡🚦.")
    await idle()
