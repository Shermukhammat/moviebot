from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



class DefoltButtons:
    cancle_button = ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = "❌ Bekor qilish")]], resize_keyboard = True)

    def adminMenu(lang : str = 'uz'):
        if lang == 'uz':
            return ReplyKeyboardMarkup(keyboard = [
                                       [KeyboardButton(text = "🎬 Kino qo'shish ➕"), KeyboardButton(text = "📺 Seriyal qo'shish ➕")],
                                       [KeyboardButton(text = "🎬 Kino tahrirlash ✏️"), KeyboardButton(text = "📺 Seriyal tahrirlash ✏️")],
                                       [KeyboardButton(text = "🔔 Reklama jo'natish")],
                                       [KeyboardButton(text = "⚙️ Sozlamalar")]
                                       ],
                                   resize_keyboard = True)
        
        elif lang == 'ru':
            return ReplyKeyboardMarkup(keyboard = [
                                       [KeyboardButton(text = "🎬 Добавить фильм ➕"), KeyboardButton(text = "📺 Добавить серию ➕")],
                                       [KeyboardButton(text = "🎬 Монтаж фильмов ✏️"), KeyboardButton(text = "📺 Монтаж сериала ✏️")],
                                       [KeyboardButton(text = "🔔 Отправить рекламу")],
                                       [KeyboardButton(text = "⚙️ Настройки")]
                                       ],
                                   resize_keyboard = True)

        return ReplyKeyboardMarkup(keyboard = [
                                       [KeyboardButton(text = "🎬 Add movie ➕"), KeyboardButton(text = "📺 Add series ➕")],
                                       [KeyboardButton(text = "🎬 Movie Editing ✏️"), KeyboardButton(text = "📺 Series editing ✏️")],
                                       [KeyboardButton(text = "🔔 Send advertisement")],
                                       [KeyboardButton(text = "⚙️ Settings")]
                                       ],
                                   resize_keyboard = True)
    
    def back_button(cancle_button : bool = False):
        if cancle_button:
            return ReplyKeyboardMarkup(keyboard = [
                                       [KeyboardButton(text = "⬅️ Orqaga qaytish"), KeyboardButton(text = "❌ Bekor qilish")]],
                                       resize_keyboard = True)
        return ReplyKeyboardMarkup(keyboard = [
                                       [KeyboardButton(text = "⬅️ Orqaga qaytish")]],
                                       resize_keyboard = True)
    
    