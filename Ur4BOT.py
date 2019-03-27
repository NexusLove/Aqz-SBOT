# Ur4BOT by Arobqse_

import discord, asyncio, random, time, sys, os
from discord.ext.commands import Bot
from colorama import Fore

token = input('Token : ')

red, blue, green, yellow, purple, pink = (

	0xFA8072, 0x40E0D0, 0x7CFC00,
	0xEEE8AA, 0xDDA0DD, 0xFFC0CB

)

add, remove, diagnosis, warn, error = (' [+] ', ' [-] ', ' [*] ', ' [!] ', ' [x] ')

bot = Bot(command_prefix='/', self_bot=True)
bot.remove_command('help')

@bot.event
async def on_ready():
	print(add + bot.user.name + ' : [ON]\n' + diagnosis + bot.user.name + ' ID : ' + bot.user.id)

@bot.command(pass_context = True)
async def help(ctx):
	await bot.delete_message(ctx.message)
	embed = discord.Embed(title='To install Ur4BOT self-bot', url='https://github.com/Ar0basL4/Ur4BOT', color=random.choice([red, blue, green, yellow, purple, pink]))
	embed.set_author(name='Help')
	embed.add_field(name='/sl [msg]', value='Add a spoiler to your message.', inline=False)
	embed.add_field(name='/ls [msg]', value='Add leet speak to your message.', inline=False)
	embed.add_field(name='/hug [user]', value='I love U :3 !', inline=False)
	embed.add_field(name='/uload [time]', value='The message will loaddaol.', inline=False)
	embed.add_field(name='/load [time]', value='The message will looooooooooad.', inline=False)
	embed.add_field(name='/play [txt]', value='Set your custom status to play.', inline=False)
	embed.add_field(name='/stream [link] [txt]', value='Do you want to feel like streamer ? .', inline=False)
	embed.add_field(name='/listen [txt]', value='What is this noise ? .', inline=False)
	embed.add_field(name='/watch [txt]', value='I am watching you.', inline=False)
	embed.add_field(name='/gp [user]', value='Who ping me ? .', inline=False)
	embed.add_field(name='/calc [nbr1] [op] [nbr2]', value='1 + 1 = ? .', inline=False)
	embed.add_field(name='/dm_pub [server_id] [deadline] [msg]', value='If you want to be hated by the community.', inline=False)
	embed.add_field(name='/stop', value='Hoping to see you again.', inline=False)
	await bot.say(embed=embed)

@bot.command(pass_context = True)
async def sl(ctx, *argv):
	await bot.delete_message(ctx.message)
	result = ''

	for word in argv:
		result = result + ' ' + str(word)

	await bot.say('||' + result + '||')

@bot.command(pass_context = True)
async def ls(ctx, *argv):
	await bot.delete_message(ctx.message)

	list = {

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
			result += list[lettre] + ' '

		else:
			result += ' '

	await bot.say(result)

@bot.command(pass_context = True)
async def hug(ctx, user):
	await bot.delete_message(ctx.message)
	hugs = ['https://tenor.com/FQNP.gif', 'https://tenor.com/SjBB.gif', 'https://tenor.com/vQcO.gif']
	author = str(ctx.message.author)
	author, tag = author.split('#')
	await bot.say(str(author) + ' hugging ' + str(user) + ' :heart: ' + random.choice(hugs))

@bot.command(pass_context = True)
async def uload(ctx, time):
	wt = (int(time) / 34)

	def wait():
		asyncio.wait(wt)
	
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

@bot.command(pass_context = True)
async def load(ctx, time):
	wt = (int(time) / 34)

	def wait():
		asyncio.wait(wt)

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
async def play(ctx, *argv):
	await bot.delete_message(ctx.message)

	txt = ''

	for word in argv:
		txt = txt + ' ' + word

	await bot.change_presence(game=discord.Game(name=txt, type=0))
	embed=discord.Embed(title='Done !', description='Your status has been updated on ' + "'" + txt + "'.", color=green)
	await bot.say(embed=embed)

@bot.command(pass_context = True)
async def stream(ctx, link, *argv):
	await bot.delete_message(ctx.message)

	txt = ''

	for word in argv:
		txt = txt + ' ' + word

	await bot.change_presence(game=discord.Game(name=txt, url=link, type=1))
	embed=discord.Embed(title='Done !', description='Your status has been updated on ' + "'" + txt + "' with the url : " + link + " .", color=purple)
	await bot.say(embed=embed)

@bot.command(pass_context = True)
async def listen(ctx, *argv):
	await bot.delete_message(ctx.message)

	txt = ''

	for word in argv:
		txt = txt + ' ' + word

	await bot.change_presence(game=discord.Game(name=txt, type=2))
	embed=discord.Embed(title='Done !', description='Your status has been updated on ' + "'" + txt + "'.", color=yellow)
	await bot.say(embed=embed)

@bot.command(pass_context = True)
async def watch(ctx, *argv):
	await bot.delete_message(ctx.message)

	txt = ''

	for word in argv:
		txt = txt + ' ' + word

	await bot.change_presence(game=discord.Game(name=txt, type=3))
	embed=discord.Embed(title='Done !', description='Your status has been updated on ' + "'" + txt + "'.", color=yellow)
	await bot.say(embed=embed)

@bot.command(pass_context = True)
async def gp(ctx):
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
	
	else:
		pass

@bot.command(pass_context = True)
async def dm_pub(ctx, server_id, time, *argv):
	await bot.delete_message(ctx.message)

	msg = ''

	for word in argv:
		msg = msg + ' ' + word

	for server in bot.servers:

		if int(server.id) == int(server_id):

			for member in server.members:
				time.sleep(int(time))

				try:
					await bot.send_message(member, msg)

				except:
					pass
		else:
			pass

@bot.command(pass_context = True)
async def stop(ctx):
	await bot.delete_message(ctx.message)
	embed = discord.Embed(description='See you soon ! :leaves:', color=random.choice([red, blue, green, yellow, purple, pink]))
	await bot.say(embed=embed)
	sys.exit()

bot.run(token, bot=False)
