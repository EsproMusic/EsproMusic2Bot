from EsproMusic import Esprodb
from EsproMusic.Helpers import remove_active_chat


async def _clear_(chat_id):
    try:
        Esprodb[chat_id] = []
        await remove_active_chat(chat_id)
    except:
        return
