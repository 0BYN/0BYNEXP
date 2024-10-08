from .config import get_config_categories, get_config_data
from .tasks import setup_tasks
from .test import ExampleCog

class Plugin:
    def __init__(self, bot):
        self.bot = bot

    async def enable_plugin(self):
        """Enable the plugin."""
        self.bot.add_cog(ExampleCog(self.bot))
        if self.bot.scheduler:
            setup_tasks(self.bot.scheduler)
        print(f"Plugin '{__name__}' enabled successfully.")