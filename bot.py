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
    
    # Allow commands to be processed
    await bot.process_commands(message)

# Run the bot
bot.run(TOKEN)