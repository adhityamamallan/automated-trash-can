import random

import discord
from numpy import base_repr
from utils import consts


def uwufy(message):
    message = message.replace("L", "W")
    message = message.replace("R", "W")
    message = message.replace("l", "w")
    message = message.replace("r", "w")
    message = message.replace("no", "nyo")
    message = message.replace("mo", "myo")
    message = message.replace("No", "Nyo")
    message = message.replace("Mo", "Myo")
    message = message.replace("na", "nya")
    message = message.replace("ni", "nyi")
    message = message.replace("nu", "nyu")
    message = message.replace("ne", "nye")
    message = message.replace("anye", "ane")
    message = message.replace("inye", "ine")
    message = message.replace("onye", "one")
    message = message.replace("unye", "une")
    if message.endswith("."):
        message = message[:-1]
        message += ", uwu!"
    elif message.endswith("?"):
        message = message[:-1]
        message += ", uwu?"
    elif message.endswith("!"):
        message = message[:-1]
        message += ", uwu, senpai!"
    else:
        message += " uwu"
    return message


def hmmstring():
    hmstring = "H"
    hmlength = random.randint(15, 25)
    for _ in range(0, hmlength):
        flag = random.randint(0, 2)
        if flag:
            hmstring += "M"
        else:
            hmstring += "m"
    hmstring += "m"
    return hmstring


def get_giveaway_props(embed):
    props = embed.title.split(" is giving away ")
    return props[0], props[1]


def get_giveaway_embed(user, item):
    return discord.Embed(
        title="{0} is giving away {1}!".format(user, item),
        description="React with {0} to enter!".format(consts.pbag),
        color=discord.Color.from_rgb(230, 0, 0),
    )


def get_giveaway_winner_embed(winner, sponsor, prize, msg_id):
    embed = discord.Embed(
        title="This giveaway by {0} has ended!".format(sponsor),
        description="Congratulations to {0} for winning {1}".format(
            winner.mention, prize
        ),
        color=discord.Color.from_rgb(230, 0, 0),
    )

    embed.set_footer(text="This was giveaway ID {0}".format(base_repr(msg_id, 36)))

    return embed
