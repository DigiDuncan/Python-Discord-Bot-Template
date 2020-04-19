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
confpath = datadir / "templatebot.conf"


def load():
    global prefix, name, activity, authtoken, admins, logchannelid
    configDict = toml.load(confpath)

    # templatebot
    if utils.hasPath(configDict, "templatebot.prefix"):
        prefix = utils.getPath(configDict, "templatebot.prefix")
    if utils.hasPath(configDict, "templatebot.name"):
        name = utils.getPath(configDict, "templatebot.name")
    if utils.hasPath(configDict, "templatebot.activity"):
        activity = utils.getPath(configDict, "templatebot.activity")

    # Discord
    if utils.hasPath(configDict, "discord.authtoken"):
        authtoken = utils.getPath(configDict, "discord.authtoken")
    if utils.hasPath(configDict, "discord.admins"):
        admins = utils.getPath(configDict, "discord.admins")

    logchannelid = utils.getPath(configDict, "discord.logchannelid")
    if logchannelid is not None:
        logchannelid = int(logchannelid)
