import random
import asyncio
from aiogram import Bot, Dispatcher, executor, types

TOKEN = "ВСТАВЬ_СЮДА_ТОКЕН_ОТ_BOTFATHER"
POCKET_LINK = "https://твоя_партнерская_ссылка"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

OTC_PAIRS = [
    "EUR/USD OTC",
    "GBP/USD OTC",
    "USD/JPY OTC",
    "AUD/USD OTC",
    "USD/CAD OTC",
    "EUR/JPY OTC",
    "GBP/JPY OTC",
    "EUR/GBP OTC"
]

DIRECTIONS = ["⬆️ BUY", "⬇️ SELL"]
EXPIRATIONS = ["5s", "15s", "30s", "1m", "2m", "5m"]

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("📊 Получить сигнал")
    await message.answer(
        "👋 Добро пожаловать!\n\n"
        "Бот выдаёт тестовые OTC сигналы.",
        reply_markup=kb
    )

@dp.message_handler(lambda msg: msg.text == "📊 Получить сигнал")
async def signal(message: types.Message):
    await message.answer("🔍 Анализ рынка OTC...")
    await asyncio.sleep(random.randint(1, 3))

    pair = random.choice(OTC_PAIRS)
    direction = random.choice(DIRECTIONS)
    exp = random.choice(EXPIRATIONS)

    text = (
        "📊 СИГНАЛ\n\n"
        f"💱 Пара: {pair}\n"
        f"📈 Направление: {direction}\n"
        f"⏱ Экспирация: {exp}"
    )

    btn = types.InlineKeyboardMarkup()
    btn.add(types.InlineKeyboardButton("🚀 Pocket Option", url=POCKET_LINK))

    await message.answer(text, reply_markup=btn)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
