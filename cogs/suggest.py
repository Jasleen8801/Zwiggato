import nextcord
from nextcord.ext import commands
import random
from dotenv import load_dotenv
import os

load_dotenv()
GUILD_ID = os.getenv("GUILD_ID")
GUILD_ID = int(GUILD_ID)

class RandomFoodCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="suggest", description="Get a random food suggestion.", guild_ids=[GUILD_ID])
    async def suggest_food(self, ctx):
        foods = ["Nachos", "Bruschetta", "Chicken wings", "Spring rolls", "Egg rolls", "Fried calamari", "Shrimp cocktail", "Mozzarella sticks", "Quesadillas", "Hummus and pita bread", "Soup", "Pizza", "Burger", "Pasta", "Sushi", "Tacos", "Fried rice", "Grilled chicken", "Salmon", "Steak", "Roasted vegetables", "Salad", "Ice cream", "Cake", "Pie", "Cookies", "Brownies", "Donuts", "Waffles", "Pancakes", "Fruit salad", "Chocolate mousse", "Pudding", "Coffee", "Tea", "Soda", "Juice", "Milkshake", "Smoothie", "Beer", "Wine", "Cocktail", "Water"]
        random_food = random.choice(foods)
        await ctx.send(f"How about trying {random_food}?")

def setup(bot):
    bot.add_cog(RandomFoodCog(bot))
