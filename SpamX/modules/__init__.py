from SpamX.config import *
from SpamX.core.version import __version__
from SpamX import sudoser, RiZoeL 
from RiZoeLX import __version__ as pip_vr
from pyrogram import __version__ as pyro_vr
import platform

__version__ = __version__


ping_msg = PING_MSG if PING_MSG else "🇻ιρ 🇩𝚒𝚝𝚝𝚘 🇺𝚜𝚎𝚛𝚋𝚘𝚝"
pic = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/469fb71dee02e7af0fabc.jpg"
amsg = ALIVE_MSG if ALIVE_MSG else "🇻ιρ 🇩𝚒𝚝𝚝𝚘 🇺𝚜𝚎𝚛𝚋𝚘𝚝"

try:
   sah = RiZoeL.get_users(OWNER_ID)
   owner_mention = sah.mention
except:
   owner_mention = f"[{OWNER_ID}](tg://user?id={OWNER_ID})"

class Alive:
     Pic = pic
     
     msg = f"""
**⁂ {amsg} ⁂**

━───────╯•╰───────━
➠ **σωиεя:** {owner_mention}
➠ ** ⩔єяនɨ០ɳ:** `{platform.python_version()}`
➠ **◈ 𝗨នєя𝗕០Ƭ ⩔єяនɨ០ɳ:** `{__version__}`
➠ **Ƥʏяσɢяαм ⩔єяនɨ០ɳ:** `{pyro_vr}`
➠ **Ɖιттσ ⩔єяនɨ០ɳ:** `{pip_vr}`
➠ **Ɔнαииɛℓ:** @DPZ_BY_DITTO
━───────╮•╭───────━
➠ **Source Code:** [𝗠𝗬😘𝗙𝗔𝗧𝗛𝗘𝗥](https://t.me/Ditto_999)
     """

handler = HNDLR
Owner = int(OWNER_ID)
DATABASE_URL = DATABASE_URL
LOGS_CHANNEL = LOGS_CHANNEL

if DATABASE_URL:
   from SpamX.database import users_db
   Sudos = []
   All = users_db.get_all_sudos()
   for x in All:
     Sudos.append(x.user_id)
else:
   Sudos = sudoser
