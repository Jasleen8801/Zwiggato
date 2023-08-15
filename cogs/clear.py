import nextcord
from nextcord.ext import commands
import sqlite3
from dotenv import load_dotenv
import os

load_dotenv()
GUILD_ID = os.getenv("GUILD_ID")
GUILD_ID = int(GUILD_ID)

class ClearCog(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @nextcord.slash_command(name="clear", description="Clear the current values in the database", guild_ids=[GUILD_ID])
    async def Clear(self, interaction):
        db = sqlite3.connect('main.sqlite')
        cursor = db.cursor()

        cursor.execute(f"DELETE FROM main WHERE guild_id = '{interaction.guild.id}'")
        db.commit()

        cursor.close()
        db.close()

        await interaction.send("Database cleared for the current guild.")

def setup(bot):
    bot.add_cog(ClearCog(bot))
