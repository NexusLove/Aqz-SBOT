# Ur4BOT By Arobqse_

import discord, random, os, sys, math
from time import *
from discord.ext.commands import Bot

pf = '/'
red, blue, green, yellow, purple, pink = (
	0xFA8072, 0x40E0D0, 0x7CFC00,
	0xEEE8AA, 0xDDA0DD, 0xFFC0CB)

add, remove, diagnosis, warn, error = '[+] ', '[-] ', '[*] ', '[!] ', '[x] '
token = input(warn + 'Put your token : ')

bot = Bot(command_prefix=pf, self_bot=True)
bot.remove_command('help')

@bot.event
async def on_ready():
	print(add + bot.user.name + ' : [ON]\n' + diagnosis + bot.user.name + ' ID : ' + bot.user.id)

@bot.command(pass_context = True)
async def load(ctx, time):
	wt = (int(time) / 34)

	def wait():
		sleep(wt)

	await bot.edit_message(ctx.message, '[#                                                       ] `5%`')
	wait()
	await bot.edit_message(ctx.message, '[##                                                    ] `10%`')
	wait()
	await bot.edit_message(ctx.message, '[###                                                 ] `15%`')
	wait()
	await bot.edit_message(ctx.message, '[####                                              ] `20%`')
	wait()
	await bot.edit_message(ctx.message, '[#####                                            ] `25%`')
	wait()
	await bot.edit_message(ctx.message, '[######                                         ] `30%`')
	wait()
	await bot.edit_message(ctx.message, '[#######                                       ] `35%`')
	wait()
	await bot.edit_message(ctx.message, '[########                                    ] `40%`')
	wait()
	await bot.edit_message(ctx.message, '[#########                                 ] `45%`')
	wait()
	await bot.edit_message(ctx.message, '[##########                              ] `50%`')
	wait()
	await bot.edit_message(ctx.message, '[###########                           ] `55%`')
	wait()
	await bot.edit_message(ctx.message, '[############                        ] `60%`')
	wait()
	await bot.edit_message(ctx.message, '[#############                     ] `65%`')
	wait()
	await bot.edit_message(ctx.message, '[##############                  ] `70%`')
	wait()
	await bot.edit_message(ctx.message, '[###############               ] `75%`')
	wait()
	await bot.edit_message(ctx.message, '[################            ] `80%`')
	wait()
	await bot.edit_message(ctx.message, '[#################         ] `85%`')
	wait()
	await bot.edit_message(ctx.message, '[##################      ] `90%`')
	wait()
	await bot.edit_message(ctx.message, '[###################   ] `95%`')
	wait()
	await bot.edit_message(ctx.message, '[####################] `100%`')
	wait()



@bot.command(pass_context = True)
async def uload(ctx, time):
	wt = (int(time) / 34)

	def wait():
		sleep(wt)
	
	while True:
		await bot.edit_message(ctx.message, '[~/.*                ] ')
		wait()
		await bot.edit_message(ctx.message, '[    ~/.*            ] ')
		wait()
		await bot.edit_message(ctx.message, '[        ~/.*        ] ')
		wait()
		await bot.edit_message(ctx.message, '[            ~/.*    ] ')
		wait()
		await bot.edit_message(ctx.message, '[                ~/.*] ')
		wait()
		await bot.edit_message(ctx.message, '[            *.\~    ] ')
		wait()
		await bot.edit_message(ctx.message, '[        *.\~        ] ')
		wait()
		await bot.edit_message(ctx.message, '[    *.\~            ] ')
		wait()
		await bot.edit_message(ctx.message, '[*.\~                ] ')
		wait()
		break

	await bot.delete_message(ctx.message)

@bot.command()
async def play(text):
	await bot.change_presence(game=discord.Game(name=text, type=0))
	embed=discord.Embed(title='Done !', description='Your status has been updated on ' + "'" + text + "'.", color=green)
	await bot.say(embed=embed)

@bot.command()
async def stream(text, link):
	await bot.change_presence(game=discord.Game(name=text, url=link, type=1))
	embed=discord.Embed(title='Done !', description='Your status has been updated on ' + "'" + text + "' with the url : " + link + " .", color=purple)
	await bot.say(embed=embed)

