from bot.get_cfg import get_config


class Commandi:
    UPLOAD_LOG_FILE = get_config(
        "COMMANDI_UPLOAD_LOG_FILE",
        "log"
    )
