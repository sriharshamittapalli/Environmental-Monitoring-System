from commonutils import *

def message_component(messages_list):
    messages_list[0], messages_list[1] = columns(len(messages_list))
    messages_list[0] = empty(messages_list[0])
    messages_list[1] = empty(messages_list[1])
    return messages_list[0], messages_list[1]