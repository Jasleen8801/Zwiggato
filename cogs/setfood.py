import nextcord
from nextcord.ext import commands
import sqlite3


class FoodCog(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @nextcord.slash_command(name="setfood", description="To set the food item name", guild_ids=[1040237301814546462])
    async def SetvalCity(self, interaction, food: str):
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT food_item FROM main WHERE guild_id = '{interaction.guild.id}'")
        result = cursor.fetchone()
        if result is None:
            sql = ("INSERT INTO main(guild_id,food_item) VALUES(?,?)")
            val = (interaction.guild.id, food)
            await interaction.send(f"Food Item has been set to '{food}'")
        elif result is not None:
            sql = ("UPDATE main SET food_item = ? WHERE guild_id = ?")
            val = (food, interaction.guild.id)
            await interaction.send(f"Food Item has been set to '{food}'.")
        cursor.execute(sql,val)
        db.commit()
        cursor.close()
        db.close()

def setup(bot):
    bot.add_cog(FoodCog(bot))
