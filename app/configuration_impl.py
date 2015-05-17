from app.parse import *
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
        if isinstance(item, Message):
            return self._isMsgOk(item)
        else:
            return True

    def prettifyItem(self, item):
        if isinstance(item, Message):
            item.sender = self._simplifyActor(item.sender)
            item.receiver = self._simplifyActor(item.receiver)

        return item

    def _simplifyActor(self, actor):
        for regexp, new_port in self.configuration.actor_mapping.items():
            if re.match(regexp, actor):
                return new_port

        return actor

    def _isMsgOk(self, msg):
        for regexp in self.configuration.ignored_actors:
            if re.match(regexp, msg.receiver):
                return False
            if re.match(regexp, msg.sender):
                return False

        return True
