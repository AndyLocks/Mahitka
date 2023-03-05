import discord
from bot_init import bot
from discord.ext import commands
from variables.constant import EMBED_COLOR

@bot.group(name="help")
async def help(ctx: commands.context.Context):
    emb = discord.Embed(
        title="Commad list",
        description="Вы можете получить детальную справку по каждой команде, указав название. Например: /help level\n\n\n\
            **level** - Уровень пользователя\n\n\
            **leaders** - Показать список лидеров \n\n\
            **role** - Выбрать свой путь\n\n\
            **setlevel** - Установить уровень участнику\n\n\
            **setpoint** - Установить очки участнику",
        color=EMBED_COLOR
    )
    await ctx.send(embed=emb, ephemeral=True)

@help.command()
async def level(ctx: commands.context.Context):
    emb = discord.Embed(
        title="Level",
        description="Выводит уровень, опыт и выбор пути участника.",
        color=discord.colour.Color.green()
    )
    emb.add_field(
        name="Аргументы",
        value="**user** - упоминание пользователя.",
        inline=False
    )
    await ctx.send(embed=emb, ephemeral=True)

@help.command()
async def leaders(ctx: commands.context.Context):
    emb = discord.Embed(
        title="Leaders",
        description="Выводит список всех \
            участников с уровнем, опытом и выбором стороны.",
            color=EMBED_COLOR
    )
    await ctx.send(embed=emb, ephemeral=True)

@help.command()
async def role(ctx: commands.context.Context):
    emb = discord.Embed(
        title="role",
        description="**Этой командой можно пользоваться только один раз!!!** Прежде чем выбрать, подумайте.\n\n\
            Выводит три варианта выбора путей. Выберете один.",
            color=EMBED_COLOR
    )
    await ctx.send(embed=emb, ephemeral=True)

@help.command()
async def setlevel(ctx: commands.context.Context):
    emb = discord.Embed(
        title="Setlevel",
        description="**ЭТОЙ КОМАНДОЙ МОГУТ ПОЛЬЗОВАТЬСЯ ТОЛЬКО АДМИНИСТАТОРЫ**\n\nУстанавливает уровень пользователю.",
        color=EMBED_COLOR
    )
    emb.add_field(
        name="Аргументы",
        value="**value** - значение которое нужно установить.\n**user** - упоминание пользователя.",
        inline=False
    )
    await ctx.send(embed=emb, ephemeral=True)

@help.command()
async def setpoint(ctx: commands.context.Context):
    emb = discord.Embed(
        title="Setpoint",
        description="**ЭТОЙ КОМАНДОЙ МОГУТ ПОЛЬЗОВАТЬСЯ ТОЛЬКО АДМИНИСТАТОРЫ**\n\nУстанавливает опыт пользователю.",
        color=EMBED_COLOR
    )
    emb.add_field(
        name="Аргументы",
        value="**value** - значение которое нужно установить.\n**user** - упоминание пользователя.",
        inline=False
    )
    await ctx.send(embed=emb, ephemeral=True)

@help.command()
async def reset(ctx: commands.context.Context):
    emb = discord.Embed(
        title="Reset",
        description="**ЭТОЙ КОМАНДОЙ МОГУТ ПОЛЬЗОВАТЬСЯ ТОЛЬКО АДМИНИСТАТОРЫ**\n\nУдаляет пользователя из базы данных.",
        color=EMBED_COLOR
    )
    emb.add_field(
        name="Аргументы",
        value="**user** - упоминание пользователя.",
        inline=False
    )
    await ctx.send(embed=emb, ephemeral=True)
