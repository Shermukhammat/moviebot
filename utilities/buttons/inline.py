from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup




class InlineButtons:
    search_movie = InlineKeyboardMarkup(inline_keyboard = [[
        InlineKeyboardButton(text = '🔍 Kino izlash', switch_inline_query_current_chat = "")]
        ])