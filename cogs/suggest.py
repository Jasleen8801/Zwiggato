import nextcord
from nextcord.ext import commands
import random

class RandomFoodCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="suggestfood", description="Get a random food suggestion.")
    async def suggest_food(self, ctx):
        foods = ["Pizza", "Burger", "Sushi", "Taco", "Pasta", "Salad", "Ramen", "Ice Cream", "Sushi", "Sandwich"]
        random_food = random.choice(foods)
        await ctx.send(f"How about trying {random_food}?")

def setup(bot):
    bot.add_cog(RandomFoodCog(bot))
