import json
from aiogram.types import FSInputFile

from aiogram import F, Router
from aiogram.filters import CommandStart, Command, Filter
from aiogram.types import Message
import app.keyboards as kb
import random
from aiogram.enums import ParseMode

router = Router()

def load_cards():
    with open('cards.json', encoding='utf-8') as f:
        cards = json.load(f)
        return cards

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Привет!", reply_markup=kb.main)

@router.message(F.text == 'Получить совет карты')
async def sovet(message: Message):
    cards = load_cards()
    card = random.choice(cards)
    name = card['name']
    image_path = card['image']
    description = card['description']
    image = FSInputFile(image_path)
    otvet = f'<b>{name}</b>\n\n{description}'

    await message.answer_photo(photo=image, caption=otvet, parse_mode=ParseMode.HTML)



