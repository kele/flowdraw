from app.parse import *
from app.configuration_impl import Prettifyier
from app.configuration import configuration
from operator import *
import re

class OutputGenerator:
    def __init__(self, template_folder):
        self.prettifyier = Prettifyier(configuration)

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

        parsedItems = filter(self.prettifyier.isItemOk, parsedItems)
        for p in parsedItems:
            p = self.prettifyier.prettifyItem(p)

        self.call_stack = []
        contents = []
        messages = []
        msg_index = 1

        actors = {}
        explicitActors = []
        for p in parsedItems:
            if isinstance(p, Message):
                msg = self.generateMessage(p, msg_index)
                messages.append(msg)

                content = self.generateContent(p, msg_index)
                contents.append(content)

                msg_index += 1

                if not p.sender in actors:
                    actors[p.sender] = 0
                if not p.receiver in actors:
                    actors[p.receiver] = 0

                actors[p.sender] += 1
                actors[p.receiver] += 1

            elif isinstance(p, Note):
                pass # TODO

            elif isinstance(p, FunctionEnter):
                self.call_stack.append(str(p))

            elif isinstance(p, FunctionLeave):
                self.call_stack.pop()

            elif isinstance(p, Actor):
                explicitActors.append(p.actor)

        main = self.main_template
        main = re.sub("\{\{msg\.\.\.\}\}", r'\n\t'.join(messages), main)
        main = re.sub("\{\{msg_content\.\.\.\}\}", r'\n\t'.join(contents), main)

        actorsStrings = []
        for a in explicitActors:
            actors.discard(a)
        for a in explicitActors:
            actorsStrings.append(self.generateActor(a));

        actors = actors.items()
        actors.sort(key = itemgetter(1))
        actors.reverse()
        for a in actors:
            actorsStrings.append(self.generateActor(a[0]));
        main = re.sub("\{\{actors...\}\}", r'\n\t'.join(actorsStrings), main)

        return main

    def generateActor(self, actor):
        out = self.actor_template
        out = re.sub("\{\{actor\}\}", actor, out)
        return out

    # TODO: generateContent and generateMessage seem to be the same...
    def generateContent(self, msg, index):
        out = self.msg_content_template
        out = re.sub("\{\{msg_id\}\}", str(index), out)
        out = re.sub("\{\{msg_callstack\}\}", '\n'.join(self.call_stack), out)
        out = re.sub("\{\{msg_content\}\}", msg.content, out)
        out = re.sub("\{\{msg_label\}\}", msg.label, out)
        out = re.sub("\{\{sender\}\}", msg.sender, out)
        out = re.sub("\{\{full_sender\}\}", msg.full_sender, out)
        out = re.sub("\{\{receiver\}\}", msg.receiver, out)
        out = re.sub("\{\{full_receiver\}\}", msg.full_receiver, out)
        return out

    def generateMessage(self, msg, index):
        out = self.msg_template
        out = re.sub("\{\{msg_id\}\}", str(index), out)
        out = re.sub("\{\{msg_callstack\}\}", '\n'.join(self.call_stack), out)
        out = re.sub("\{\{msg_content\}\}", msg.content, out)
        out = re.sub("\{\{msg_label\}\}", msg.label, out)
        out = re.sub("\{\{sender\}\}", msg.sender, out)
        out = re.sub("\{\{full_sender\}\}", msg.full_sender, out)
        out = re.sub("\{\{receiver\}\}", msg.receiver, out)
        out = re.sub("\{\{full_receiver\}\}", msg.full_receiver, out)
        return out

