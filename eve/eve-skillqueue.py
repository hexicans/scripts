#!/usr/bin/env python

import evelink.eve
import evelink.api
import time
from datetime import datetime

class getCharInfo:
    def __init__(self, charname, apikey, apicode):
        self.cn = charname
        self.apik = apikey
        self.apic = apicode

    def getRemainder(self, timestamp):
        queuetime = datetime.fromtimestamp(timestamp)
        curtime = datetime.now()
        tdiff = queuetime - curtime
        days = tdiff.days
        minutes, seconds = divmod(tdiff.seconds, 60)
        hours, minutes = divmod(minutes, 60)
        remdays = "{0} days ".format(days) if days>0 else ""
        remhours = "{0} hours ".format(hours) if hours>0 else ""
        remainder = "%s%s%s minutes" % (remdays, remhours, minutes)
        return remainder

    def getCharID(self):
        el = evelink.eve.EVE()
        result = el.character_id_from_name(self.cn)
        return result.result

    def getSkillQueue(self, charid):
        api = evelink.api.API(api_key=(self.apik, self.apic))
        char = evelink.char.Char(charid, api=api)
        try:
            queue = char.skill_queue().result[-1]["end_ts"] + 3600 # adding an hour for GMT+1
            print "Character '{0}' has a skill queue until: {1} ({2})".format(self.cn, time.strftime("%A %D %H:%M:%S", time.gmtime(queue)), self.getRemainder(queue))
        except IndexError:
            print "Character '{0}' has an empty skill queue!".format(self.cn)

api = getCharInfo("Character Name", "api key", "long api code")
charid = api.getCharID()
api.getSkillQueue(charid)

