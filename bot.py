import discord
from discord.ext import commands

# Replace 'your_token_here' with your bot's token
TOKEN = 'your_token_here'

# Create a bot instance with the command prefix '/'
bot = commands.Bot(command_prefix='/', intents=discord.Intents.default())

# Role names
REGISTER_ROLE = "🌍 > Зарегистрировать Разрушенная экономика"
UNREGISTERED_ROLE = "📂 > Незарегистрировано"
REQUIRED_ROLE = "📂 > UnRegistered"

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

@bot.command(name='register')
async def register(ctx):
    """Register command - adds Register role and removes Unregistered role"""
    try:
        guild = ctx.guild
        member = ctx.author
        
        # Check if member has the required role
        required_role = discord.utils.get(guild.roles, name=REQUIRED_ROLE)
        
        if required_role is None:
            await ctx.send(f"❌ Role '{REQUIRED_ROLE}' not found on the server.")
            return
        
        if required_role not in member.roles:
            await ctx.send(f"❌ You need the '{REQUIRED_ROLE}' role to use this command!")
            return
        
        # Get the roles
        register_role = discord.utils.get(guild.roles, name=REGISTER_ROLE)
        unregistered_role = discord.utils.get(guild.roles, name=UNREGISTERED_ROLE)
        
        if register_role is None:
            await ctx.send(f"❌ Role '{REGISTER_ROLE}' not found. Please create it first.")
            return
        
        # Add register role
        if register_role not in member.roles:
            await member.add_roles(register_role)
            await ctx.send(f"✅ {member.mention} registered successfully! Role '{REGISTER_ROLE}' added.")
        else:
            await ctx.send(f"ℹ️ {member.mention} already has the '{REGISTER_ROLE}' role.")
        
        # Remove unregistered role if it exists
        if unregistered_role is not None and unregistered_role in member.roles:
            await member.remove_roles(unregistered_role)
            await ctx.send(f"✅ Role '{UNREGISTERED_ROLE}' removed.")
    
    except discord.Forbidden:
        await ctx.send("❌ I don't have permission to manage roles.")
    except Exception as e:
        await ctx.send(f"❌ An error occurred: {str(e)}")

# Run the bot
bot.run(TOKEN)