from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Получить совет карты")]
],                          resize_keyboard=True,
                            input_field_placeholder="Совет дня")