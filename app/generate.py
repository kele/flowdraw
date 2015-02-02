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

        self.call_stack = []
        contents = []
        messages = []
        msg_index = 1
        for p in parsedMsgs:
            if isinstance(p, Message):
                msg = self.generateMessage(p, msg_index)
                messages.append(msg)

                content = self.generateContent(p, msg_index)
                contents.append(content)

                msg_index += 1

            elif isinstance(p, FunctionEnter):
                self.call_stack.append(str(p))
            elif isinstance(p, FunctionLeave):
                self.call_stack.pop()

        main = self.main_template
        main = re.sub("\{\{message\.\.\.\}\}", r'\n\t'.join(messages), main)
        main = re.sub("\{\{message_content\.\.\.\}\}", r'\n\t'.join(contents), main)


        return main

    def generateContent(self, msg, index):
        out = self.msg_content_template
        out = re.sub("\{\{msg_id\}\}", str(index), out)
        out = re.sub("\{\{message_type\}\}", str(index) + ". " + msg.type, out)
        out = re.sub("\{\{message_callstack\}\}", '\n'.join(self.call_stack), out)
        out = re.sub("\{\{message_content\}\}", msg.content, out)
        return out

    def generateMessage(self, msg, index):
        out = self.msg_template
        out = re.sub("\{\{sender\}\}", msg.sender, out)
        out = re.sub("\{\{message_type\}\}", str(index) + ". " + msg.type, out)
        out = re.sub("\{\{receiver\}\}", msg.receiver, out)
        return out



