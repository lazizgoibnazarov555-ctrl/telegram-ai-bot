from aiogram import Bot, Dispatcher, executor, types
import random
import asyncio

TOKEN = "ВСТАВЬ_СЮДА_ТОКЕН_ОТ_BOTFATHER"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "🤖 AI Trade Bot\n\n"
        "🔒 Signals locked\n\n"
        "To activate AI:\n"
        "1️⃣ Register via link\n"
        "2️⃣ Deposit from $30\n"
        "3️⃣ Click 'I deposited'"
    )

@dp.message_handler(commands=['signal'])
async def signal(message: types.Message):
    await message.answer("🤖 AI analyzing market...")
    await asyncio.sleep(random.randint(1, 3))

    direction = random.choice(["BUY ⬆️", "SELL ⬇️"])

    await message.answer(
        f"📊 SIGNAL FOUND\n\n"
        f"Asset: EUR/USD\n"
        f"Direction: {direction}\n"
        f"Expiration: 1m\n\n"
        f"⚠️ Wait for arrow"
    )

if __name__ == "__main__":
    executor.start_polling(dp)
  TOKEN = 8204103493:AAG1iz5wa-dhyiXwVNgI8evrMJ7KpCZTHL4
