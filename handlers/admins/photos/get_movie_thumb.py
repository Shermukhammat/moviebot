from loader import dp, bot, db, AdminStates, BOT_NAME, types, InlineButtons, DefoltButtons, Movie, picsum
from aiogram.dispatcher import FSMContext
import os


n = 0


@dp.message_handler(content_types = types.ContentType.PHOTO, state = AdminStates.get_movie_thumb)
async def get_movie_thumb2(update : types.Message, state : FSMContext):
    photo = update.photo[-1]
    info = await bot.get_file(photo.file_id)
    ext = get_file_extension(info)
    
    if ext != 'jpg' and ext != 'png':
        await update.answer("❌ Rasim formati jpg yoki png formatda bo'lishi shart")
        return

    if info.file_size >= 5 * 1024 * 1024:
        await update.answer("❌ Rasim hajmi 5 Mb dan ko'p")
        return
    
    path = await download_photo(info)
    if not os.path.exists(path):
        return
    
    url = await picsum.get_photo_poster_url(path)
    os.remove(path)

    if not url:
        return





    await state.set_state(AdminStates.edit_movie_menu)
    
    async with state.proxy() as data:
        data['thumb'] = url
        
        if update.caption:
            message_data = await bot.copy_message(chat_id = db.DATA_CHANEL_ID, 
                                                  from_chat_id = update.from_user.id, 
                                                  message_id = update.message_id)
        else:
            message_data = await bot.copy_message(chat_id = db.DATA_CHANEL_ID, 
                                                  from_chat_id = update.from_user.id, 
                                                  message_id = update.message_id,
                                                  caption = 'Kino\'nomi: ' + data['title'])
        
        data['id'] = message_data.message_id


        await bot.copy_message(chat_id = update.from_user.id,
                               from_chat_id = db.DATA_CHANEL_ID,
                               message_id = data['id'],
                               caption = f"Kino nomi: {data['title']} ",
                               reply_markup = InlineButtons.movie_add_menu())
            




@dp.channel_post_handler()
async def chanel_handler(update : types.Message):
    print(update.sender_chat.title)
    print(update.sender_chat.id)


    


def get_file_extension(info : types.File) -> str:
    return info.file_path.split('.')[-1]

async def download_photo(info : types.File, path : str = 'data/photos') -> str:
    download_file = await bot.download_file(info.file_path)

    global n 
    n+=1
    with open(f'{path}/photo{n}.jpg', 'wb') as file:
        file.write(download_file.getvalue())

    return f'{path}/photo{n}.jpg'


