import networkx as nx
import matplotlib.pyplot as plt


class GrafoVisual:
    def __init__(self, grafo):
        self.grafo = grafo
        self.G = nx.DiGraph()

        for vertice, arestas in grafo.items():
            for vizinho, peso in arestas.items():
                self.G.add_edge(vertice, vizinho, weight=peso)

    def mostrar_grafo(self, caminho):
        pos = nx.spring_layout(self.G)
        edge_labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw(self.G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=10, font_weight='bold')
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=edge_labels)

        if caminho:
            path_edges = list(zip(caminho, caminho[1:]))
            nx.draw_networkx_edges(self.G, pos, edgelist=path_edges, edge_color='r', width=2)

        plt.show()