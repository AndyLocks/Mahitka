import discord
from discord.ext import commands
from basa.users_basa import Conection
from variables.config import *

bot = commands.Bot(command_prefix = ".", intents = discord.Intents.all(), status=discord.Status.idle)

bot.help_command = None

basa = Conection(
    host=host,
    user=user,
    password=password,
    db_name=db_name,
    port=3306
)