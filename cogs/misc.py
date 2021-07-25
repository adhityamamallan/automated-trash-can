import asyncio
import random

import discord
from discord.ext import commands
from numpy import base_repr

from utils.configManager import BotConfig, RedditConfig
from utils import misc, consts


class Misc(commands.Cog):
    """Miscellaneous commands."""

    def __init__(self, bot):
        self.bot = bot
        self.bot_config = BotConfig()

    def mentions_bot(self, message):
        for mention in message.mentions:
            if mention == self.bot.user:
                return True
        return False

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if self.mentions_bot(message):
            await message.reply(content="Bish whet")

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
    async def giveaway(self, ctx, user: str, item: str):
        """Start a giveaway."""

        commandmsg = await ctx.channel.fetch_message(ctx.channel.last_message_id)
        await commandmsg.delete()

        if not item:
            errmsg = await ctx.send("I, for one, would not like to win nothing")
            await asyncio.sleep(5)
            await errmsg.delete()
            return
        if not user:
            errmsg = await ctx.send("Who's hosting the giveaway?")
            await asyncio.sleep(5)
            await errmsg.delete()
            return

        giveawaymsg = await ctx.send(embed=misc.get_giveaway_embed(user, item))

        await giveawaymsg.add_reaction(consts.pbag)

        giveaway_id = base_repr(giveawaymsg.id, 36)

        giveawaymsg.embeds[0].set_footer(
            text="Type $end {0} to end this giveaway.".format(giveaway_id)
        )
        await giveawaymsg.edit(embed=giveawaymsg.embeds[0])

    @commands.command(
        usage="<giveaway ID> (or just $end to end the last active giveaway)"
    )
    async def end(self, ctx, *args):
        """End/reroll a giveaway."""

        commandmsg = await ctx.channel.fetch_message(ctx.channel.last_message_id)
        await commandmsg.delete()

        if len(args) > 0:
            msgid = int(" ".join(args), base=36)
        else:
            msglist = []
            async for message in ctx.channel.history(limit=10):
                if message.embeds:
                    print(message.id)
                    msglist.append(message.id)
            msgid = msglist[0]
        try:
            giveawaymsg = await ctx.channel.fetch_message(msgid)
        except:
            ctx.send("That message does not seem to exist. Please check and try again.")

        users = await giveawaymsg.reactions[0].users().flatten()

        sponsor, prize = misc.get_giveaway_props(giveawaymsg.embeds[0])

        users.remove(self.bot.user)
        try:
            winner = random.choice(users)
        except:
            await ctx.channel.send(
                "Looks like no one has entered this giveaway yet. Oops."
            )
            return
        await ctx.channel.send(
            "{0} has won the giveaway! Congratulations!".format(winner.mention)
        )

        await giveawaymsg.edit(
            embed=misc.get_giveaway_winner_embed(winner, sponsor, prize, giveawaymsg.id)
        )

    @commands.command()
    async def tcsa(ctx):
        """For when someone falls for one of the classic blunders."""
        embed = discord.Embed(
            title="You fell for it, fool!", description="Thunder Cross Split Attack!"
        )
        embed.set_image(
            url="https://i.kym-cdn.com/entries/icons/facebook/000/030/814/Dio_vs_Dire_-_Thunder_Cross_Split_Attack_-_4K_-_JJBA_Part_1_-_%E3%82%B8%E3%83%A7%E3%82%B8%E3%83%A7_1-12_screenshot.jpg"
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def uwu(ctx, *args):
        """Kawaii desu ne senpai uwu .｡･ﾟﾟ･(＞_＜)･ﾟﾟ･｡."""
        if len(args) > 0:
            msgcontent = " ".join(args)
        else:
            msglist = []
            async for message in ctx.channel.history(limit=10):
                if not message.content.startswith("$") and not message.content == "":
                    msglist.append(message.content)
            print(msglist)
            msgcontent = msglist[0]
        await ctx.send(misc.uwufy(msgcontent))

    @commands.command()
    async def hmm(ctx):
        """For when someone says something questionable."""
        await ctx.send(misc.hmmstring())

    @commands.command(usage="<website to hack>")
    async def hack(ctx, website):
        """Use with extreme caution"""
        ctx.send(
            embed=discord.Embed(
                title="{0} mainframe breached, click here to initiate hack".format(
                    website
                ),
                url="https://hackertyper.net/",
                description="You'll need at least 3 VPNs or else your computer will get COVID-20",
            )
        )

    @giveaway.error
    async def giveawayError(self, ctx, error):
        """
        Error handler for the giveaway command
        """
        if isinstance(error, commands.errors.MissingRequiredArgument):
            errmsg = await ctx.send(
                "You might have forgotten to include either the prize or the user."
            )
            await asyncio.sleep(5)
            errmsg.delete()
        else:
            print(ctx.channel.id, "Oopsie, exception: ", error)


def setup(bot):
    """
    Called automatically by discord while loading extension. Adds the Miscellaneous cog on to the bot.
    """
    bot.add_cog(Misc(bot))
