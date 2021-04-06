import os

from discord.ext import commands
from discord_slash import SlashCommand

bot = commands.Bot(command_prefix="/")
slash = SlashCommand(bot, sync_commands = False)

bot.load_extension("cogs")

bot.run(os.environ['token'])




