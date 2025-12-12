from typing import Optional

from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command

from bot.middlewares.i18n import JsonI18n
from config.settings import settings

router = Router(name="user_proxy")

@router.message(Command("proxy"))
async def cmd_proxy(message: Message, i18n_data: dict):
    current_lang = i18n_data.get("current_language", settings.DEFAULT_LANGUAGE)
    i18n: Optional[JsonI18n] = i18n_data.get("i18n_instance")
    _ = lambda key, **kwargs: i18n.gettext(current_lang, key, **kwargs
                                           ) if i18n else key

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=_(key="proxy_connect_button"),
                url=settings.MTPROXY_LINK
            )
        ]
    ])

    await message.answer(_(key="proxy_connect_text"), reply_markup=keyboard, parse_mode="HTML")
