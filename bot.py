import sys,os
import discord
import asyncio
from discord.ext import commands
from src import azlyric
from src import keep_alive

cmd = commands.Bot(command_prefix="", help_command=None)


@cmd.event
async def on_ready():
	print("bot ready!")


@cmd.command(name="!help")
async def help(ctx):
	info = """```
This is bot for find music lyrics
Created by natsuya#8537
thanks to azlyrics.com

usage : !lyric <title>

thanks, enjoy :)
    ```
    """
	await ctx.send(info)


@cmd.command(name="!lyric")
async def lyric(ctx, *args):
	query = " ".join(args)
	if len(query) <= 1:
		return

	c = """
"""
	if azlyric.find(query).result() == None:
		return await ctx.send(
		    "```sorry result not found for {}```".format(query))

	num = 0
	for a in azlyric.find(query).results():
		c += "{}. {}\n".format(num, a["title"])
		num += 1
	await ctx.send("```{}```".format(c))

	def check(author):
		def inner_check(message):
			return message.author == author

		return inner_check

	try:
		msg = await cmd.wait_for(
		    "message", check=check(ctx.author), timeout=30)
		url = azlyric.find(query).results()[int(msg.content)]["url"]
		return await ctx.send("```{}```".format(azlyric.get(url).lyric(), ))
	except IndexError:
		return await ctx.send("the above options are not found")
	except asyncio.TimeoutError as e:
		return await ctx.send("please try again, timeout :)")


@cmd.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		pass

keep_alive.keep_alive()
cmd.run(YOURTOKEN)
# you need a token
