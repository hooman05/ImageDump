import discord
from discord.ext import commands
import random
import time
from datetime import datetime
#import datetime

bot = commands.Bot(command_prefix=".")
bot.remove_command('help')

@bot.event
async def on_ready():
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    print(date_time)
    Cmd_Record = open("DiscordCmdLog_rebot.txt", "a")#
    Cmd_Record.write("\n\n---------------------------------")
    Cmd_Record.write(f"\nrestart | {date_time}")
    Cmd_Record.write("\n---------------------------------")
    print('bot is ready')
    print('logged in as:')
    print(bot.user.name)


#HELP command
@bot.command(pass_context = True)
async def help(ctx):
    author = ctx.message.author
    print(f'sent help to {author}')
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    Cmd_Record = open("DiscordCmdLog_rebot.txt", "a")
    Cmd_Record.write(f"\n{author} used; help | {date_time}")
    Cmd_Record.close()

    embed = discord.Embed(colour = discord.Colour.orange())

    #embed.add_field(name = '', value = '', inline = False)
    embed.set_author(name = 'help is here friend')
    embed.add_field(name = '.ping', value = 'returns ping along with bot latency', inline = False)
    embed.add_field(name = '.8ball', value = "its what it says on the tin. just make sure u add a question on the end or it won't work", inline = False)
    embed.add_field(name = '.purge', value = 'clears a given amount of messages (e.g."clear 4" this will clear 4 messages including the cmd itself)', inline = False)
    embed.add_field(name = '.smith', value = 'just type it in', inline = False)
    embed.add_field(name = '.og', value = 'again... just try it', inline = False)
    embed.add_field(name = '.creeper', value = 'gives the expeced response', inline = False)
    embed.add_field(name = '.embed', value = 'what ever u type after the initial cmd will be put into an embed. your username will automatically be added at the end of the embed.', inline = False)
    embed.add_field(name = '.cmdlog', value = 'gives a log of all commands written', inline = False)

    embed.add_field(name = '...........................', value = "more commands comming soon. :P", inline = False)
    embed.add_field(name = 'from', value = "thee superior bot. quick note i'm not always onlne, i can only be online once my creator is on because i'm being hosted locally but soon enough i'll be up 2/47 (with the exception of getting a restart which will be me getting an update)", inline = False)

    await ctx.send(embed = embed)
#/HELP command

@bot.command()
async def ping(ctx): #gets ping value
    author = ctx.message.author
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    print(f'\n{author} used ping | {date_time}')
    Cmd_Record = open("DiscordCmdLog_rebot.txt", "a")
    Cmd_Record.write(f"\n{author} used; ping")
    Cmd_Record.close()
    await ctx.send(f'pong! {round(bot.latency * 1000)}ms')

@bot.command(aliases = ['8ball', 'test'])
async def _8ball(ctx, *, qusetion): #ask the 8
    author = ctx.message.author
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    print(f'\n{author} used 8ball | {date_time}')
    Cmd_Record = open("DiscordCmdLog_rebot.txt", "a")
    Cmd_Record.write(f"\n{author} used; 8ball")
    Cmd_Record.close()
    responses = [
                'It is certain.',
                'It is decidedly so.',
                'Without a doubt.',
                'Yes - definitely.',
                'You may rely on it.',
                'As I see it, yes.',
                'Most likely.',
                'Outlook good.',
                'Yes.',
                'Signs point to yes.',
                'Reply hazy, try again.',
                'Ask again later.',
                'Better not tell you now.',
                'Cannot predict now.',
                'Concentrate and ask again.',
                "Don't count on it.",
                'My reply is no.',
                'My sources say no.',
                'Outlook not so good.',
                'Very doubtful'
                ] #responses the command will give
    await ctx.send(f'Question: {qusetion}\nAnswer: {random.choice(responses)}')

@bot.command()
async def purge(ctx, amount = 2): #clears given amount of messages
    author = ctx.message.author
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    await ctx.channel.purge(limit = amount)
    print(f'{author} cleared', amount, ' messages')
    Cmd_Record = open("DiscordCmdLog_rebot.txt", "a")
    Cmd_Record.write(f"\n{author} cleared {amount} lines | {date_time}")
    Cmd_Record.close()

@bot.command()
async def smith(ctx):
        author = ctx.message.author
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

        print(f'\n{author} used smith')
        Cmd_Record = open("DiscordCmdLog_rebot.txt", "a")
        Cmd_Record.write(f"\n{author} used; smith | {date_time}")
        Cmd_Record.close()
        responses = [
                    'StOp sInGinG',
                     'AAAAAAAAHHHHHHHH'
                     ]
        await ctx.send(f'{random.choice(responses)}')

@bot.command()
async def og(ctx):
        author = ctx.message.author
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

        print(f'\n{author} used smith | {date_time}')
        Cmd_Record = open("DiscordCmdLog_rebot.txt", "a")
        Cmd_Record.write(f"\n{author} used; smith")
        Cmd_Record.close()
        responses = ['sshhhhhllappp a "h" on it',
                     'hello?... cabbage']
        await ctx.send(f'{random.choice(responses)}')

@bot.command()
async def creeper(ctx):
    author = ctx.message.author
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

    print(f'\n{author} used creeper | {date_time}')
    Cmd_Record = open("DiscordCmdLog_rebot.txt", "a")
    Cmd_Record.write(f"\n{author} used; creeper")
    Cmd_Record.close()
    await ctx.send(f'awwwwwwwww man!!!!!!!!!!')

@bot.command()
async def cmdlog(ctx):
    #await ctx.author.send('hopefully this is in ur dms')
    Cmd_Record = open("DiscordCmdLog_rebot.txt", "r")
    log = Cmd_Record.read()
    Cmd_Record.close()
    await ctx.author.send(log)

@bot.command()
async def embed(ctx, *, msg):
    await ctx.channel.purge(limit = 1)
    author = ctx.message.author
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    Cmd_Record = open("DiscordCmdLog_rebot.txt", "a")
    Cmd_Record.write(f"\n{author} used; embed to embed {msg}")
    Cmd_Record.close()

    embed = discord.Embed(colour = discord.Colour.orange())
    embed.add_field(name = f'{msg}', value = f'({author})', inline = False)

    await ctx.send(embed = embed)

@bot.command()
async def changeCol(ctx, role_name, colour):
    for role in server.roles:
        if role.name == 'role_name':
            # What you want to do.
            await client.edit_role(server=server, role=role, colour=colour)
            break

bot.run('NjMxODI4NDEyMjkzNTc4NzU4.XaDb_g.gJ4oO4vZjCP_VxOcRhxfcG98s8w')
