from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



class DefoltButtons:
    cancle_button = ReplyKeyboardMarkup(keyboard = [[KeyboardButton(text = "❌ Bekor qilish")]], resize_keyboard = True)

    def adminMenu():
        return ReplyKeyboardMarkup(keyboard = [
                                       [KeyboardButton(text = "➕ Kino qo'shish")]],
                                   resize_keyboard = True)
    
    def back_button(cancle_button : bool = False):
        if cancle_button:
            return ReplyKeyboardMarkup(keyboard = [
                                       [KeyboardButton(text = "⬅️ Orqaga qaytish"), KeyboardButton(text = "❌ Bekor qilish")]],
                                       resize_keyboard = True)
        return ReplyKeyboardMarkup(keyboard = [
                                       [KeyboardButton(text = "⬅️ Orqaga qaytish")]],
                                       resize_keyboard = True)
    
    