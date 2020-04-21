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
authtoken = None
logchannelid = None

# File paths
datadir = getDataDir()
confpath = datadir / "templatebot.conf"


def load():
    global prefix, name, authtoken, logchannelid
    configDict = toml.load(confpath)

    # templatebot
    if utils.hasPath(configDict, "templatebot.prefix"):
        prefix = utils.getPath(configDict, "templatebot.prefix")
    if utils.hasPath(configDict, "templatebot.name"):
        name = utils.getPath(configDict, "templatebot.name")

    # Discord
    if utils.hasPath(configDict, "discord.authtoken"):
        authtoken = utils.getPath(configDict, "discord.authtoken")

    logchannelid = utils.getPath(configDict, "discord.logchannelid")
    if logchannelid is not None:
        logchannelid = int(logchannelid)
