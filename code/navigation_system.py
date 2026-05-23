"""
Indoor navigation system based on graph algorithms.

The hospital map is modeled as a weighted graph and
the shortest path is computed using Dijkstra algorithm.
"""

import networkx as nx

hospital_graph = nx.Graph()

# Example connections
hospital_graph.add_edge("Entrance", "Radiology", weight=4)
hospital_graph.add_edge("Radiology", "Cardiology", weight=2)

# Compute shortest path
path = nx.shortest_path(
    hospital_graph,
    source="Entrance",
    target="Cardiology",
    weight="weight"
)

print("Navigation Path:", path)
