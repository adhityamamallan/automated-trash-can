import random
import asyncio

import discord
from bs4 import BeautifulSoup
from discord.ext import commands
from urllib.request import Request, urlopen

from utils.configManager import RedditConfig, BotConfig
from utils import consts, realmHelpers


class Realm(commands.Cog):
    """Various Realm-related commands."""

    def __init__(self, bot):
        self.bot = bot
        self.bot_config = BotConfig()

    async def get_info(self, ctx, name, typestr):
        site = (
            "https://www.realmeye.com/"
            + typestr
            + "/{0}".format(name.replace(" ", "%20"))
        )
        print(site)
        hdr = {"User-Agent": "Mozilla/5.0"}
        clean_name = None
        try:
            req = Request(site, headers=hdr)
            page = urlopen(req)
            soup = BeautifulSoup(page, "html.parser")
            table = soup.find("table")
            table_rows = table.find_all("tr")
            span = soup.find("span", {"class": "entity-name"})
            clean_name = span.text
        except:
            if typestr == "player":
                await ctx.send(
                    "Sorry, that player does not seem to exist. Check the spelling and try again."
                )
            elif typestr == "guild":
                await ctx.send(
                    "Sorry, that guild does not seem to exist. Check the spelling and try again.\nDo note that guild names are case-sensitive."
                )
            else:
                await ctx.send("How did you even get here tf")
            return

        info = []

        for tr in table_rows:
            td = tr.find_all("td")
            row = [i.text for i in td]
            info.append(row)

        await ctx.send(
            embed=realmHelpers.get_realmeye_embed(clean_name, typestr, site, info)
        )

    @commands.command(usage="<player name>", aliases=["realmeye", "stalk"])
    async def player(self, ctx, pname: str):
        """Stalk people's Realmeyes."""
        await self.get_info(ctx, pname, "player")

    @commands.command(usage="guild <guild name>")
    async def guild(self, ctx, *, gname: str):
        """Stalk guilds on Realmeye."""
        await self.get_info(ctx, gname, "guild")

    @commands.command(usage="<dungeon name>", aliases=["afkcheck"])
    async def afk(self, ctx, *args):
        """Start an AFK check."""

        commandmsg = await ctx.channel.fetch_message(ctx.channel.last_message_id)
        await commandmsg.delete()

        if len(args) > 0:
            dungeon = " ".join(args)
        else:
            errmsg = await ctx.send("You gotta specify the dungeon stepbro")
            await asyncio.sleep(5)
            await errmsg.delete()
            return

        afkmsg = await ctx.send(embed=realmHelpers.get_afk_embed(dungeon))

        await afkmsg.add_reaction(consts.ping)
        await afkmsg.add_reaction(consts.knight)
        await afkmsg.add_reaction(consts.warr)
        await afkmsg.add_reaction(consts.pally)
        await afkmsg.add_reaction(consts.priest)
        await afkmsg.add_reaction(consts.brain)
        await afkmsg.add_reaction(consts.slow)
        await afkmsg.add_reaction(consts.pbag)

    @commands.command(usage="<event name>", aliases=["hc"])
    async def headcount(self, ctx, *args):
        """Start a headcount."""
        commandmsg = await ctx.channel.fetch_message(ctx.channel.last_message_id)
        await commandmsg.delete()

        if len(args) > 0:
            event = " ".join(args)
        else:
            errmsg = await ctx.send(
                "You gotta specify what the headcount is for stepbro"
            )
            await asyncio.sleep(5)
            await errmsg.delete()
            return

        hcmsg = await ctx.send(embed=realmHelpers.get_headcount_embed)

        await hcmsg.add_reaction(consts.ping)
        await hcmsg.add_reaction(consts.pbag)


def setup(bot):
    """
    Called automatically by discord while loading extension. Adds the Realm cog on to the bot.
    """
    bot.add_cog(Realm(bot))
