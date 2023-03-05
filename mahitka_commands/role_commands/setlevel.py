import discord
from bot_init import bot, basa
from discord.ext import commands
from variables.constant import *
from ..magagment import management_role
from discord import app_commands

@bot.hybrid_command(name="setlevel", description = "set user level")
@app_commands.describe(user="user mention")
async def setlevel(ctx: commands.context.Context, value: int, user: discord.User):
    if not ctx.author.guild_permissions.administrator:
        emb = discord.Embed(
            title="Ошибка",
            description="Вы не администратор.",
            color=discord.Color.red()
        )
        await ctx.send(embed=emb, ephemeral=True)
        return
        
    user = user.id

    if await basa.chek(member_id=user):
        if value < 0:
            emb = discord.Embed(
                title="Ошибка",
                description="Значение слишком маленькое.",
                color=discord.Color.red()
            )

            await ctx.send(embed=emb, ephemeral=True)
            return
        
        await basa.set_point(memberId=user, value=value*100)
        await management_role(ctx=ctx)
        try: await ctx.message.add_reaction("✅")
        except: await ctx.send("✅", ephemeral=True)

    else:
        emb = discord.Embed(
            title="Ошибка",
            description="Пользователь не выбрал свой путь.",
            color=discord.Color.red()
        )
        await ctx.send(embed=emb, ephemeral=True)