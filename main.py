import os, json, asyncio
from dotenv import load_dotenv
from nextcord.ext import commands
from nextcord import Intents, Interaction, Embed, Activity, ActivityType
from pathlib import Path

helpGuide = json.load(open("help.json"))

load_dotenv()

# DISCORD_TOKEN = os.environ["DISCORD_TOKEN"]
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = os.getenv("GUILD_ID")

intents = Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)
bot.remove_command('help')

# @bot.slash_command(name="ping", description="Just a check command")
# async def ping(interaction: Interaction):
#     embed = Embed(title="Ping", description=f"The bot's ping is {round(bot.latency * 1000)}")
#     await interaction.send(embed=embed)

def extensions():
    files = Path("cogs").rglob("*.py")
    for file in files:
        yield file.as_posix()[:-3].replace("/", ".")

for ext_file in extensions():
    try:
        bot.load_extension(ext_file)
        print(f"Loaded {ext_file}")
    except Exception as ex:
        print(f"Failed to load {ext_file}: {ex}")

@bot.event
async def on_ready():
    await bot.change_presence(activity=Activity(name="Swiggy vs Zomato", type=ActivityType.competing))

async def main():
    await bot.start(DISCORD_TOKEN)

asyncio.run(main())
