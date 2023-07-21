
import asyncio
import os
import contextlib
import random
import sys
from asyncio.exceptions import CancelledError
import requests
import heroku3
import re
import urllib3
from telethon import events 
from SHRU import HEROKU_APP, UPSTREAM_REPO_URL, l313l
from ..core.managers import edit_delete, edit_or_reply
from telethon.events import NewMessage
from telethon import event
from telethon.tl import types

from telethon.utils import get_display_name
plugin_category = "utils"



@l313l.ar_cmd(
    pattern="عدد$",
    command=("عدد", plugin_category),
    info={
        "header": "Count the number of lines in a message.",
        "usage": "{tr}عدد (reply to a message)",
    },
)
async def count_lines(event):
    reply = await event.get_reply_message()
    if not reply or not reply.message:
        return await edit_or_reply(event, "⌔∮ يرجى الرد على الرسالة لحساب عدد الأسطر.")
    lines = reply.message.split("\n")
    count = len(lines)
    await edit_or_reply(event, f"⌔∮ عدد الأسطر في الرسالة: {count}")


ashour = [
    "أَقِيمُوا الْعَزَاء اُذْكُرُوا سِّيِّد الشَّبَاب قتييل كَرْبَلا ءاِبْن عَلِيّ والزهراء",
    "سأمضي وما بالموت عارٌ على الفتى * إذا ما نوى حقاً وجاهد مسلمًا.",
    "فهل إلاّ الموت ؟ فمرحباً به",
    "أيّها الناس نافِسوا في المكارم وسارعوا في المغانِم.",
    "نَفْسِ مَنْ بَعْدِ الْحُسَيْن هَوِّنِي وَبَعْدَهُ لَا كُنْتِ أَوْ تَكُونِي",
    "هَذَا الْحُسَيْن شَارِب الْمَنُون وتشربين بَارِد الْمُعَيَّن",
    "هَيْهَاتَ مَا هَذَا فَعَّال دِينِي وَلَا فِعَالَ صَادِقٌ الْيَقِين",
    "وَاَللَّه لو قطعـتموا يمـيني",
    "يَا نَفْسُ لَا تخـشي مِن الكفار",
    "نَفْسِ مَنْ بَعْدِ الْحُسَيْن هَوِّنِي وَبَعْدَهُ لَا كُنْتِ أَوْ تَكُونِي",
]

@l313l.ar_cmd(
    pattern="عاشوراء$",
    command=("عاشوراء", plugin_category),
    info={
        "header": "Get random qusts about عاشوراء (Ashura).",
        "usage": "{tr}عاشوراء",
    },
)
async def ashura_info(event):
    # Choose a random fact from the list
    ahsouralshen = random.choice(ashour)
    await edit_or_reply(event, ahsouralshen)
