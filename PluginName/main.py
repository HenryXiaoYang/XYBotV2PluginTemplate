from loguru import logger

from WechatAPI import WechatAPIClient
from utils.decorators import *
from utils.plugin_base import PluginBase


class PluginName(PluginBase):
    description = "插件名"
    author = ""
    version = "1.0.0"

    # 同步初始化
    def __init__(self):
        super().__init__()

    # 异步初始化
    async def async_init(self):
        return

    @on_text_message(priority=99)
    async def handle_text(self, bot: WechatAPIClient, message: dict):
        pass

    @on_at_message(priority=50)
    async def handle_at(self, bot: WechatAPIClient, message: dict):
        pass

    @on_voice_message()
    async def handle_voice(self, bot: WechatAPIClient, message: dict):
        pass

    @on_image_message
    async def handle_image(self, bot: WechatAPIClient, message: dict):
        pass

    @on_video_message
    async def handle_video(self, bot: WechatAPIClient, message: dict):
        pass

    @on_file_message
    async def handle_file(self, bot: WechatAPIClient, message: dict):
        pass

    @on_quote_message
    async def handle_quote(self, bot: WechatAPIClient, message: dict):
        pass

    @on_pat_message
    async def handle_pat(self, bot: WechatAPIClient, message: dict):
        pass

    @on_emoji_message
    async def handle_emoji(self, bot: WechatAPIClient, message: dict):
        pass

    @schedule('interval', seconds=5)
    async def periodic_task(self, bot: WechatAPIClient):
        pass

    @schedule('cron', hour=8, minute=30, second=30)
    async def daily_task(self, bot: WechatAPIClient):
        pass

    @schedule('date', run_date='2026-01-01 00:00:00')
    async def new_year_task(self, bot: WechatAPIClient):
        pass
