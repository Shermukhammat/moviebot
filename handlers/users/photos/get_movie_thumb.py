from loader import dp, bot, db, UserStates, AdminStates, BOT_NAME, types, InlineButtons, DefoltButtons, Movie, picsum
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

    async with state.proxy() as data:
        data['thumb'] = url

        if update.caption:
            data['caption'] = update.caption
            return
    
    await state.set_state(AdminStates.get_movie_caption)
    await update.answer("Kino haqida malumot(caption) kiriting")

    # print(await state.get_data())


    


def get_file_extension(info : types.File) -> str:
    return info.file_path.split('.')[-1]

async def download_photo(info : types.File, path : str = 'data/photos') -> str:
    download_file = await bot.download_file(info.file_path)

    global n 
    n+=1
    with open(f'{path}/photo{n}.jpg', 'wb') as file:
        file.write(download_file.getvalue())

    return f'{path}/photo{n}.jpg'


