# AroSBOT by Arobqze_

from discord.ext.commands import Bot
import discord
import asyncio
import random
import base64
import json
import sys
import os

with open("core/settings.json", "r") as dump:
	settings = json.load(dump)

footer, color, link = ("AroSBOT • by Arobqze_", 0xFFA500, settings["stream"]["link"])

bot = Bot(command_prefix=settings["login"]["prefix"], self_bot=True)
bot.remove_command("help")


@bot.event
async def on_ready():
	print(
		" [+] {} : [ON]\n [*] Tag : {}\n [*] ID : {}".format(
			bot.user.name, bot.user.discriminator, bot.user.id
		)
	)


async def status_task():

	while True:
		await bot.change_presence(
			game=discord.Game(name=settings["stream"]["1"], url=link, type=1)
		)
		await asyncio.sleep(9)
		await bot.change_presence(
			game=discord.Game(name=settings["stream"]["2"], url=link, type=1)
		)
		await asyncio.sleep(9)
		await bot.change_presence(
			game=discord.Game(name=settings["stream"]["3"], url=link, type=1)
		)
		await asyncio.sleep(9)


@bot.command(pass_context=True, aliases=["help"])
async def options(ctx):
	await bot.delete_message(ctx.message)
	embed = discord.Embed(
		title="**Install AroSBOT selfbot**",
		url="https://github.com/Arobqse9/AroSBOT",
		color=color,
	)
	embed.set_author(name="Help | Options")
	embed.add_field(
		name="/clear | purge <nbr>", value="`Clear messages.`", inline=False
	)
	embed.add_field(
		name="/embed | emb | e <txt>", value="`Embed is comming !`", inline=False
	)
	embed.add_field(
		name="/gettkn <uid>", value="`Not entirely but still nice.`", inline=False
	)
	embed.add_field(
		name="/ghostping | gp <user>", value="`Who ping me ?`", inline=False
	)
	embed.add_field(name="/hug <user>", value="`I love you ! :3`", inline=False)
	embed.add_field(
		name="/load <time>", value="`The message will looooooooooad.`", inline=False
	)
	embed.add_field(name="/loadnick | lnick", value="`I N S A N E`", inline=False)
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
	embed.add_field(name="/spamreact | sreact", value="`COMCOMBRE !!!`", inline=False)
	embed.add_field(
		name="/exit | stop", value="`Hoping to see you again.`", inline=False
	)
	embed.set_footer(text=footer)
	await bot.say(embed=embed)


@bot.command(pass_context=True, aliases=["purge"])
async def clear(ctx, nbr):
	await bot.delete_message(ctx.message)
	msgs = []

	async for msg in bot.logs_from(ctx.message.channel, limit=int(nbr) + 1):
		msgs.append(msg)

	try:
		await bot.delete_messages(msgs)

	except:
		pass


@bot.command(pass_context=True, aliases=["emb", "e"])
async def embed(ctx, *argv):
	await bot.delete_message(ctx.message)
	txt = ""
	
	for word in argv:
		txt = txt + " " + word

	embed = discord.Embed(description=str(txt), color=color)
	embed.set_footer(text=footer)
	await bot.say(embed=embed)


@bot.command(pass_context=True)
async def gettkn(ctx, uid):
	await bot.delete_message(ctx.message)
	reply = base64.b64encode(uid.encode())
	reply = str(reply)
	await bot.say(
		"<@{}> __Token begin__ : `{}`".format(
			uid, reply.replace("b'", "").replace("'", "")
		)
	)


@bot.command(pass_context=True, aliases=["gp"])
async def ghostping(ctx):
	await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def hug(ctx, user):
	await bot.delete_message(ctx.message)
	hugs = [
		"https://tenor.com/FQNP.gif",
		"https://tenor.com/SjBB.gif",
		"https://tenor.com/vQcO.gif",
	]
	await bot.say(
		str(bot.user.name)
		+ " hugging **"
		+ str(user)
		+ "** :heart: "
		+ random.choice(hugs)
	)


@bot.command(pass_context=True)
async def load(ctx):
	await bot.edit_message(ctx.message, "[~/.*                ] ")
	await bot.edit_message(ctx.message, "[    ~/.*            ] ")
	await bot.edit_message(ctx.message, "[        ~/.*        ] ")
	await bot.edit_message(ctx.message, "[            ~/.*    ] ")
	await bot.edit_message(ctx.message, "[                ~/.*] ")
	await bot.edit_message(ctx.message, "[            *.\~    ] ")
	await bot.edit_message(ctx.message, "[        *.\~        ] ")
	await bot.edit_message(ctx.message, "[    *.\~            ] ")
	await bot.edit_message(ctx.message, "[*.\~                ] ")
	await bot.delete_message(ctx.message)


@bot.command(pass_context=True, aliases=["lnick"])
async def loadnick(ctx):
	await bot.delete_message(ctx.message)

	while True:
		name = ""

		for letter in bot.user.name:
			name = name + letter
			await bot.change_nickname(ctx.message.author, name)


@bot.command(pass_context=True, aliases=["mstream"])
async def mstreaming(ctx):
	await bot.delete_message(ctx.message)
	bot.loop.create_task(status_task())


@bot.command(pass_context=True, aliases=["stream", "listen", "watch"])
async def play(ctx, *argv):
	await bot.delete_message(ctx.message)

	txt = ""

	for word in argv:
		txt = txt + " " + word

	if "/play" in ctx.message.content:
		await bot.change_presence(game=discord.Game(name=txt, type=0))

	elif "/streaming" in ctx.message.content or "/stream" in ctx.message.content:
		await bot.change_presence(
			game=discord.Game(name=txt, url=settings["stream"]["link"], type=1)
		)

	elif "/listen" in ctx.message.content:
		await bot.change_presence(game=discord.Game(name=txt, type=2))

	elif "/watch" in ctx.message.content or "/look" in ctx.message.content:
		await bot.change_presence(game=discord.Game(name=txt, type=3))

	else:
		pass


@bot.command(pass_context=True, aliases=["sreact"])
async def spamreact(ctx, nbr):
	await bot.delete_message(ctx.message)

	async for msg in bot.logs_from(ctx.message.channel, limit=int(nbr)):

		try:
			await bot.add_reaction(msg, emoji="🍆")

		except:
			pass


@bot.command(pass_context=True, aliases=["stop"])
async def exit(ctx):
	await bot.delete_message(ctx.message)
	embed = discord.Embed(description="See you soon ! :leaves:", color=color)
	embed.set_footer(text=footer)
	await bot.say(embed=embed)
	sys.exit()


try:
	bot.run(settings["login"]["token"], bot=False)

except:
	print("[!] Loading error, check the token validity.")
