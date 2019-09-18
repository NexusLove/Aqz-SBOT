#!/usr/bin/env python3

from discord.ext import commands
import discord
import asyncio
import hashlib
import random
import base64
import json

with open("settings.json", "r") as dump:
	settings = json.load(dump)

footer, color, link = ("HiveNet • by NexusLove", 0xFAF684, settings["link"])

bot = commands.Bot(command_prefix=settings["prefix"], self_bot=True)
bot.remove_command("help")


@bot.event
async def on_ready():
	print("\n [+] {} : [ON] | Tag : {}\n [*] ID : {}".format(bot.user.name, bot.user.discriminator, bot.user.id))


async def status_task():
	while True:
		await bot.change_presence(
			activity=discord.Streaming(name=settings["1"], url=link)
		)
		await asyncio.sleep(9)
		await bot.change_presence(
			activity=discord.Streaming(name=settings["2"], url=link)
		)
		await asyncio.sleep(9)
		await bot.change_presence(
			activity=discord.Streaming(name=settings["3"], url=link)
		)
		await asyncio.sleep(9)


@bot.command(pass_context=True, aliases=["help"])
async def options(ctx, category=None):
	await ctx.message.delete()

	"""
	if category == None:
		embed = discord.Embed(title="**Install HiveNet**", url="https://github.com/NexusLove/", color=0xFF7676)
		embed.set_author(name="Help - Options")
		embed.add_field(name="Help gui's", value="• fun\n• util\n• status\n• other\n• all", inline=True)

	elif category == "fun":
		embed = discord.Embed(title="Fun Help")

	embed.set_footer(text="HiveNet • by NexusLove")
	await ctx.send(embed=embed)

	"""
	embed = discord.Embed(
		title="**Install HiveNet**",
		url="https://github.com/NexusLove",
		color=color,
	)
	embed.set_author(name="Help | Options")
	embed.add_field(
		name="/avatar <@user>", value="`Clear messages.`", inline=False
	)
	embed.add_field(
		name="/clear | purge <nbr>", value="`Clear messages.`", inline=False
	)
	embed.add_field(
		name="/embed | emb | e <txt>", value="`Embed is comming !`", inline=False
	)
	embed.add_field(
		name="/gettkn <member>", value="`Not entirely but still nice.`", inline=False
	)
	embed.add_field(
		name="/ghostping | gp <@user>", value="`Who ping me ?`", inline=False
	)
	embed.add_field(name="/hug <@user>", value="`I love you ! :3`", inline=False)
	embed.add_field(
		name="/load <time>", value="`The message will looooooooooad.`", inline=False
	)
	# embed.add_field(name="/loadnick | lnick", value="`I N S A N E`", inline=False)
	embed.add_field(
		name="/mstreaming | mstream <txt>",
		value="`Community manager ! :p`",
		inline=False,
	)
	embed.add_field(
		name="/play <txt>", value="`Set your custom status to play.`", inline=False
	)
	embed.add_field(
		name="/streaming | stream <txt>",
		value="`Do you want to feel like streamer ?`",
		inline=False,
	)
	embed.add_field(name="/listen <txt>", value="`What is this noise ?`", inline=False)
	embed.add_field(
		name="/watch | look <txt>", value="`I am watching you.`", inline=False
	)
	# embed.add_field(name="/quote | qt", value="`Do not deny it, you said it.`", inline=False)
	# embed.add_field(name="/spamreact | sreact", value="`COMCOMBRE !!!`", inline=False)
	embed.add_field(
		name="/exit | stop", value="`Hoping to see you again.`", inline=False
	)
	embed.set_footer(text=footer)
	await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def avatar(ctx, user: discord.Member):
	await ctx.message.delete()
	await ctx.send(user.avatar_url)


@bot.command(pass_context=True, aliases=["purge"])
async def clear(ctx, msgs):
	await ctx.message.delete()
	await ctx.message.channel.purge(limit=int(msgs))

