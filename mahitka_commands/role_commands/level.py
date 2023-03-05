import discord
from bot_init import bot, basa
from discord.ext import commands
from variables.constant import *
from ..magagment import management_role
from discord import app_commands

@bot.hybrid_command(name="level", description = "view user level")
@app_commands.describe(user = "user mention")
async def level(ctx: commands.context.Context, user: discord.User):
    user = user.id

    if await basa.chek(member_id=user):
        user_name = ctx.guild.get_member(user).name
        point = await basa.get_point(memberId=user)
        level = point // 100
        choise = await basa.get_choise(memberId=user)
        if choise == "Marine":
            emoji = "🟦"
        elif choise == "Pirate":
            emoji = "🟥"
        elif choise == "Bounty-Hunter":
            emoji = "🟩"

        emb = discord.Embed(
            title=user_name,
            description=f"Level: **{level}** | Point: **{point}**",
            color=discord.Color.green()
        )
        emb.set_footer(text=f"Choise {choise} {emoji}")

        await ctx.send(embed=emb)
    else:
        emb = discord.Embed(
            title="Ошибка",
            description="Пользователь не выбрал свой путь.",
            color=discord.Color.red()
        )
        await ctx.send(embed=emb, ephemeral=True)