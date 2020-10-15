import re
import random

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', 175)

class Utils:
    def __init__(self, logger):
        self.logger = logger

    @staticmethod
    def normalize_utterances(utterances):
        normalized = ''
        for u in utterances:
            u = re.sub('\\W+', ' ', u)
            normalized += u.lower().strip() + "|"

        return normalized[:-1]

    @staticmethod
    def match_pattern(voice_note, pattern):
        data = Utils.normalize_utterances(pattern)
        compiled = re.compile(data)
        value = compiled.search(voice_note)
        if value:
            return True
        else:
            False

    @staticmethod
    def choose_random(response):
        return random.choice(response)

    @staticmethod
    def playsound(response):
        engine.say(response)
        engine.runAndWait()
