import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    startmsg = (
        'ʙᴏᴛ sᴜᴅᴀʜ ᴀᴋᴛɪғ ᴅᴀɴ ʙᴇʀᴊᴀʟᴀɴ. ʙᴏᴛ ɪɴɪ '
        'ᴅᴀᴘᴀᴛ ᴍᴇɴʏɪᴍᴘᴀɴ ᴘᴇsᴀɴ ᴅᴀʟᴀᴍ ᴏʙʀᴏʟᴀɴ ᴋʜᴜsᴜs, '
        'ᴅᴀɴ ᴘᴇɴɢɢᴜɴᴀ ᴍᴇɴɢᴀᴋsᴇsɴʏᴀ ᴍᴇʟᴀʟᴜɪ ʙᴏᴛ.'
    )
    forcemsg = (
        'ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ᴘᴇsᴀɴ ʏᴀɴɢ ᴅɪɴᴀɢɪᴋᴀɴ ᴏʟᴇʜ ʙᴏᴛ. '
        'ɢᴀʙᴜɴɢ ᴅᴜʟᴜ, ʟᴀʟᴜ ᴛᴇᴋᴀɴ ᴛᴏᴍʙᴏʟ ᴄᴏʙᴀ ʟᴀɢɪ.'
    )

    API_ID = int(os.environ.get('API_ID', 2040))
    API_HASH = (
        os.environ.get(
            'API_HASH',
            'b18441a1ff607e10a989891a5462e627',
        ),
    )
    OWNER_ID = int(os.environ.get('OWNER_ID', 1700312902))
    MONGO_URL = (
        os.environ.get(
            'MONGO_URL',
            'mongodb://root:passwd@mongo',
        ),
    )

    BOT_TOKEN = os.environ.get('BOT_TOKEN', '')
    DATABASE_ID = int(os.environ.get('DATABASE_ID', ''))

    BOT_ID = BOT_TOKEN.split(':', 1)[0]


Config = Config()
