import discord
import random
import asyncio
import json
from discord.ext import tasks, commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!',intents=intents)

with open('config.json') as f:
    config = json.load(f)
    token = config['bot_token']
    channel_id = config['channel_id']

def get_random_quote():
    with open('quotes.json') as f:
        js = json.load(f)
        quotes = js['quotes']
    return random.choice(quotes)

@tasks.loop(hours=24)
async def send_quote():
    channel = bot.get_channel(int(channel_id))
    quote = get_random_quote()
    await channel.send(quote)

@bot.event
async def on_ready():
    print('Bot is ready.')
    send_quote.start()

bot.run(token)