import nextcord
from nextcord.ext import commands
import sqlite3


class RestCog(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @nextcord.slash_command(name="setrest", description="To set the restaurant name", guild_ids=[1040237301814546462])
    async def SetvalCity(self, interaction, rest: str):
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT restaurant_name FROM main WHERE guild_id = '{interaction.guild.id}'")
        result = cursor.fetchone()
        if result is None:
            sql = ("INSERT INTO main(guild_id,restaurant_name) VALUES(?,?)")
            val = (interaction.guild.id, rest)
            await interaction.send(f"Restaurant name has been set to '{rest}'")
        elif result is not None:
            sql = ("UPDATE main SET restaurant_name = ? WHERE guild_id = ?")
            val = (rest, interaction.guild.id)
            await interaction.send(f"Restaurant name has been set to '{rest}'")
        cursor.execute(sql,val)
        db.commit()
        cursor.close()
        db.close()

def setup(bot):
    bot.add_cog(RestCog(bot))
