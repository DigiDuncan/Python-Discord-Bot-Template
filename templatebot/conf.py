from pathlib import Path

import appdirs
import toml

from templatebot.lib import utils


def getDataDir():
    appname = "TemplateBot"
    appauthor = "DigiDuncan"
    datadir = Path(appdirs.user_data_dir(appname, appauthor))
    return datadir


description = "This is a template. Replace this!"
prefix = "!"
name = "TemplateBot"
activity = "TemplateBot"
authtoken = None
admins = []             # List of admins # TODO: (deprecated?)
logchannelid = None

# File paths
datadir = getDataDir()
confpath = datadir / "sizebot.conf"


def load():
    global prefix, name, activity, authtoken, admins, logchannelid
    configDict = toml.load(confpath)

    # SizeBot
    if utils.hasPath(configDict, "sizebot.prefix"):
        prefix = utils.getPath(configDict, "sizebot.prefix")
    if utils.hasPath(configDict, "sizebot.name"):
        name = utils.getPath(configDict, "sizebot.name")
    if utils.hasPath(configDict, "sizebot.activity"):
        activity = utils.getPath(configDict, "sizebot.activity")

    # Discord
    if utils.hasPath(configDict, "discord.authtoken"):
        authtoken = utils.getPath(configDict, "discord.authtoken")
    if utils.hasPath(configDict, "discord.admins"):
        admins = utils.getPath(configDict, "discord.admins")

    logchannelid = utils.getPath(configDict, "discord.logchannelid")
    if logchannelid is not None:
        logchannelid = int(logchannelid)
