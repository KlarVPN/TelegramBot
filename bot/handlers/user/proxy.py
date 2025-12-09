from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from urllib.parse import urlencode

from config.settings import settings

router = Router(name="user_proxy")

# TODO: Сделать переводы для русского и английского языков

def create_socks5_button(server: str, port: int, user: str, password: str):
    """Создаёт кнопку для подключения SOCKS5 в Telegram"""
    params = {
        'server': server,
        'port': port,
        'user': user,
        'pass': password
    }

    socks_url = f"https://t.me/socks?{urlencode(params)}"

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text="🔗 Подключить прокси",
                url=socks_url
            )
        ]
    ])

    return keyboard


@router.message(Command("proxy"))
async def cmd_proxy(message: Message):
    keyboard = create_socks5_button(
        settings.SOCKS5_PROXY_HOST,
        settings.SOCKS5_PROXY_PORT,
        settings.SOCKS5_PROXY_USERNAME,
        settings.SOCKS5_PROXY_PASSWORD
    )

    text = f"<b>🔐 Прокси для Telegram</b>\n\nНажмите кнопку для подключения 👇\n\n<b>💎 KlarVPN</b> откроет доступ к <b>YouTube, Instagram и любым сайтам</b>"

    await message.answer(text, reply_markup=keyboard, parse_mode="HTML")