@bot.command(pass_context=True, aliases=["emb", "e"])
async def embed(ctx, *argv):
	await ctx.message.delete()
	txt = ""

	for word in argv:
		txt = txt + " " + word

	embed = discord.Embed(description=str(txt), color=color)
	await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def gettkn(ctx, member: discord.Member):
	await ctx.message.delete()
	reply = base64.b64encode(str(member.id).encode())
	await ctx.send("{} __Token begin__ : `{}`".format(member.mention, reply.decode()))


@bot.command(pass_context=True, aliases=["gp"])
async def ghostping(ctx):
	await ctx.message.delete()


@bot.command(pass_context=True)
async def hug(ctx, user):
	await ctx.message.delete()
	hugs = [
		"https://tenor.com/FQNP.gif",
		"https://tenor.com/SjBB.gif",
		"https://tenor.com/vQcO.gif",
	]
	await ctx.send(
		str(bot.user.name)
		+ " hugging **"
		+ str(user)
		+ "** :heart: "
		+ random.choice(hugs)
	)


@bot.command(pass_context=True)
async def load(ctx):
	await ctx.message.edit(content="[~/.*                ] ")
	await ctx.message.edit(content="[    ~/.*            ] ")
	await ctx.message.edit(content="[        ~/.*        ] ")
	await ctx.message.edit(content="[            ~/.*    ] ")
	await ctx.message.edit(content="[                ~/.*] ")
	await ctx.message.edit(content="[            *.\~    ] ")
	await ctx.message.edit(content="[        *.\~        ] ")
	await ctx.message.edit(content="[    *.\~            ] ")
	await ctx.message.edit(content="[*.\~                ] ")
	await ctx.message.delete()


@bot.command(pass_context=True, aliases=["lnick"])
async def loadnick(ctx):
	await ctx.message.delete()

	while True:
		name = ""

		for letter in bot.user.name:
			name = name + letter
			await ctx.message.author.edit(nick=name)


@bot.command(pass_context=True)
async def md5c(ctx, *argv):
	await ctx.message.delete()

	txt = ""

	for word in argv:
		txt = txt + " " + word

	result = hashlib.md5(txt.encode("utf-8"))
	await ctx.send("`{}`".format(result.hexdigest()))


@bot.command(pass_context=True, aliases=["mstream"])
async def mstreaming(ctx):
	await ctx.message.delete()
	bot.loop.create_task(status_task())


@bot.command(pass_context=True, aliases=["stream", "listen", "watch"])
async def play(ctx, *argv):
	await ctx.message.delete()

	txt = ""

	for word in argv:
		txt = txt + " " + word

	if settings["prefix"] + "play" in ctx.message.content:
		await bot.change_presence(activity=discord.Game(name=txt))

	elif settings["prefix"] + "streaming" in ctx.message.content or settings["prefix"] + "stream" in ctx.message.content:
		await bot.change_presence(activity=discord.Streaming(name=txt, url=link))

	elif settings["prefix"] + "listen" in ctx.message.content:
		await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=txt))

	elif settings["prefix"] + "watch" in ctx.message.content or settings["prefix"] + "look" in ctx.message.content:
		await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=txt))


 # Temporarily unavailable #

"""
@bot.command(pass_context=True, aliases=["qt"])
async def quote(ctx, msg_id):
	await ctx.message.delete()

	msgs = await ctx.channel.history(limit=123).flatten()

	for msg in msgs:
		print(msg.content)
		if msg.id == msg_id:
			embed = discord.Embed(title=msg.content, color=color)
			embed.set_author(
				name="{} said :".format(msg.author.name), icon_url=msg.author.avatar_url
			)
			await ctx.send(embed=embed)
"""


 # Temporarily unavailable #

"""
@bot.command(pass_context=True, aliases=["sreact"])
async def spamreact(ctx, nbr):
	await ctx.message.delete()

	async for msg in bot.logs_from(ctx.message.channel, limit=int(nbr)):

		try:
			await bot.add_reaction(msg, emoji="🍆")

		except:
			pass
"""

@bot.command(pass_context=True, aliases=["stop"])
async def exit(ctx):
	await ctx.message.delete()
	await bot.logout()


try:
	bot.run(settings["token"], bot=False)

except:
	print(" [!] Loading error, please check the token validity.")
