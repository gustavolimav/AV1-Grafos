from typing import Dict
from graph import Graph
from edge import Edge
from vortex import Vortex


# Vortex: 
# 	label: str, 
# 	adjacent_edges: Dict[str: Edge]

# Edge: 
# 	label: str, 
# 	weight: float
# 	is_directed: bool
#	connected_vertices: Tuple[str, str]

def parse_csv_into_graph(file_path: str) -> Graph:
	csv = open(file_path, 'r')
	lines = csv.readlines()
	is_directed = True
	vertices = dict()
	edges = dict()
	i = 0
	for line in lines:
		# Ignore headers
		if i == 0:
			i += 1
			continue
		line = line.strip()
		values = line.split(';')
		vortex_label_1 = values[0]
		vortex_label_2 = values[1]
		edge_weight = float(values[2])
		edge_label = str(i)
		connected_vertices = (vortex_label_1, vortex_label_2)

		edge = Edge(edge_label, is_directed)
		edge.connected_vertices = connected_vertices
		edge.weight = edge_weight

		vortex_1 = Vortex(vortex_label_1)
		vortex_2 = Vortex(vortex_label_2)

		if vortex_label_1 not in vertices.keys():
			vortex_1.adjacent_edges[edge_label] = edge
			vertices[vortex_label_1] = vortex_1
		else:
			vortex = vertices[vortex_label_1]
			vortex.adjacent_edges[edge_label] = edge
		if vortex_label_2 not in vertices.keys():
			vortex_2.adjacent_edges[edge_label] = edge
			vertices[vortex_label_2] = vortex_2
		else:
			vortex = vertices[vortex_label_2]
			vortex.adjacent_edges[edge_label] = edge
		
		edges[edge_label] = edge
		i += 1

	graph = Graph(is_directed)	
	graph.vertices = vertices
	graph.edges = edges
	return graph


# Testing
# graph = parse_csv_into_graph("./planilha-aeroportos-brasil.csv")
# print(graph)