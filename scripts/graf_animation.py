import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation
from diagram import diagram
from slave import slave
from console import ConsoleControl

#graf
graph = nx.DiGraph()

fixed_position = {
    'Ramię w pozycji I': (3, 2.5),
    'Element na linii I': (4, 3),
    'Element rozpoznany - Master': (5, 2.5),
    'Element na linii II': (6, 2),
    'Ramię w pozycji II': (2, 2),
    'Element rozpoznany - Slave': (4, 1.5),
    'Ciąg dalszy procesu': (3, 1),
    'Oczekiwanie na element': (5, 1)}

opt = {
    'node_size': 3000,
    'width': 2,
    'with_labels': True,
    'pos': fixed_position,
    'font_color': 'blue',
    'edge_color': 'grey'}

for s in diagram['states']:
    graph.add_node(s.name)

for s in slave['states']:
    graph.add_node(s.name)

for t in diagram['form_to']:
    s = diagram['states'][t[0]].name
    d = diagram['states'][t[1]].name

    graph.add_edges_from([(s, d)])

for t in slave['form_to']:
    s = slave['states'][t[0]].name
    d = slave['states'][t[1]].name

    graph.add_edges_from([(s, d)])

fig, ax = plt.subplots(figsize=(50, 50))

#consola
con = ConsoleControl()
graph_updated = False

def update(num):
    ax.clear()
    global graph_updated

    if graph_updated:
        con.print_curr_state()
        con.print_allowed_trans()
        choice = con.choose_tran()
        if choice == 'q':
            exit(1)
            plt.close()
        else:
            con.run_tran(choice)
        con.system.refresh()
        graph_updated = False
    else:
        graph_updated = True

    color_map = []

    for i, state in enumerate(fixed_position.keys()):
        if con.get_curr_state().name == state:
            color_map.append('pink')
        else:
            color_map.append('grey')

    if con.get_curr_state() in con.system.slave.states:
        color_map[2] = 'pink'

    nx.draw(graph, node_color=color_map, **opt)

def init():
    color_map = []

    for i, state in enumerate(fixed_position.keys()):
        if con.get_curr_state().name == state:
            color_map.append('pink')
        else:
            color_map.append('grey')

    if con.get_curr_state() in con.system.slave.states:
        color_map[2] = 'pink'
    nx.draw(graph, node_color=color_map, **opt)

if __name__ == '__main__':
    init()
    ani = matplotlib.animation.FuncAnimation(fig, update)
    plt.show()
