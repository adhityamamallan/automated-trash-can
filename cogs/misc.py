import random

import discord
from discord.ext import commands
from utils.configManager import BotConfig, RedditConfig
from utils.misc import uwufy, hmmstring


class Misc(commands.Cog):
    """Miscellaneous commands."""

    def __init__(self, bot):
        self.bot = bot
        self.bot_config = BotConfig()

    @commands.command(
        usage='"<question>" "<option1>" "<option2>" (the quotation marks are important)'
    )
    async def poll(self, ctx, question: str, option1: str, option2: str):
        """Make polls."""

        commandmsg = await ctx.channel.fetch_message(ctx.channel.last_message_id)
        await commandmsg.delete()

        embed = discord.Embed(title=question, color=discord.Color.from_rgb(230, 0, 0))

        embed.add_field(name="A", value=option1, inline=False)
        embed.add_field(name="B", value=option2, inline=False)

        pollmsg = await ctx.send(embed=embed)

        await pollmsg.add_reaction("🇦")
        await pollmsg.add_reaction("🇧")

    @commands.command()
    async def tcsa(ctx):
        """For when someone falls for one of the classic blunders."""
        embed = discord.Embed(
            title = "You fell for it, fool!",
            description = "Thunder Cross Split Attack!"
        )
        embed.set_image(url = "https://i.kym-cdn.com/entries/icons/facebook/000/030/814/Dio_vs_Dire_-_Thunder_Cross_Split_Attack_-_4K_-_JJBA_Part_1_-_%E3%82%B8%E3%83%A7%E3%82%B8%E3%83%A7_1-12_screenshot.jpg")
        await ctx.send(embed = embed)

    @commands.command()
    async def uwu(ctx, *args):
        """Kawaii desu ne senpai uwu .｡･ﾟﾟ･(＞_＜)･ﾟﾟ･｡."""
        if(len(args) > 0):
            msgcontent = " ".join(args)
        else:
            msglist = []
            async for message in ctx.channel.history(limit=10):
                if(not message.content.startswith("$") and not message.content == ''):
                    msglist.append(message.content)
            print(msglist)
            msgcontent = msglist[0]
        await ctx.send(uwufy(msgcontent))

    @commands.command()
    async def hmm(ctx):
        """For when someone says something questionable."""
        await ctx.send(hmmstring())  


def setup(bot):
    """
    Called automatically by discord while loading extension. Adds the Miscellaneous cog on to the bot.
    """
    bot.add_cog(Misc(bot))
