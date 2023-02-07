import openai
from aiogram import Bot, Dispatcher, executor, types

openai.api_key = "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"

bot = Bot("5022934428:AAFd-Bq4Q3pDFPSCIC_cSxHswjy2WgdvWUQ")
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    await msg.answer(f"Приветики, {msg.from_user.username}\n" +
                    "Введите любой вопрос, чтобы я мог ответить на него")

@dp.message_handler()
async def send_answer(msg: types.Message):
    cmd = " ".join(msg["text"].split())
    print(cmd)
    comp = openai.Completion.create(engine="text-davinci-003", 
                            prompt=str(cmd), max_tokens=1000)
    print(comp.choices[0]['text'])
    await msg.answer(comp.choices[0]['text'])

if __name__=="__main__":
    executor.start_polling(dp)