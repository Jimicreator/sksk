import html
import random
import time
from typing import List

from telegram import Bot, Update, ParseMode
from telegram.ext import run_async

from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler
from tg_bot.modules.helper_funcs.chat_status import is_user_admin, user_admin
from tg_bot.modules.helper_funcs.extraction import extract_user

#sleep how many times after each edit in 'police' 
EDIT_SLEEP = 1
#edit how many times in 'police' 
EDIT_TIMES = 3

police_siren = [
            "š“š“š“ā¬ļøā¬ļøā¬ļøšµšµšµ\nš“š“š“ā¬ļøā¬ļøā¬ļøšµšµšµ\nš“š“š“ā¬ļøā¬ļøā¬ļøšµšµšµ",
            "šµšµšµā¬ļøā¬ļøā¬ļøš“š“š“\nšµšµšµā¬ļøā¬ļøā¬ļøš“š“š“\nšµšµšµā¬ļøā¬ļøā¬ļøš“š“š“"
]



@user_admin
@run_async
def police(bot: Bot, update: Update):
    msg = update.effective_message.reply_text('Police is coming!') 
    for x in range(EDIT_TIMES):
        msg.edit_text(police_siren[x%2])
        time.sleep(EDIT_SLEEP)
    msg.edit_text('Police is here!')


__help__ = """
Specially Thanks To @SaitamaRobot For This Modules
- /police : š
"""

POLICE_HANDLER = DisableAbleCommandHandler("police", police)


dispatcher.add_handler(POLICE_HANDLER)

__mod_name__ = "POLICE"
__command_list__ = ["police"]
__handlers__ = [POLICE_HANDLER]
