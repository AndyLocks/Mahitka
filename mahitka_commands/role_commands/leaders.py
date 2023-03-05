import discord
from bot_init import bot, basa
from discord.ext import commands
from variables.constant import *
from ..magagment import management_role
from discord import app_commands
from variables.constant import EMBED_COLOR

@bot.hybrid_command(name="leaders", description = "returns the list of leaders")
async def leaders(ctx: commands.context.Context):
    offset = 0
    async def get_embed(offset: int) -> discord.Embed:
        data = await basa.get_top_list(offset=offset)
        emb = discord.Embed(
            title="Leaders",
            color=EMBED_COLOR
        )
        if not data: emb.set_footer(text="end of list")
        for i in data:
            if i["choise"] == "Marine":
                emoji = "🟦"
            elif i["choise"] == "Pirate":
                emoji = "🟥"
            elif i["choise"] == "Bounty-Hunter":
                emoji = "🟩"
            emb.add_field(
                name=ctx.guild.get_member(int(i["user_id"])).name,
                value=f"Level: **{i['point'] // 100}** | Point: **{i['point']}**\nChoise: **{i['choise']}** {emoji}",
                inline=False
            )
        
        try: emb.set_thumbnail(url=ctx.guild.icon.url)
        except: pass

        return emb
    
    left_button = discord.ui.Button(
        emoji="⬅️"
    )
    right_button = discord.ui.Button(
        emoji="➡️"
    )

    view = discord.ui.View()
    view.add_item(left_button)
    view.add_item(right_button)


    async def left_arrow(interaction: discord.Interaction):
        nonlocal offset
        if offset != 0:
            offset -= 5

            await interaction.response.edit_message(embed=await get_embed(offset=offset), view=view)
        else:
            await interaction.response.edit_message(embed=await get_embed(offset=0), view=view)

    async def right_arrow(interaction: discord.Interaction):
        nonlocal offset
        offset += 5

        await interaction.response.edit_message(embed=await get_embed(offset=offset), view=view)

    left_button.callback = left_arrow
    right_button.callback = right_arrow

    await ctx.send(embed=await get_embed(offset=offset), view=view)