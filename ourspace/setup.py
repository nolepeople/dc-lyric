import os
import sys
import re
import discord
import asyncio

from discord.ext import commands
from ourspace import keep_alive
from .modules import (
        wikibot,
        connection,
        anisearch,
        )


cmd = commands.Bot(command_prefix="", help_command=None)

class Functions:

    def __init__(self):
        pass

    def check(self,author):
        def inner_check(message):
            return message.author == author
        return inner_check


class bot(object):
    global cmd

    def __init__(self,token):
        self.token = token
        self.check = Functions().check
        self.spamFile = f"{os.getcwd()}/ourspace/modules/spam.txt"

        @cmd.event
        async def on_ready():
            print("bot success running")
            while True:
                await asyncio.sleep(10)
                with open(self.spamFile,'r+') as file:
                    file.truncate(0)

        @cmd.command(name="!help")
        async def help(ctx):
            self.info = f"```ourspace ```"
            await ctx.send(self.info)

        @cmd.command(name="!speedtest")
        async def speedtest(ctx):
            await ctx.send('results will arrive, wait a moment 👍')
            return await ctx.send(connection.SpeedtestResult())

        @cmd.command(name="!anime")
        async def anime(ctx,*args):
            await ctx.send(anisearch.Anime.website())

        @cmd.command(name="!wikipedia")
        async def wikipedia(ctx, *args):
            if not args:
               return await ctx.send('`!help`')

            userInput = " ".join(args)
            lang = (lambda get_label: re.findall('-lang=([\w\d]+)',get_label))(userInput)

            if lang:
                lang = lang[0]
            else:
               lang = "en"

            keyword = re.sub('-(.*?)$','',userInput)
            output = wikibot.wiki(keyword,lang)
            try:
               if output.search_result()['status'] == None:
                  return await ctx.send(output.search_result()['info'])
            except Exception as e:
               await ctx.send(output.search_result())
               try:
                   await ctx.send('Enter the number of your choice (timeout:30s)')
                   msg = await cmd.wait_for('message',check=self.check(ctx.author),timeout=30)
                   options = output.result[int(msg.content)]
                   summary = output.summary(str(options))
                   return await ctx.send(f'{summary}')

               except IndexError:
                   return await ctx.send("the above options are not found")
               except asyncio.TimeoutError as e:
                   return await ctx.send("please try again, timeout")


        @cmd.event
        async def on_message(message):
            counter = 0
            with open(self.spamFile,'r+') as file:
                for lines in file:
                    if lines.strip('\n') == str(message.author.id):
                        counter += 1
                file.writelines(f'{str(message.author.id)}\n')

            if counter > 5:
                await message.channel.send('You are a spammer, I will spam back 😎')

            await cmd.process_commands(message)


        @cmd.event
        async def on_command_error(ctx, error):
            if isinstance(error, commands.CommandNotFound):
                pass

        cmd.run(self.token)


def runserver(token):
    keep_alive.keep_alive()
    run = bot(token)
