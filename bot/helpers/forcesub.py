import asyncio
import os
#from config import Config
from pyrogram import Client
from pyrogram.errors import FloodWait, UserNotParticipant
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "MyTestBotZ")
    
async def ForceSub(bot: Client, cmd: Message):
    try:
        user = await bot.get_chat_member(chat_id=(int(UPDATES_CHANNEL) if UPDATES_CHANNEL.startswith("-100") else UPDATES_CHANNEL), user_id=cmd.from_user.id)
        if user.status == "kicked":
            await bot.send_message(
                chat_id=cmd.from_user.id,
                text="Sorry man, You are Banned to use me...",
                parse_mode="markdown",
                disable_web_page_preview=True
            )
            return 400
    except UserNotParticipant:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="**Please Join My Updates Channel to use this Bot!**\n\nDue to Overload, Only Channel Subscribers can use the Bot!",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔔 Join Updates Channel", url="https://t.me/MyTestBotZ")
                    ]
                ]
            ),
            parse_mode="markdown"
        )
        return 400
    except Exception:
        await bot.send_message(
            chat_id=cmd.from_user.id,
            text="Something went Wrong. Contact @OO7ROBOT\n\n**© @MyTestBotZ**",
            parse_mode="markdown",
            disable_web_page_preview=True
        )
        return 400
    return 200
