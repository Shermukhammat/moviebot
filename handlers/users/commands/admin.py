from loader import dp, db, types, AdminType, Context, user_context, bot, set_admin_commands

# user_context.put_and_update("✅ {name}, siz ega sifatida ro'yxatdan o'tdingiz !", src='uz', key = 'owner_registred')
# user_context.put_and_update("❌ Afsus {name}, qandaydir xato yuz berdi", src='uz', key = 'somthing_went_wrong')
# user_context.put_and_update("❌ Sizda adminlik huquqi yo'q !", src = 'uz', key = 'you_not_owner')



@dp.message_handler(lambda update : db.is_user(update.from_user.id), commands = 'admin')
async def admin_command(update : types.Message):
    user = db.get_user(update.from_user.id)
    name = f"[{update.from_user.first_name}]({update.from_user.url})"

    if db.OWNER_ID == update.from_user.id:
        if db.register_admin(update.from_user.id, 
                                 update.from_user.first_name, 
                                 lang = user['lang'], 
                                 admin_type = AdminType.owner):
            db.remove_user(update.from_user.id)
            await set_admin_commands(update.from_user.id, bot, lang = user['lang'])
            await update.answer(user_context.get('owner_registred', 
                                                 target = user['lang'], 
                                                 name = name), 
                                parse_mode = types.ParseMode.MARKDOWN)
        else:
            await update.answer(user_context.get('somthing_went_wrong', 
                                                 target = user['lang'], 
                                                 name = name), 
                                parse_mode = types.ParseMode.MARKDOWN)
    
    else:
        await update.answer(user_context.get('you_not_owner', target = user['lang']))
