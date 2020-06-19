import discord
from discord.ext import commands
from botInfo import *

class botClass:
    def __init__(self,botToken,botImageURL=None,botDescription=None,prefix="!"):
        self.token=botToken
        self.imgURL=botImageURL
        self.description=botDescription
        self.prefix=prefix
        self.bot = commands.Bot(command_prefix=self.prefix, description=self.description)

    def setup(self):
        @self.bot.event
        async def on_ready():
            print('------')
            print('Logged as')
            print(self.bot.user.name)
            print(self.bot.user.id)
            print('------')
            game = discord.Game("disc bot start")
            await self.bot.change_presence(status=discord.Status.online, activity=game)

        @self.bot.command()
        async def github(ctx):
            embed = discord.Embed(color=0x523063,title="Github Repository")
            embed.set_thumbnail(url="https://github.githubassets.com/images/modules/open_graph/github-mark.png")
            embed.set_author(name="OriolFilter",url="https://github.com/OriolFilter",icon_url="https://avatars2.githubusercontent.com/u/55088942")
            embed.add_field(name="Link:", value="https://github.com/OriolFilter/Hello-World", inline=False)
            await ctx.send(embed=embed)

    def help(self):pass


    def helloWorldCommands(self):
        @self.bot.command()
        async def hjava(ctx):
            embed = discord.Embed(color=0xffba66,title="Java Hello World")
            embed.set_thumbnail(url="https://galaxyproject.org/images/logos/JavaLogo.png")
            embed.set_author(name="Java Hello World")
            embed.add_field(name="W3Schools", value="https://www.w3schools.com/java/default.asp", inline=False)
            embed.add_field(name="Interactive Tutorials", value="https://www.learnjavaonline.org/", inline=False)
            embed.add_field(name="Javatpoint", value="https://www.javatpoint.com/simple-program-of-java", inline=False)
            await ctx.send(embed=embed)

        @self.bot.command()
        async def hjs(ctx):
            embed = discord.Embed(color=0xffd866, title="JavaScript   Hello World")
            embed.set_thumbnail(url="https://lh3.googleusercontent.com/proxy/zJj7-z906Mq8uF6ycSRPjU0llTykasvp-YWmhxsmLpM-is5Mac8umpHp1vj-nFytwHQbeLORbHIH_lyid8uiAzwmNncgkaoCYSxRwZyElul_UQNrUYY3Xy5kwQ3ingJrcSc3C5g5hUM1")
            embed.set_author(name="JavaScript   Hello World")
            embed.add_field(name="W3Schools", value="https://www.w3schools.com/js/default.asp", inline=False)
            embed.add_field(name="Interactive Tutorials", value="https://www.learn-js.org/", inline=False)
            embed.add_field(name="JavaScript.info", value="https://javascript.info/hello-world", inline=False)
            embed.add_field(name="digitalocean", value="https://www.digitalocean.com/community/tutorials/how-to-write-your-first-javascript-program", inline=False)
            embed.add_field(name="JavaScriptTutorial", value="https://www.javascripttutorial.net/javascript-hello-world/", inline=False)
            await ctx.send(embed=embed)

        @self.bot.command()
        async def hpy(ctx):
            embed = discord.Embed(color=0x9ec3ff, title="Python Hello World")
            embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png")
            embed.set_author(name="Python   Hello World")
            embed.add_field(name="W3Schools", value="https://www.w3schools.com/python/default.asp", inline=False)
            embed.add_field(name="Interactive Tutorials", value="https://www.learnpython.org/en/Hello,_World!", inline=False)
            embed.add_field(name="JavaScript.info", value="https://javascript.info/hello-world", inline=False)
            embed.add_field(name="Programiz", value="https://www.programiz.com/python-programming/examples/hello-world", inline=False)
            await ctx.send(embed=embed)

        @self.bot.command()
        async def hphp(ctx):
            embed = discord.Embed(color=0xa0bbeb, title="PHP Hello World")
            embed.set_thumbnail(url="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1200px-Python-logo-notext.svg.png")
            embed.set_author(name="PHP Hello World")
            embed.add_field(name="W3Schools", value="https://www.w3schools.com/php/default.asp", inline=False)
            embed.add_field(name="Interactive Tutorials", value="https://www.learn-php.org/", inline=False)
            embed.add_field(name="Wikibooks", value="https://en.wikibooks.org/wiki/PHP_Programming/Beginning_with_%22Hello_World!%22", inline=False)
            embed.add_field(name="PHP.net", value="https://www.php.net/manual/en/tutorial.firstpage.php", inline=False)
            await ctx.send(embed=embed)



    def helpSetup(self):
        self.bot.remove_command('help')
        @self.bot.command()
        async def help(ctx, command=None):
            if command is None:
                messageInfo="""\n\t**{prefix}help**:         Show this menu\n
                            \t**{prefix}help <command>**:      Show info only from the specified command\n
                            \t**{prefix}github**:           Show the github repo from the project\n""".format(prefix=self.prefix)

                messageHelloWorld="""\t**{prefix}hjava**:             Show links to start learning Java \n
                                    \t**{prefix}hpy**:            Show links to start learning Python  \n
                                    \t**{prefix}hphp**:               Show links to start learning PHP \n
                                    \t**{prefix}hjs**:                Show links to start learning JavaScript\n""".format(prefix=self.prefix)

                embed = discord.Embed(color=0x917c7c)
                # embed.set_author(name=authName, url=authLink, icon_url=URL)
                embed.set_author(name="Help")
                embed.set_thumbnail(url=self.imgURL)
                # embed.add_field(name=, value=value, inline=False)
                embed.add_field(name="Info", value=messageInfo, inline=False)
                embed.add_field(name="Hello world", value=messageHelloWorld, inline=False)
                # embed.set_footer(text=footer)
                # await self.bot.say(embed=embed)
                await ctx.send(embed=embed)
            else: #Switch insted of is
                if command is 'hjava': ctx.send('Show links to start learning Java')
                elif command is 'hpy': ctx.send('Show links to start learning Python')
                elif command is 'hphp': ctx.send('Show links to start learning PHP')
                elif command is 'hhjs': ctx.send('Show links to start learning JavaScript')
                elif command is 'help': ctx.send('Show a list of commands aviable')
                elif command is 'github': ctx.send('Show the github repo from the project')

                else: await ctx.send('The command was not found')



    def start(self):self.bot.run(self.token)

helloWorld=botClass(botToken=token,botImageURL=discordBotImgUrl,botDescription=description,prefix=prefix)


helloWorld.setup()
helloWorld.helloWorldCommands()
helloWorld.helpSetup()
helloWorld.start()
