import nextcord
from nextcord.ext import commands
import json
from nextcord import ButtonStyle
from nextcord.ui import Button, View
from dotenv import load_dotenv
import os

load_dotenv()
GUILD_ID = os.getenv("GUILD_ID")


class ResultCog(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @nextcord.slash_command(name="result", description="To view the result card from food delivery website", guild_ids=[GUILD_ID])
    async def Result(self, interaction, website: str):
        if website.lower() == "zomato":
            fp = open('Zomato.json')
            data = json.load(fp)
            embed = nextcord.Embed(title="Zomato Price Chart", color=0x14aaeb,
                                description="The food item you want to purchase are:")
            embed.add_field(name='Restaurant_name',
                            value=data['name'], inline=True)
            embed.add_field(name='Speciality',
                            value=data['speciality'], inline=True)
            offerlist = '\n'.join(data['offers'])
            embed.add_field(name='Offers', value=offerlist, inline=False)
            itemlist = '\n'.join(data['Food-items'])
            embed.add_field(name='Item - Price', value=itemlist, inline=False)
            embed.set_image(
                url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQXS4hEp66KMEs_teHQrFuezES2xUL5S4vcOBaLK2cLLEO8MiTVPCi-GHEz7WC4CFnTsbs&usqp=CAU')
            fp.close()

            order = Button(label="Order Now", style=ButtonStyle.blurple, url=data['url'])

            async def order_callback(interaction):
                await interaction.response.send_message("Order Now")

            order.callback = order_callback

            myview = View(timeout=180)
            myview.add_item(order)

            await interaction.send(embed=embed, view=myview)
        elif website.lower() == "swiggy":
            fp = open('Swiggy.json')
            data = json.load(fp)
            embed = nextcord.Embed(title="Swiggy Price Chart", color=0x14aaeb,
                                description="The food item you want to purchase are:", url=data['url'])
            embed.add_field(name='Restaurant_name',
                            value=data['name'], inline=True)
            embed.add_field(name='Speciality',
                            value=data['speciality'], inline=True)
            offerlist = '\n'.join(data['offers'])
            embed.add_field(name='Offers', value=offerlist, inline=False)
            itemlist = '\n'.join(data['Food-items'])
            embed.add_field(name='Item - Price', value=itemlist, inline=False)
            embed.set_image(
                url='https://entrackr-bucket.s3.ap-south-1.amazonaws.com/wp-content/uploads/2022/02/10123018/Swiggy-img.jpg')
            fp.close()
            
            order = Button(label="Order Now", style=ButtonStyle.blurple, url=data['url'])

            async def order_callback(interaction):
                await interaction.response.send_message("Order Now")

            order.callback = order_callback

            myview = View(timeout=180)
            myview.add_item(order)

            await interaction.send(embed=embed, view=myview)
        else:
            await interaction.send("Data not found. Sorry for inconvenience!!")

def setup(bot):
    bot.add_cog(ResultCog(bot))
