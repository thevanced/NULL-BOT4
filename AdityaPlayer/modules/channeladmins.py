# Aditya Player - Telegram bot for streaming audio in group calls
# Copyright (C) 2021  Aditya Halder

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from asyncio import QueueEmpty
from AdityaPlayer.config import que
from pyrogram import Client, filters
from pyrogram.types import Message

from AdityaPlayer.function.admins import set
from AdityaPlayer.helpers.channelmusic import get_chat_id
from AdityaPlayer.helpers.decorators import authorized_users_only, errors
from AdityaPlayer.helpers.filters import command, other_filters
from AdityaPlayer.services.callsmusic import callsmusic
from AdityaPlayer.services.queues import queues


@Client.on_message(filters.command(["channelpause","cpause"]) & filters.group & ~filters.edited)
@errors
@authorized_users_only
async def pause(_, message: Message):
    try:
      conchat = await _.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("**❗ Ɩs Ƭɦɩs Ƈɦɑʈ Eⱱɘɳ Łɩɳƙɘɗ ❓**")
      return    
    chat_id = chid
    if (chat_id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[chat_id] == "paused"
    ):
        await message.reply_text("**🚫 Ɲøʈɦɩɳʛ ɩs Ƥɭɑƴɩɳʛ ❗️**")
    else:
        callsmusic.pytgcalls.pause_stream(chat_id)
        await message.reply_text("**▶ ️Sʋƈƈɘssƒʋɭɭƴ Ƥɑʋsɘɗ ❗**️")


@Client.on_message(filters.command(["channelresume","cresume"]) & filters.group & ~filters.edited)
@errors
@authorized_users_only
async def resume(_, message: Message):
    try:
      conchat = await _.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("**❗ Ɩs Ƭɦɩs Ƈɦɑʈ Eⱱɘɳ Łɩɳƙɘɗ ❓**")
      return    
    chat_id = chid
    if (chat_id not in callsmusic.pytgcalls.active_calls) or (
        callsmusic.pytgcalls.active_calls[chat_id] == "playing"
    ):
        await message.reply_text("**🚫 Ɲøʈɦɩɳʛ ɩs Ƥɑʋsɘɗ ❗**")
    else:
        callsmusic.pytgcalls.resume_stream(chat_id)
        await message.reply_text("**⏸ ️Sʋƈƈɘssƒʋɭɭƴ Ʀɘsʋɱɘɗ ❗**")


@Client.on_message(filters.command(["channelend","cend"]) & filters.group & ~filters.edited)
@errors
@authorized_users_only
async def stop(_, message: Message):
    try:
      conchat = await _.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("**❗ Ɩs Ƭɦɩs Ƈɦɑʈ Eⱱɘɳ Łɩɳƙɘɗ ❓**")
      return    
    chat_id = chid
    if chat_id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("**🚫 Ɲøʈɦɩɳʛ ɩs Sʈɤɘɑɱɩɳʛ ❗**")
    else:
        try:
            callsmusic.queues.clear(chat_id)
        except QueueEmpty:
            pass

        callsmusic.pytgcalls.leave_group_call(chat_id)
        await message.reply_text("**❌ Sʋƈƈɘssƒʋɭɭƴ Sʈøƥƥɘɗ Sʈɤɘɑɱɩɳʛ ❗**")


@Client.on_message(filters.command(["channelskip","cskip"]) & filters.group & ~filters.edited)
@errors
@authorized_users_only
async def skip(_, message: Message):
    global que
    try:
      conchat = await _.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("**❗ Ɩs Ƭɦɩs Ƈɦɑʈ Eⱱɘɳ Łɩɳƙɘɗ ❓**")
      return    
    chat_id = chid
    if chat_id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text("**🚫 Ɲøʈɦɩɳʛ ɩs Ƥɭɑƴɩɳʛ ʈø Sƙɩƥ ❗**")
    else:
        callsmusic.queues.task_done(chat_id)

        if callsmusic.queues.is_empty(chat_id):
            callsmusic.pytgcalls.leave_group_call(chat_id)
        else:
            callsmusic.pytgcalls.change_stream(
                chat_id, callsmusic.queues.get(chat_id)["file"]
            )

    qeue = que.get(chat_id)
    if qeue:
        skip = qeue.pop(0)
    if not qeue:
        return
    await message.reply_text(f"**⏩ Sƙɩƥƥɘɗ** **{skip[0]}**\n**▶️ Ɲøω Ƥɭɑƴɩɳʛ** **{qeue[0][0]}**")


@Client.on_message(filters.command("channeladmincache"))
@errors
async def admincache(client, message: Message):
    try:
      conchat = await client.get_chat(message.chat.id)
      conid = conchat.linked_chat.id
      chid = conid
    except:
      await message.reply("**❗ Ɩs Ƭɦɩs Ƈɦɑʈ Eⱱɘɳ Łɩɳƙɘɗ ❓**")
      return
    set(
        chid,
        [
            member.user
            for member in await conchat.linked_chat.get_members(filter="administrators")
        ],
    )
    await message.reply_text("**✅ Ʌɗɱɩɳ Ƈɑƈɦɘ Ʀɘƒɤɘsɦɘɗ ❗️**")

