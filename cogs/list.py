import nextcord
from nextcord.ext import commands
import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()
GUILD_ID = os.getenv("GUILD_ID")
GUILD_ID = int(GUILD_ID)

class ListCog(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @nextcord.slash_command(name="list", description="Check the current set values", guild_ids=[GUILD_ID])
    async def List(self, interaction):
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT city, restaurant_name, food_item FROM main WHERE guild_id = '{interaction.guild.id}'")
        result = cursor.fetchone()
        cursor.close()
        db.close()
        if result:
            city_name, restaurant_name, food_item = result
            embed = nextcord.Embed(title="Current List", color=0x3498db)
            embed.add_field(name="City Name", value=city_name, inline=False)
            embed.add_field(name="Restaurant Name", value=restaurant_name, inline=False)
            embed.add_field(name="Food Item", value=food_item, inline=False)
        else:
            embed = nextcord.Embed(title="Current List", description="No data found.", color=0xe74c3c)

        await interaction.send(embed=embed)


def setup(bot):
    bot.add_cog(ListCog(bot))