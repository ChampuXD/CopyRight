import asyncio
import importlib
from pyrogram import idle
from CopyRight import CopyRight
from CopyRight.modules import ALL_MODULES

LOGGER_ID = -1001919135283

loop = asyncio.get_event_loop()

async def champu_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("CopyRight.modules." + all_module)
    print("ʙᴏᴛ sᴛᴀʀᴛɪɴɢ")
    await idle()
    print("ʏᴏᴜ ʜᴀᴠᴇ sᴏᴍᴇ ᴛᴇᴄʜɴɪᴄᴀʟ ᴇʀʀᴏʀ ")
    await CopyRight.send_message(LOGGER_ID, "**ɪ ᴀᴍ ᴀʟɪᴠᴇ ʙᴏᴛ sᴜᴄᴄᴇssғᴜʟʟʏ ᴅᴇᴘʟᴏʏ \n [ ᴄʜᴧᴍᴘᴜ ](https://t.me/TheChampu)**")

if __name__ == "__main__":
    loop.run_until_complete(champu_boot())
    
