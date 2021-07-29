
import asyncio
import io
import os
import shutil
import sys
import time
import traceback

from bot import LOG_FILE_ZZGEVC
from bot.dinmamoc import Commandi


async def upload_log_file(client, message):
    await message.reply_document(
        LOG_FILE_UP
    )
