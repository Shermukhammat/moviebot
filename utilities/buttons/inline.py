from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup




class InlineButtons:
    resolutions = [240, 360, 480, 720, 1080, 1024, 1440, 2160]
    search_movie = InlineKeyboardMarkup(inline_keyboard = [[
        InlineKeyboardButton(text = '🔍 Kino izlash', switch_inline_query_current_chat = "")]
        ])
    
    def get_resolutions(avaible_resolutions : list = []):
        buttons = Buttons()
        for resolution in [240, 360, 480, 720, 1080, 1024, 1440, 2160]:
            if resolution in avaible_resolutions:
                buttons.add_button(InlineKeyboardButton(text = f"✅📹 {resolution}p", callback_data = f'a&{resolution}'))

            else:
                buttons.add_button(InlineKeyboardButton(text = f"📹 {resolution}p", callback_data = str(resolution)))
        buttons.add_button(InlineKeyboardButton(text = "⬅️ Orqaga", callback_data = "back"), new_line = True)
        return InlineKeyboardMarkup(inline_keyboard = buttons.get_buttons())
    

    def movie_add_menu():
        return InlineKeyboardMarkup(inline_keyboard = [
            [InlineKeyboardButton(text = "🚀 Kino yuklash", callback_data = 'upload_movie'), InlineKeyboardButton(text = "➕ Yil", callback_data = "change_title")],
            [InlineKeyboardButton(text = "➕ Yil", callback_data = "add_year"), InlineKeyboardButton(text = "➕ Janir", callback_data = "add_geners")],
            [InlineKeyboardButton(text = "🏳️ Davlat", callback_data = "country"), InlineKeyboardButton(text = "🌐 Til", callback_data = "chose_lang")],
            [InlineKeyboardButton(text = "⬇️ Saqlash", callback_data = "save_movie")]
        ])
    
    def lang_buttons(lang : str) -> InlineKeyboardMarkup:
        if lang == 'uz':
            return InlineKeyboardMarkup(inline_keyboard = [
                [InlineKeyboardButton(text = "🇷🇺 Ruscha", callback_data = "ru"),
                 InlineKeyboardButton(text = "🇬🇧 Inglizcha", callback_data = "en")]
            ])
        elif lang == 'ru':
            return InlineKeyboardMarkup(inline_keyboard = [
                [InlineKeyboardButton(text = "🇺🇿 Узбекский", callback_data = "uz"),
                 InlineKeyboardButton(text = "🇬🇧 Английский", callback_data = "en")]
            ])
        
        return InlineKeyboardMarkup(inline_keyboard = [
                [InlineKeyboardButton(text = "🇺🇿 Uzbek", callback_data = "uz"),
                 InlineKeyboardButton(text = "🇷🇺 Russian", callback_data = "ru")]
            ])
    




class Buttons:
    def __init__(self):
        self.buttons = [[]]
        self.index = 0
        self.curent_item_count = 0
    
    
    def add_button(self, button : InlineKeyboardButton, new_line : bool = False):
        if new_line:
            self.index += 1
            self.curent_item_count = 1
                
            self.buttons.append([])
            self.buttons[self.index].append(button)
            
        else:
            if self.curent_item_count < 3:
                self.curent_item_count += 1
                self.buttons[self.index].append(button)
            else:
                self.index += 1
                self.curent_item_count = 1
                
                self.buttons.append([])
                self.buttons[self.index].append(button)
    
    def get_buttons(self):
        return self.buttons
    
    
    def reset(self):
        self.buttons = [[]]
        self.index = 0
        self.curent_item_count = 0