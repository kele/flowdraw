__author__ = 'kele'

from app.parse import *
import re

class OutputGenerator:
    def __init__(self, template_folder):
        # TODO: find a better way to do this
        with open(template_folder + "/main.template") as file:
            self.main_template = ''.join(file.readlines())

        with open(template_folder + "/message.template") as file:
            self.msg_template = ''.join(file.readlines())

        with open(template_folder + "/message_content.template") as file:
            self.msg_content_template = ''.join(file.readlines())

    def generate(self, inputfilename):
        with open(inputfilename) as file:
            parsedMsgs = [parseLine(line) for line in file]

        messages = [self.generateMessage(msg, index + 1) for index, msg in enumerate(parsedMsgs)]
        contents = [self.generateContent(msg, index + 1) for index, msg in enumerate(parsedMsgs)]

        main = self.main_template
        main = re.sub("\{\{message\.\.\.\}\}", r'\n\t'.join(messages), main)
        main = re.sub("\{\{message_content\.\.\.\}\}", r'\n\t'.join(contents), main)


        return main

    def generateContent(self, msg, index):
        out = self.msg_content_template
        out = re.sub("\{\{msg_id\}\}", str(index), out)
        out = re.sub("\{\{message_type\}\}", str(index) + ". " + msg.type, out)
        out = re.sub("\{\{message_content\}\}", msg.content, out)
        return out

    def generateMessage(self, msg, index):
        out = self.msg_template
        out = re.sub("\{\{sender\}\}", msg.sender, out)
        out = re.sub("\{\{message_type\}\}", str(index) + ". " + msg.type, out)
        out = re.sub("\{\{receiver\}\}", msg.receiver, out)
        return out



