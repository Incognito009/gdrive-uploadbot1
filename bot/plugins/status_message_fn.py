
import asyncio
import io
import os
import shutil
import sys
import time
import traceback

from bot.config import Messages
from bot.dinmamoc import Commandi

@Client.on_message(filters.private & filters.incoming & filters.command(['log']), group=2)
async def upload_log_file(client, message):
    await message.reply_document(
        LOG_FILE_ZZGEVC
    )
