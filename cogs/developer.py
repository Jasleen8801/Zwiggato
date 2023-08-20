import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
GUILD_ID = os.getenv("GUILD_ID")
GUILD_ID = int(GUILD_ID)
ADMIN_USER_ID = os.getenv("ADMIN_USER_ID")
ADMIN_USER_ID = int(ADMIN_USER_ID)

class DeveloperCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @nextcord.slash_command(name="developer", description="Get information about the developer.", guild_ids=[GUILD_ID])
    async def developer(self, interaction: nextcord.Interaction):
        funny_info = (
            "👋 Hey there, fellow human! I'm Jasleen Kaur, your friendly bot creator.\n"
            "🤖 I like long walks on the server and coding sessions by the moonlight.\n"
            "🌙 I don't have any favourite programming language but ping me up if you're interested in Augmented Reality or WebXR related development.\n"
            "🎮 Fun fact: I love hearing Spotify so let me know some new pop songs and occasionally binging on memes.\n"
            "💬 If you'd like to connect or have any questions, feel free to find me on [LinkedIn](https://www.linkedin.com/in/jasleen-kaur-9a27b821a/) or [GitHub](https://github.com/Jasleen8801).\n"
            "🌟 Remember, I'm here to make your server life easier and brighter! Hit me up on Discord by username `_jasleenkaur`"
        )

        embed = nextcord.Embed(
            title="👩‍💻 Developer Information",
            description=funny_info,
            color=0x00ff00,
            timestamp=interaction.created_at,
            url="https://github.com/Jasleen8801"
        )
        
        await interaction.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(DeveloperCog(bot))
