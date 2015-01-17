__author__ = 'kele'

from app.parse import *
import re

class OutputGenerator:
    def __init__(self, template_folder):
        with open(template_folder + "/main.template") as main_file:
            self.main_template = ''.join(main_file.readlines())

        with open(template_folder + "/message_sequence.template") as msg_seq_file:
            self.msg_seq_template = ''.join(msg_seq_file.readlines())

        with open(template_folder + "/message.template") as msg_file:
            self.msg_template = ''.join(msg_file.readlines())

    def generate(self, inputfilename):
        messages = []

        with open(inputfilename) as file:
            for line in file:
                messages.append(parseLine(line))

        msgs_out = []
        for msg in messages:
            out = re.sub("\{\{sender\}\}", msg.sender, self.msg_template)
            out = re.sub("\{\{message_type\}\}", msg.type, out)
            out = re.sub("\{\{receiver\}\}", msg.receiver, out)
            msgs_out.append(out)


