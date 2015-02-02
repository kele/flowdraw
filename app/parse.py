__author__ = 'kele'

import re

class Message:
    def __init__(self, sender, receiver, type, content):
        self.sender = sender
        self.receiver = receiver
        self.type = type
        self.content = content

class FunctionEnter:
    def __init__(self, place, instance):
        self.place = place
        self.instance = instance

    def __str__(self):
        return self.place + ": " + self.instance

class FunctionLeave:
    pass

def parseEnter(line):
    place, instance = re.match("enter \| (.+) \| (.+)", line).groups()
    return FunctionEnter(place=place, instance="")

def parseLeave(line):
    return FunctionLeave()

def parseLine(line):
    if line.startswith("enter "):
        return parseEnter(line)
    elif line.startswith("leave "):
        return parseLeave(line)
    else:
        sender, receiver, type, content = re.match(r"(.+) --> (.+) \| (.+) \| (.+)", line).groups()
        return Message(sender, receiver, type, content)

