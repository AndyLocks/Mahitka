import discord
from bot_init import bot, basa
from discord.ext import commands
from variables.constant import *
from ..magagment import management_role
from discord import app_commands
from variables.constant import EMBED_COLOR

@bot.hybrid_command(name="role", description = "choose your rank path")
async def role(ctx: commands.context.Context):
    if ctx.guild.id == SERVERID:
        select = discord.ui.Select(min_values=1, max_values=1, options=[
            discord.SelectOption(label = "Bounty-Hunter"),

            discord.SelectOption(label="Pirate"),

            discord.SelectOption(label="Marine")
        ],
        placeholder="Выберете роль")

        view = discord.ui.View()
        view.add_item(select)

        async def result(interaction: discord.Interaction):
            if interaction.user.id != ctx.author.id:
                emb = discord.Embed(
                    title="Ошибка",
                    description="Вы не можете взаимодействовать с этим сообщением",
                    color=discord.Color.red()
                )

                await interaction.response.send_message(embed=emb, ephemeral=True)
                return
            if not await basa.chek(ctx.author.id):
                if select.values[0] == "Bounty-Hunter":
                    await interaction.user.add_roles(ctx.guild.get_role(BOUNTYHUNTER))
                    await basa.set_new_member(memberId=interaction.user.id, choise="Bounty-Hunter")

                elif select.values[0] == "Pirate":
                    await interaction.user.add_roles(ctx.guild.get_role(PIRATE))
                    await basa.set_new_member(memberId=interaction.user.id, choise="Pirate")


                elif select.values[0] == "Marine":
                    await interaction.user.add_roles(ctx.guild.get_role(MARINE))
                    await basa.set_new_member(memberId=interaction.user.id, choise="Marine")

                emb = discord.Embed(title="Ура!",
                                        description=f"Вы выбрали: {select.values[0]}",
                                        color=discord.Color.green())

                await interaction.response.send_message(embed=emb, ephemeral=True)

            else:
                emb = discord.Embed(title="Ошибка",
                                    description=f"А ты типа уже выбрал свой путь. Все уже. <:KitikHeHe:1034077713453027409>\nВопросы есть? тогда тебе сюда: <#{TICKET_CHANNEL}>",
                                    color=EMBED_COLOR)
                await interaction.response.send_message(embed=emb, ephemeral=True)

        select.callback = result

        await ctx.send(view=view, ephemeral=True)