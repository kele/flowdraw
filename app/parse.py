__author__ = 'kele'

import re

class Message:
    def __init__(self, sender, receiver, label, content):
        self.sender = sender
        self.receiver = receiver
        self.label = label 
        self.content = content
        self.full_receiver = receiver
        self.full_sender = sender

class Note:
    def __init__(self, content):
        self.content = content

class FunctionEnter:
    def __init__(self, place, instance):
        self.place = place
        self.instance = instance

    def __str__(self):
        return self.place + ": " + self.instance

class Actor:
    def __init__(self, actor):
        self.actor = actor

class FunctionLeave:
    pass

def parseEnter(line):
    place, instance = re.match("enter \| (.+) \| (.+)", line).groups()
    return FunctionEnter(place=place, instance="")

def parseLeave(line):
    return FunctionLeave()

def parseNote(line):
    return Note(line)

def parseActor(line):
    actor = re.match("actor (.+)", line).groups()
    return Actor(actor)

def parseLine(line):
    if line.startswith("enter "):
        return parseEnter(line)
    elif line.startswith("leave "):
        return parseLeave(line)
    elif line.startswith("note over "):
        return parseNote(line)
    elif line.startswith("actor "):
        return parseActor(line)
    else:
        sender, receiver, type, content = re.match(r"(.+) --> (.+) \| (.+) \| (.+)", line).groups()
        return Message(sender, receiver, type, content)

