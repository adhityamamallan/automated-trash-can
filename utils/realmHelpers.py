import discord
from utils import consts


def get_dungeon_color(dungeon):
    dungeoncolor = discord.Color.blue()

    dungeon_lower = dungeon.lower()

    if dungeon_lower == "lost halls" or dungeon_lower == "mbc":
        dungeoncolor = discord.Color.lighter_grey()
    elif dungeon_lower == "thicket" or dungeon_lower == "secluded thicket":
        dungeoncolor = discord.Color.dark_green()
    elif dungeon_lower == "fungal cavern" or dungeon_lower == "fungal":
        dungeoncolor = discord.Color.dark_purple()
    elif (
        dungeon_lower == "void"
        or dungeon_lower == "fullskip void"
        or dungeon_lower == "voivoi"
        or dungeon_lower == "lost halls void"
    ):
        dungeoncolor = discord.Color.from_rgb(0, 0, 128)
    elif dungeon_lower == "cult" or dungeon_lower == "cultist hideout":
        dungeoncolor = discord.Color.from_rgb(230, 0, 0)
    elif dungeon_lower == "shatters" or dungeon_lower == "shatts":
        dungeoncolor = discord.Color.darker_grey()

    return dungeoncolor


def get_afk_embed(dungeon):
    return discord.Embed(
        title="A {0} run is starting soon!".format(dungeon),
        description="React to:\n"
        + "• {0} if you want to join\n".format(consts.ping)
        + "• Any classes/abilities you are going to bring\n"
        + "• {0} if you want to rush/have a brain\n".format(consts.brain)
        + "• {0} for good luck".format(consts.pbag),
        color=get_dungeon_color(dungeon),
    )


def get_headcount_embed(event):
    return discord.Embed(
        title="Headcount for {0}".format(event),
        description="React to:\n"
        + "• {0} if you want to join\n".format(consts.ping)
        + "• {0} for good luck".format(consts.pbag),
        color=discord.Color.blurple(),
    )


def get_realmeye_embed(name, type, link, info):
    embed = discord.Embed(title="Realmeye of " + type + " {0}".format(name), url=link)

    for row in info:
        embed.add_field(name=row[0], value=row[1], inline=False)

    return embed
