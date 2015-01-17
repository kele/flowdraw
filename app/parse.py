__author__ = 'kele'

import re

class Message:
    def __init__(self, sender, receiver, type, content):
        self.sender = sender
        self.receiver = receiver
        self.type = type
        self.content = content

def parseLine(line):
   sender, receiver, type, content = re.match(r"(.+) --> (.+) \| (.+) \| (.+)", line, re.MULTILINE | re.DOTALL).groups()
   return Message(sender, receiver, type, content)

