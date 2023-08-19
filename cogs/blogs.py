import nextcord
from nextcord.ext import commands
import random

class FoodBlogsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.food_blogs = [
            "https://www.foodblog1.com/rss",  # Replace with actual RSS feed URLs
            "https://www.foodblog2.com/rss",
            "https://www.foodblog3.com/rss"
        ]

    @commands.command(name="random_recipe", description="Fetch and display a random recipe from popular food blogs")
    async def random_recipe(self, ctx):
        random_blog_url = random.choice(self.food_blogs)
        # Implement code to fetch and parse the RSS feed
        # You can use libraries like feedparser to parse RSS feeds
        
        # For demonstration purposes, let's create a fake recipe data
        fake_recipe = {
            "title": "Delicious Pasta Recipe",
            "description": "Learn how to make a mouthwatering pasta dish.",
            "link": "https://www.foodblog1.com/recipes/delicious-pasta"
        }

        embed = nextcord.Embed(title=f"Random Recipe from Food Blogs", color=0x14aaeb)
        embed.add_field(name=f"**{fake_recipe['title']}**", value=fake_recipe['description'], inline=False)
        embed.add_field(name="Read More", value=f"[Click here]({fake_recipe['link']})", inline=False)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(FoodBlogsCog(bot))
