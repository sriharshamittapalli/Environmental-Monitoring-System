# Implemented all important functions in commonutils.
from commonutils import *

def graph_component(graphs_list, tab):
    if graphs_list:
        if graphs_list[0]:
            if graphs_list[1]:
                if tab:
                    graphs_list[0], graphs_list[1] = columns(len(graphs_list), tab)
                    graphs_list[0] = empty(graphs_list[0])
                    graphs_list[1] = empty(graphs_list[1])
    return graphs_list[0], graphs_list[1]
