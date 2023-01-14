import config
import discord
from discord import Emoji
from discord.ext import commands
import asyncio
from datetime import datetime, timedelta
from collections import Counter
import pandas as pd

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=discord.Intents.all())
bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

task = None
user_reactions = {}
desired_channel_id = config.channel

delete = open("reactions.csv",'w')
delete.close()

@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')
    await bot.change_presence(activity=discord.Game(name="/help"))
    try:
        start_task()
        print("task created")
    except Exception as e:
        print(e)
    try:
        synced = await bot.tree.sync()
        print(f"synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


def stop_task():
    global task
    task.cancel()

def start_task():
    global task
    task = bot.loop.create_task(check_reactions_task())


async def check_reactions_task():
    global user_reactions
    while True:
        user_reactions.clear()
        await check_reactions()
        export_data()
        await asyncio.sleep(60)


async def check_reactions():
    new_user_reactions = {}
    channel = bot.get_channel(desired_channel_id)
    if not channel:
        return
    async for message in channel.history(limit=1000, after=datetime.utcnow() - timedelta(hours=24)):
        for reaction in message.reactions:
            if isinstance(reaction.emoji, Emoji):
                reaction_name = reaction.emoji.name
            else:
                reaction_name = reaction.emoji

            async for user in reaction.users():
                user_id = user.id
                if user_id in new_user_reactions:
                    new_user_reactions[user_id][reaction_name] += 1
                else:
                    new_user_reactions[user_id] = Counter({reaction_name: 1})

    for user_id, reactions in new_user_reactions.items():
        if user_id in user_reactions:
            user_reactions[user_id].update(reactions)
        else:
            user_reactions[user_id] = reactions
    print(user_reactions)


def export_data():
    current_time = datetime.now()
    start_time = current_time.replace(second=0, microsecond=0)
    end_time = start_time - timedelta(hours=24)
    f = open("reactions.csv", 'a')
    f.write("Time Range: {} - {}\n".format(start_time, end_time))
    data = {}
    for user_id, reactions in user_reactions.items():
        for reaction_name, count in reactions.items():
            if user_id not in data:
                data[user_id] = {}
            data[user_id][reaction_name] = count
    df = pd.DataFrame(data).T
    df.index.name = 'User ID'
    df['Timestamp'] = datetime.now()
    csvraw = df.to_csv()
    print(csvraw)
    f.write(csvraw)
    f.close()


@bot.tree.command(name="start")
async def start(interaction: discord.Interaction):
    await interaction.response.defer()
    try:
        if task is None or task.done():
            start_task()
            await interaction.followup.send("Task Started")
    except asyncio.CancelledError as e:
        await interaction.followup.send(e)


@bot.tree.command(name="cancel")
async def cancel(interaction: discord.Interaction):
    await interaction.response.defer()
    try:
        if task:
            stop_task()
            await interaction.followup.send("Task Canceled")
        else:
            await interaction.followup.send("Failed (task already canceled)")
    except asyncio.CancelledError as e:
        await interaction.followup.send(e)

bot.run(config.TOKEN)
