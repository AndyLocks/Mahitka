import discord
from bot_init import bot, basa
from discord.ext import commands
from variables.constant import *
from ..magagment import management_role
from discord import app_commands

@bot.hybrid_command(name="reset", description = "user role reset")
@app_commands.describe(user = "user mention")
async def reset(ctx: commands.context.Context, user: discord.User):
    if not ctx.author.guild_permissions.administrator:
        emb = discord.Embed(
            title="Ошибка",
            description="Вы не администратор.",
            color=discord.Color.red()
        )
        await ctx.send(embed=emb, ephemeral=True)
        return
    if await basa.chek(member_id=user.id):
        emb = discord.Embed(
            title="**Внимание!!!**",
            description="Вы уверены?",
            color=discord.Color.yellow()
        )
        view = discord.ui.View()
        button_yes = discord.ui.Button(
            emoji="✅",
            label="Да"
        )
        button_no = discord.ui.Button(
            emoji="❌",
            label="Нет"
        )
        async def result_yes(interaction: discord.Interaction):
            emb = discord.Embed(
                title="Готово",
                description="Пользователь был удален из базы данных.",
                color=discord.Color.green()
            )

            author_roles_id = []
            for i in ctx.author.roles:
                author_roles_id.append(i.id)

            range_roles = set(BOUNTYHUNTERS_ROLES) | set(MARINES_ROLES) | set(PIRATES_ROLES)

            roles = set(author_roles_id) & range_roles

            for i in roles:
                role = ctx.guild.get_role(i)
                await ctx.author.remove_roles(role)

            await basa.reset_user(memberId=user.id)

            await interaction.response.edit_message(embed=emb, view=None)
        
        async def result_no(interaction: discord.Interaction):
            await interaction.response.edit_message(content="Удаление было отменено", view=None, embed=None)
        
        button_yes.callback = result_yes
        button_no.callback = result_no

        view.add_item(button_yes)
        view.add_item(button_no)
        await ctx.send(embed=emb, ephemeral=True, view=view)
    else:
        emb = discord.Embed(
            title="Ошибка",
            description="Пользователь не выбрал свой путь.",
            color=discord.Color.red()
        )
        await ctx.send(embed=emb, ephemeral=True)