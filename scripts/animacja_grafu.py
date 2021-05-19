import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation
from diagram import diagram
from slave import slave
from konsola import Konsola


class Anim:
    def __init__(self):
        # graf
        self.graph = nx.DiGraph()

        for s in diagram['states']:
            self.graph.add_node(s.name)

        for s in slave['states']:
            self.graph.add_node(s.name)

        for t in diagram['form_to']:
            s = diagram['states'][t[0]].name
            d = diagram['states'][t[1]].name

            self.graph.add_edges_from([(s, d)])

        for t in slave['form_to']:
            s = slave['states'][t[0]].name
            d = slave['states'][t[1]].name

            self.graph.add_edges_from([(s, d)])

        # konsola
        self.con = Konsola()

        # fig
        self.fig, self.ax = plt.subplots(figsize=(50, 50))

        self.fixed_position = {
            'Ramię w pozycji I': (3, 2.5),
            'Element na linii I': (4, 3),
            'Element rozpoznany - Master': (5, 2.5),
            'Element na linii II': (6, 2),
            'Ramię w pozycji II': (2, 2),
            'Element rozpoznany - Slave': (4, 1.5),
            'Ciąg dalszy procesu': (3, 1),
            'Oczekiwanie na element': (5, 1)}

        self.options = {
            'node_size': 3000,
            'width': 2,
            'with_labels': True,
            'pos': self.fixed_position,
            'font_color': 'blue',
            'edge_color': 'grey'}

        self.graph_updated = False
        color_map = []

        for i, state in enumerate(self.fixed_position.keys()):
            if self.con.get_curr_state().name == state:
                color_map.append('pink')
            else:
                color_map.append('grey')

        nx.draw(self.graph, node_color=color_map, **self.options)

    def update(self, num):
        self.ax.clear()

        if self.graph_updated:
            self.con.print_curr_state()
            self.con.print_allowed_trans()
            choice = self.con.choose_tran()
            if choice == 'q':
                exit(1)
                plt.close()
            else:
                self.con.run_tran(choice)
            self.con.system.refresh()
            self.graph_updated = False
        else:
            self.graph_updated = True

        color_map = []

        for i, state in enumerate(self.fixed_position.keys()):
            if self.con.get_curr_state().name == state:
                color_map.append('pink')
            else:
                color_map.append('grey')

        if self.con.get_curr_state() in self.con.system.slave.states:
            color_map[2] = 'pink'

        nx.draw(self.graph, node_color=color_map, **self.options)

    def run_ani(self):
        ani = matplotlib.animation.FuncAnimation(self.fig, self.update)
        plt.show()


if __name__ == '__main__':
    anim = Anim()
    anim.run_ani()

