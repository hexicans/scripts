#!/usr/bin/env python

import evelink.eve
import evelink.api
import time

class getCharInfo:
    def __init__(self, charname, apikey, apicode):
        self.cn = charname
        self.apik = apikey
        self.apic = apicode

    def getCharID(self):
        el = evelink.eve.EVE()
        result = el.character_id_from_name(self.cn)
        return result.result

    def getSkillQueue(self, charid):
        api = evelink.api.API(api_key=(self.apik, self.apic))
        char = evelink.char.Char(charid, api=api)
        try:
            print "Character '%s' has a skill queue until:" % self.cn, time.strftime("%A %D %H:%M:%S", time.gmtime(char.skill_queue().result[-1]["end_ts"] + 3600))
        except:
            print "Character '%s' has an empty skill queue!" % self.cn

api = getCharInfo("Character Name", 123456, "long api code")
charid = api.getCharID()
api.getSkillQueue(charid)
