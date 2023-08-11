import nextcord
from nextcord.ext import commands
import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()
GUILD_ID = os.getenv("GUILD_ID")
GUILD_ID = int(GUILD_ID)


class CityCog(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @nextcord.slash_command(name="setcity", description="To set the city name", guild_ids=[GUILD_ID])
    async def SetvalCity(self, interaction, city: str):
        # await interaction.response.send_message(f"City set to {city}")
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()
        cursor.execute(f"SELECT city FROM main WHERE guild_id = '{interaction.guild.id}'")
        result = cursor.fetchone()
        if result is None:
            sql = ("INSERT INTO main(guild_id,city) VALUES(?,?)")
            val = (interaction.guild.id, city)
            await interaction.send(f"City has been set to '{city}'")
        elif result is not None:
            sql = ("UPDATE main SET city = ? WHERE guild_id = ?")
            val = (city, interaction.guild.id)
            await interaction.send(f"City has been set to '{city}'")
        cursor.execute(sql,val)
        db.commit()
        cursor.close()
        db.close()

def setup(bot):
    bot.add_cog(CityCog(bot))
