import nextcord
from nextcord.ext import commands


class TestCog(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    # @nextcord.slash_command(name="test", guild_ids=[1028619109044326440])
    # async def testing(self, interaction):
    #     await interaction.send("Testing")

    @nextcord.slash_command(name="test2", guild_ids=[1028619109044326440])
    async def test(self, interaction, arg: str):
        await interaction.response.send_message(f"You said {arg}")


def setup(bot):
    bot.add_cog(TestCog(bot))
