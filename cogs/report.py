import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
GUILD_ID = os.getenv("GUILD_ID")
GUILD_ID = int(GUILD_ID)
ADMIN_USER_ID = os.getenv("ADMIN_USER_ID")
ADMIN_USER_ID = int(ADMIN_USER_ID)

class ReportCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @nextcord.slash_command(name="report", description="Report a bug or suggest a feature.", guild_ids=[GUILD_ID])
    async def report(self, interaction: nextcord.Interaction, message: str):
        admin_user = await self.bot.fetch_user(ADMIN_USER_ID)
        admin_dm = await admin_user.create_dm()
        user_mention = interaction.user.mention
        guild_name = interaction.guild.name
        guild_id = interaction.guild.id
        await admin_dm.send(f"Reported by {user_mention} in {guild_name} ({guild_id}): {message}")

        embed = nextcord.Embed(title="Report", description="Thank you for your feedback! I'll get back to you as soon as possible.")
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(ReportCog(bot))
