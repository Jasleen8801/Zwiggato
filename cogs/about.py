import nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()
GUILD_ID = os.getenv("GUILD_ID")
GUILD_ID = int(GUILD_ID)

class AboutCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @nextcord.slash_command(name="about", description="Get information about the bot.", guild_ids=[GUILD_ID])
    async def about(self, ctx):
        embed = nextcord.Embed(title="About", description="🍔 Ever wondered if you're paying too much for that burger? Fear not, for I am Foodie-Fi, your food price detective! 🕵️‍♂️ I'll help you uncover the mysteries of food prices from various delivery services. Whether it's the 'spend less, eat more' deals or the 'gourmet bites for a king' offers, I've got you covered. Just command me and let's unveil the secrets of delicious savings! 🍕🥤")

        embed.add_field(name="Developer", value="Jasleen Kaur", inline=False)
        embed.add_field(name="Commands", value="`/help` - To get a list of my commands\n`/result` - To see the food prices", inline=False)
        
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(AboutCog(bot))
