#  This file is part of the VIDEOconvertor distribution.
#  Copyright (c) 2021 vasusen-code ; All rights reserved. 
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, version 3.
#
#  This program is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#  General Public License for more details.
#
#  License can be found in < https://github.com/vasusen-code/VIDEOconvertor/blob/public/LICENSE> .
#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in 



from helper._get import *

LOGS.info("Starting...")


BOT_TOKEN ="5509916510:AAG2fow3mScpTf3VzMnDzAGO99nPZnYLIxw"
API_HASH ="74a2665339484da3eaaed5f4fe16da79"
APP_ID = 14560088
LOG_CHANNEL = "-1001715617029"

######## Connect ########


try:
    cbot = TelegramClient("bot", APP_ID, API_HASH).start(bot_token=BOT_TOKEN)
except Exception as e:
    LOGS.info("Environment vars are missing! Kindly recheck.")
    LOGS.info("Bot is quiting...")
    LOGS.info(str(e))
    exit()


####### GENERAL CMDS ########


@cbot.on(events.NewMessage(pattern="/start"))
async def _(e):
    await start(e)


@cbot.on(events.NewMessage(pattern="/ping"))
async def _(e):
    await up(e)


@cbot.on(events.NewMessage(pattern="/help"))
async def _(e):
    await help(e)


######## Callbacks #########


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"sshot(.*)")))
async def _(e):
    await screenshot(e)


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"gsmpl(.*)")))
async def _(e):
    await sample(e)


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"skip(.*)")))
async def _(e):
    await skip(e)


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"stats(.*)")))
async def _(e):
    await stats(e)


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"encc(.*)")))
async def _(e):
    await encc(e)


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"sencc(.*)")))
async def _(e):
    await sencc(e)


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"ccom(.*)")))
async def _(e):
    await ccom(e)


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"back(.*)")))
async def _(e):
    await back(e)


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile("ihelp")))
async def _(e):
    await ihelp(e)


@cbot.on(events.callbackquery.CallbackQuery(data=re.compile("beck")))
async def _(e):
    await beck(e)


########## Direct ###########


@cbot.on(events.NewMessage(pattern="/eval"))
async def _(e):
    await eval(e)


@cbot.on(events.NewMessage(pattern="/bash"))
async def _(e):
    await bash(e)


########## AUTO ###########


@cbot.on(events.NewMessage(incoming=True))
async def _(e):
    await encod(e)


########### Start ############

LOGS.info("Bot has started.")
cbot.run_until_disconnected()



#  This file is part of the VIDEOconvertor distribution.
#  Copyright (c) 2021 vasusen-code ; All rights reserved. 
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, version 3.
#
#  This program is distributed in the hope that it will be useful, but
#  WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#  General Public License for more details.
#
#  License can be found in < https://github.com/vasusen-code/VIDEOconvertor/blob/public/LICENSE> .
#    This file is part of the Compressor distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
#    License can be found in 
