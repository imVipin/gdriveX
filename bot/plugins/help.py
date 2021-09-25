from bot import SUPPORT_CHAT_LINK
from pyrogram import Client, filters
from bot.config import Messages as tr
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#from pyrogram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant, UserBannedInChannel


from forcesub import ForceSub


TB = [
           [
             InlineKeyboardButton(text = 'Creator', url = "https://t.me/OO7ROBot"),
             InlineKeyboardButton(text = 'Other bots', url = "https://t.me/mybotzlist")
            ],
            [InlineKeyboardButton(text = '⭕ Update Channel ⭕', url = "https://t.me/MyTestBotZ")]

        ]

@Client.on_message(filters.private & filters.incoming & filters.command(['start']), group=2)
def _start(client, message):
           
    if UPDATE_CHANNEL = "MyTestBotZ":
        try:
            user = await bot.get_chat_member(UPDATE_CHANNEL, update.from_user.id)
            if user.status == "kicked":
              await bot.edit_message_text(text="You are Banned", message_id=fmsg.message_id)
              return
        except UserNotParticipant:
            await bot.edit_message_text(chat_id=update.chat.id, text="join my update channel", message_id=fmsg.message_id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="😎 Join Channel 😎", url=f"https://telegram.me/MyTestBotZ")]]))
            return
        except Exception:
            await bot.edit_message_text(chat_id=update.chat.id, text="something wrong", message_id=fmsg.message_id)
            return
           
           
    #forcesub = ForceSub(client, message)
    #if forcesub == 400:
        #return
    client.send_message(chat_id = message.chat.id,
        text = tr.START_MSG.format(message.from_user.mention),
        reply_markup = InlineKeyboardMarkup(TB),                 
        reply_to_message_id = message.message_id
    )

    
@Client.on_message(filters.private & filters.incoming & filters.command(['about']), group=2)
def _about(client, message):
        client.send_message(chat_id = message.chat.id,
                                    text = tr.ABOUT_MSG.format(message.from_user.mention),
                                    reply_markup = InlineKeyboardMarkup(TB),
                                    reply_to_message_id = message.message_id
                           )
        
        
@Client.on_message(filters.private & filters.incoming & filters.command(['help']), group=2)
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(c, callback_query):
    chat_id = callback_query.from_user.id
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    c.edit_message_text(chat_id = chat_id,    message_id = message_id,
        text = tr.HELP_MSG[msg],    reply_markup = InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if(pos==1):
        button = [
            [InlineKeyboardButton(text = 'Next⇨', callback_data = "help+2")]
        ]
    elif(pos==len(tr.HELP_MSG)-1):

        button = [
            [
             InlineKeyboardButton(text = '©️Update Channel', url = "https://t.me/MyTestBotZ"),
             InlineKeyboardButton(text = 'Other bots', url = "https://t.me/mybotzlist")
            ],
            [InlineKeyboardButton(text = '⇦Back', callback_data = f"help+{pos-1}")]

        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '⇦Back', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = 'Next⇨', callback_data = f"help+{pos+1}")
            ],
        ]
    return button
