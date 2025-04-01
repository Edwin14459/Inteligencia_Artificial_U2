import networkx as nx
import matplotlib.pyplot as plt

# Crear un grafo dirigido para la red semántica
G = nx.DiGraph()

# Agregar nodos (conceptos)
nodos = ["Perro", "Mamífero", "Animal", "Cuatro patas", "Sangre caliente", "Oxígeno"]
G.add_nodes_from(nodos)

# Agregar relaciones (aristas)
relaciones = [
    ("Perro", "Mamífero", "es un"),
    ("Perro", "Cuatro patas", "tiene"),
    ("Mamífero", "Animal", "es un"),
    ("Mamífero", "Sangre caliente", "tiene"),
    ("Animal", "Oxígeno", "necesita")
]

for origen, destino, relacion in relaciones:
    G.add_edge(origen, destino, label=relacion)

# Dibujar la red semántica
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='black', node_size=3000, font_size=10)
edge_labels = {(origen, destino): relacion for origen, destino, relacion in relaciones}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
plt.title("Red Semántica Simple")
plt.show()