@bot.command()
async def listen(text):
	await bot.change_presence(game=discord.Game(name=text, type=2))
	embed=discord.Embed(title='Done !', description='Your status has been updated on ' + "'" + text + "'.", color=yellow)
	await bot.say(embed=embed)

@bot.command()
async def watch(text):
	await bot.change_presence(game=discord.Game(name=text, type=3))
	embed=discord.Embed(title='Done !', description='Your status has been updated on ' + "'" + text + "'.", color=yellow)
	await bot.say(embed=embed)

@bot.command(pass_context = True)
async def gp(ctx, mention):
	await bot.delete_message(ctx.message)

@bot.command(pass_context = True)
async def calc(ctx, nbr1, op, nbr2):
	await bot.delete_message(ctx.message)

	if op == '+':
		result = (int(nbr1) + int(nbr2))
		embed=discord.Embed(title='Calculator', color=purple)
		embed.set_thumbnail(url='https://cdn2.iconfinder.com/data/icons/freecns-cumulus/16/519630-131_Calculator-128.png')
		embed.add_field(name='Input :', value=str(nbr1) + op + str(nbr2), inline=True)
		embed.add_field(name='Result : ', value=result, inline=False)
		await bot.say(embed=embed)

	elif op == '-':
		result = (int(nbr1) - int(nbr2))
		embed=discord.Embed(title='Calculator', color=purple)
		embed.set_thumbnail(url='https://cdn2.iconfinder.com/data/icons/freecns-cumulus/16/519630-131_Calculator-128.png')
		embed.add_field(name='Input :', value=str(nbr1) + op + str(nbr2), inline=True)
		embed.add_field(name='Result : ', value=result, inline=False)
		await bot.say(embed=embed)

	elif op == '*':
		result = (int(nbr1) * int(nbr2))
		embed=discord.Embed(title='Calculator', color=purple)
		embed.set_thumbnail(url='https://cdn2.iconfinder.com/data/icons/freecns-cumulus/16/519630-131_Calculator-128.png')
		embed.add_field(name='Input :', value=str(nbr1) + op + str(nbr2), inline=True)
		embed.add_field(name='Result : ', value=result, inline=False)
		await bot.say(embed=embed)

	elif op == ':':
		result = (int(nbr1) / int(nbr2))
		embed=discord.Embed(title='Calculator', color=purple)
		embed.set_thumbnail(url='https://cdn2.iconfinder.com/data/icons/freecns-cumulus/16/519630-131_Calculator-128.png')
		embed.add_field(name='Input :', value=str(nbr1) + op + str(nbr2), inline=True)
		embed.add_field(name='Result : ', value=result, inline=False)
		await bot.say(embed=embed)

@bot.command(pass_context = True)
async def ls(ctx, *argv):
	await bot.delete_message(ctx.message)
	lis = {

	'a': '4', 'b': '8', 'c': 'c', 'd': 'd',
	'e': '3', 'f': 'f', 'g': '6', 'h': 'h',
	'i': '1', 'j': 'j', 'k': 'k', 'l': '1',
	'm': 'm', 'n': 'n', 'o': '0', 'p': 'p',
	'q': 'q', 'r': '2', 's': '5', 't': '7',
	'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x',
	'y': 'j', 'z': '2'

	}

	sentence = ''
	for me in argv:
		sentence = sentence + ' ' + str(me)
	sentence = sentence.lower()
	sentence = list(sentence)
	result = ''

	for lettre in sentence:
		if lettre != ' ':
			result += lis[lettre] + ''
		else:
			result += ''

	await bot.say(result)

@bot.command(pass_context = True)
async def md(ctx, lg, code):
	await bot.delete_message(ctx.message)
	await bot.say('```' + lg + '\n' + code + '\n```')

@bot.command(pass_context = True)
async def sl(ctx, msg):
	await bot.delete_message(ctx.message)
	await bot.say('||' + msg + '||')

@bot.command(pass_context = True)
async def stop(ctx):
	ebd_stop = discord.Embed(description='Finished. :leaves:', color=random.choice([red, blue, green, yellow, purple, pink]))
	await bot.say(embed=ebd_stop)
	sys.exit()

bot.run(token, bot=False)