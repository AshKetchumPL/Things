import random, os
import discord
from discord.ext import commands, tasks

if __name__ == "__main__":
    TOKEN = "Your token here" # its so you cant import token idk why maby for safety?
    print("Starting...")

intents = discord.Intents().all()
client = commands.Bot(command_prefix="!", case_sensitive=False, intents=intents, owner_ids=[480110129971200010], description="simple bot description")


@tasks.loop(minutes=1)
async def change_status():
    table = ["A simple bot status"]
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=random.choice(table)))

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Starting..."))
    print(f"Logged in as {client.user}!")
    print(f"ping: {round(client.latency * 1000)}ms")
    print(f"Servers: {len(client.guilds)}")
    print(f"Started!")
    change_status.start()

if __name__ == "__main__":
    for file in os.listdir("cogs"):
        if file.endswith(".py") and not file.startswith("-"):
            file_name = file[:-3]
            client.load_extension(f"cogs.{file_name}")
    try:
        client.run(TOKEN)
    except KeyboardInterrupt:
        print("Action stopped by user (Ctrl-C)")
        quit(0)
    except Exception as e:
        print(f"Error: {str(e)} | {str(type(e))}")

else: print("main was imported")