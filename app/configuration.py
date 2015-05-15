import re


port_mapping = { \
} 

ignored_actors = { \
}

# TODO: throw out to _impl:wq
def simplifyActor(actor):
    for regexp, new_port in port_mapping.items():
        if re.match(regexp, actor):
            return new_port
    return actor

def isMsgOk(msg):
    for regexp in ignored_actors:
        if re.match(regexp, msg.receiver):
            return False
        if re.match(regexp, msg.sender):
            return False

    return True

