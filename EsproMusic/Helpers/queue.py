from EsproMusic import Esprodb


async def put(
    chat_id,
    title,
    duration,
    videoid,
    file_path,
    ruser,
    user_id,
):
    put_f = {
        "title": title,
        "duration": duration,
        "file_path": file_path,
        "videoid": videoid,
        "req": ruser,
        "user_id": user_id,
    }
    get = Esprodb.get(chat_id)
    if get:
        Esprodb[chat_id].append(put_f)
    else:
        Esprodb[chat_id] = []
        Esprodb[chat_id].append(put_f)
