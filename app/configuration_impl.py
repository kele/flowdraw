import re

class Configuration:
    def __init__(self):
        self.actor_mapping = {}
        self.ignored_actors = {}
        self.ignored_messages = {}


class Prettifyier:
    def __init__(self, configuration):
        self.configuration = configuration

    def isItemOk(self, item):
        return True

    def prettifyItem(self, item):
        return item

    def _simplifyActor(actor):
        for regexp, new_port in port_mapping.items():
            if re.match(regexp, actor):
                return new_port
        return actor

    def _isMsgOk(msg):
        for regexp in ignored_actors:
            if re.match(regexp, msg.receiver):
                return False
            if re.match(regexp, msg.sender):
                return False

        return True
