__author__ = 'kele'

from app.parse import *
import configuration
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

        with open(template_folder + "/actor.template") as file:
            self.actor_template = ''.join(file.readlines())

    def generate(self, inputfilename):
        with open(inputfilename) as file:
            parsedItems = [parseLine(line) for line in file]

        for p in parsedItems:
            if isinstance(p, Message):
                p.sender = configuration.simplifyActor(p.sender)
                p.receiver = configuration.simplifyActor(p.receiver)

        parsedItems = filter(configuration.isMsgOk, parsedItems)

        self.call_stack = []
        contents = []
        messages = []
        msg_index = 1

        actors = set()
        explicitActors = []
        for p in parsedItems:
            if isinstance(p, Message):
                msg = self.generateMessage(p, msg_index)
                messages.append(msg)

                content = self.generateContent(p, msg_index)
                contents.append(content)

                msg_index += 1

                actors.add(p.sender)
                actors.add(p.receiver)

            elif isinstance(p, Note):
                messages.append(p.content)

            elif isinstance(p, FunctionEnter):
                self.call_stack.append(str(p))

            elif isinstance(p, FunctionLeave):
                self.call_stack.pop()

            elif isinstance(p, Actor):
                explicitActors.append(p.actor)

        main = self.main_template
        main = re.sub("\{\{message\.\.\.\}\}", r'\n\t'.join(messages), main)
        main = re.sub("\{\{message_content\.\.\.\}\}", r'\n\t'.join(contents), main)

        actorsStrings = []
        for a in explicitActors:
            actors.discard(a)
        for a in explicitActors:
            actorsStrings.append(self.generateActor(a));
        for a in actors:
            actorsStrings.append(self.generateActor(a));
        main = re.sub("\{\{actors...\}\}", r'\n\t'.join(actorsStrings), main)

        return main

    def generateActor(self, actor):
        out = self.actor_template
        out = re.sub("\{\{actor\}\}", actor, out)
        return out

    def generateContent(self, msg, index):
        out = self.msg_content_template
        out = re.sub("\{\{msg_id\}\}", str(index), out)
        out = re.sub("\{\{message_header\}\}", "%d. %s [%s -> %s]" % (index, msg.type, msg.sender, msg.receiver), out)
        out = re.sub("\{\{message_callstack\}\}", '\n'.join(self.call_stack), out)
        out = re.sub("\{\{message_content\}\}", msg.content, out)
        return out

    def generateMessage(self, msg, index):
        out = self.msg_template
        out = re.sub("\{\{sender\}\}", msg.sender, out)
        out = re.sub("\{\{msg_id\}\}", str(index), out)
        out = re.sub("\{\{message_type\}\}", msg.type, out)
        out = re.sub("\{\{receiver\}\}", msg.receiver, out)
        return out

