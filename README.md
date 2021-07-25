# Automated Trash Can

A Discord bot that does a few things, including:
- Random games
- Pulling posts from Reddit
- Coming up with bullshit
- Making polls and generally being a nuisance in chat

Credits to [naveen-u](https://github.com/naveen-u) and his [WingBot](https://github.com/naveen-u/WingBot) for letting me steal most of his work.

## Development

If you want to run a copy of this bot locally, this is what you'll need to set up.

### Prerequisites

- python-3.8
- [A Discord token](https://discordpy.readthedocs.io/en/latest/discord.html)
- [A Reddit application's credentials](https://ssl.reddit.com/prefs/apps/)

### Installing

- Install the required packages using:

```
pip install -r requirements.txt
```

### Configuration

- Create a file named `.env` in the root directory with:

```
DISCORD_TOKEN=<your discord token>
REDDIT_CLIENT_ID=<your reddit app's client ID>
REDDIT_SECRET=<your reddit app's client secret>
```

### Deployment

Run `python bot.py` from the root directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
