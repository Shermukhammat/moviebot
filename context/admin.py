from aiogram import types

class Admin:
    menu = {'uz' : '🎛 Menu', 
            'en' : '🎛 Menu',
            'ru' : '🎛 Меню'}
    
    
    def owner_registred(update : types.Message, lang : str) -> str:
        name = f"[{update.from_user.first_name}]({update.from_user.url})"
        if lang == 'uz':
            return f"✅ {name}, siz ega sifatida ro'yxatdan o'tdingiz !"
        elif lang == 'ru':
            return f"✅ {name}, вы зарегистрированы как владелец !"
        return f"✅ {name}, you have successfully registered as an owner!"
    
    def owner_not_registred(update : types.Message, lang : str):
        name = f"[{update.from_user.first_name}]({update.from_user.url})"
        if lang == 'uz':
            return f"❌ {name}, siz ega emasiz !"
        elif lang == 'ru':
            return f"❌ {name}, ты не владелец !"
        return f"❌ {name}, you aren't owner"
    
    def chose_lang(lang : str):
        if lang == 'uz':
            return "Iltimos tilni tanlang"
        elif lang == 'ru':
            return "Пожалуйста, выберите язык"
        return "Pleas select a language"
    
    def settings_menu(lang : str):
        if lang == 'uz':
            return "Sozlamalar Menyusi"
        elif lang == 'ru':
            return "Пожалуйста, выберите язык"
        return "Pleas select a language"
    
    
