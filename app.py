import logging

from aiogram import Bot, Dispatcher, executor, types
from diffusers import StableDiffusionPipeline
import torch
import os

model_id = "nitrosocke/redshift-diffusion"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
pipe = pipe.to("cuda")

logging.basicConfig(level=logging.INFO)

bot = Bot(token="6051434362:AAHX-95smUeA5RlQMwnSQJSN9gyyKRKFdlo")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Izohni jo'nating.....")


@dp.message_handler()
async def start(message: types.Message):
    image = pipe(message.text).images[0]
    image.save('image.png')
    with open('image.png', 'rb') as photo:
        await message.reply_photo(photo)
        
    os.remove("image.png")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
