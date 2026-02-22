import discord
from discord.ext import commands

# Replace 'your_token_here' with your bot's token
TOKEN = 'your_token_here'

# Create a bot instance with the command prefix '!' 
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.event
async def on_message(message):
    # Prevent the bot from replying to itself
    if message.author == bot.user:
        return

    # Respond to a specific message
    if message.content == 'Hello bot!':
        await message.channel.send('Hello! How can I help you today?')

    # Allow commands to be processed
    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Run the bot
bot.run(TOKEN)