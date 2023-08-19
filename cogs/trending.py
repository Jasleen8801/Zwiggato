import nextcord
from nextcord.ext import commands
import random

class TrendingItemsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="trending", description="Display trending food items from various restaurants.")
    async def trending_items(self, ctx):
        # List of trending food items
        trending_items = [
            "Burger with special sauce",
            "Pizza with extra cheese",
            "Spicy chicken wings",
            "Sushi rolls with fresh fish",
            "Ice cream sundae with toppings",
            "Tacos with savory fillings",
            "Pasta with creamy Alfredo sauce",
            "Crispy fried chicken",
            "Healthy salad with assorted greens",
            "Delicious chocolate cake"
        ]
        
        # Randomly select trending items
        selected_items = random.sample(trending_items, k=5)
        
        # Create an embed to display the trending items
        embed = nextcord.Embed(title="Trending Food Items", color=nextcord.Color.gold())
        for index, item in enumerate(selected_items, start=1):
            embed.add_field(name=f"#{index}", value=item, inline=False)
        
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(TrendingItemsCog(bot))
