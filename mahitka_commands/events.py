import discord
from bot_init import bot
from .magagment import user_role_management

@bot.listen()
async def on_presence_update(before: discord.Member, after: discord.Member):
    maksId: discord.Member = after.guild.get_member(975483916263776317)
    JustABush: discord.Member = after.guild.get_member(726448693888417803)
    channel: discord.VoiceChannel = before.guild.get_channel(1067523994854625431)

    try:
        if maksId.status != discord.Status.offline and JustABush.status != discord.Status.offline:
            await channel.edit(name="Кайдо🐉 и Биг Мама⛅ в сети")

        elif maksId.status != discord.Status.offline:
            await channel.edit(name="Кайдо🐉 в сети")

        elif JustABush.status != discord.Status.offline:
            await channel.edit(name="Биг Мама⛅ в сети")

        else:
            await channel.edit(name="Кайдо🐉 и Биг Мамы⛅ нет в сети😣")
    except: pass


@bot.listen()
async def on_message(message: discord.Message):
    await user_role_management(message=message)


@bot.listen()
async def on_ready():


    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching,
                                name=f".help"),
        status=discord.Status.idle
    )