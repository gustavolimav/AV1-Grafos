from typing import Dict
from edge import Edge
from vortex_exception import VortexException

class Vortex:
	def __init__(self, label: str):
		self.label = label
		self.adjacent_edges: Dict[str, Edge] = dict() 
	
	def add_adjacent_edge(self, edge: Edge):
		"""
		Adds an adjacent edge to vortex instance	

		Parameters:
		edge (Edge): Edge object
	
		Returns:
		None
	
		"""
		if not isinstance(edge, Edge):
			raise VortexException("'edge' must be an instance of Edge")

		self.adjacent_edges[edge.label] = edge
	
	def __repr__(self):
		adjacent_edges_list = list(self.adjacent_edges.keys())
		return f'Vortex[label: {self.label}, adjacent_edges: {adjacent_edges_list}]'




# Testing
# vortex = Vortex('1')
# edge_1 = Edge('a', True)
# edge_2 = Edge('b', True)

# vortex.add_adjacent_edge(edge_1)
# vortex.add_adjacent_edge(edge_2)
# print(vortex)