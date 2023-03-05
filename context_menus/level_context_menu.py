import discord
from discord.ext import commands
from discord import app_commands
from bot_init import bot
from bot_init import basa

async def levelContextMenu(interaction: discord.Interaction, user: discord.User):


    user = user.id

    if await basa.chek(member_id=user):
        user_name = interaction.guild.get_member(user).name
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

        await interaction.response.send_message(embed=emb)
    else:
        emb = discord.Embed(
            title="Ошибка",
            description="Пользователь не выбрал свой путь.",
            color=discord.Color.red()
        )
        await interaction.response.send_message(embed=emb, ephemeral=True)


level_context_menu = app_commands.ContextMenu(
    name="level",
    callback=levelContextMenu,
    type=discord.AppCommandType.user
)

bot.tree.add_command(level_context_menu)