from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hello {}

Welcome {}

If you don't believe this bot,
1) It's hard to read this message
2) Block bot or delete chat

This bot works to help you get a string session via bot.Recommendations if you want to take strings Use another account, so you don't delay.Thank you
By @YDDDE .
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("- Start Generating Session .", callback_data="generate")],
        [InlineKeyboardButton(text="- Main Menu .", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("- Start Generating Session .", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("- Start Generating Session .", callback_data="generate")],
        [InlineKeyboardButton("- Deveoper .", url="https://t.me/fckualot")],
        [
            InlineKeyboardButton(" - Help .", callback_data="help"),
            InlineKeyboardButton("- About .", callback_data="about")
        ],
        [InlineKeyboardButton("- More information .", url="https://t.me/zvvvn")],
    ]

    # Help Message
    HELP = """
- **Available Commands** .

/ About - about this bot
/ Help - this message
/ Start - start bot
/ Generate - Start Generating Session
/ Cancel - Cancel Process
/ Restart - Cancel Process
"""

    # About Message
    ABOUT = """
- **About This Bot** .

A telegram bot to take pyrogram and telethon string session by @stringriobot

Group Support: [Join](t.me/xfffw)

Framework: Pyrogram

Language: Python.

Developer: @YDDDE .
    """
