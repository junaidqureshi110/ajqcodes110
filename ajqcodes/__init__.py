from telethon import TelegramClient
import logging
import time 

api_id = "20307178"
api_hash = "f047c24a556d09b3a652b27715b86ba3"
bot_token = "6257451134:AAFPfjHalgZyaSmbcK8is4dVU2XaXj9hAGI"


bot = TelegramClient("ajqcodes", api_id,api_hash).start(bot_token=bot_token)