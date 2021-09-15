import os
import sys
import re
import discord
import asyncio

from discord.ext import commands
from ourspace import keep_alive
from .modules import wikibot 


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

        @cmd.event
        async def on_ready():
            print("bot ready!")

        @cmd.command(name="!help")
        async def help(ctx):
            info = "```ourspace```"
            await ctx.send(info)

        @cmd.command(name="!wikipedia")
        async def wikipedia(ctx, *args):

            userInput = " ".join(args)
            lang = (lambda get_label: re.findall('-lang=([\w\d]+)',get_label))(userInput)

            if lang:
                lang = lang[0]

            keyword = re.sub('-(.*?)$','',userInput)
            output = wikibot.wiki(keyword,lang)
            try:
               if output.search_result()['status'] == None:
                  return await ctx.send(output.search_result()['info'])
            except Exception as e:
               await ctx.send(output.search_result())


        @cmd.event
        async def on_command_error(ctx, error):
            if isinstance(error, commands.CommandNotFound):
                pass

        cmd.run(self.token)


def runserver(token):
    keep_alive.keep_alive()
    run = bot(token)
