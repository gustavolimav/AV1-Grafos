from graph import Graph
from graph_file_mapper import GraphFileMapper
from graph_exception import GraphException
from os import system, name
from application_headers import main_header, subheader, group_name_header
from graph_file_mapper_exception import GraphFileMapperException
from text_file_import_requirements import requirements
from csv_importer import parse_csv_into_graph

class Menu:

	def __init__(self):
		self.graph = None
		self._graph_file_mapper = None


	def show_main_menu(self):
		menu_options = {
			'1': self._show_add_vertices_menu, 
			'2': self._show_add_edges_menu,
			'3': self._show_graph_information_menu,
			'4': self._show_import_graph_menu,
			'5': self._show_import_from_csv_menu,
		}

		run = True
		while run:
			self._clear_and_apply_headers()
			print("** MENU PRINCIPAL **")
			print("Entre com a opção desejada [digite 'sair' terminar o programa]")
			print("1) Adicionar vértices")
			print("2) Adicionar arestas")
			print("3) Ir para o Menu de Informações do Grafo.")
			print("4) Importar grafo a partir das informações de um arquivo")
			print("5) [Requisito Surpresa] Importar grafo a partir do CSV de Aeroportos do Brasil")
			option = input(">>> ")

			if option == "sair":
				break

			if option not in menu_options.keys(): 
				print("⚠️ OPÇÃO INVÁLIDA. TENTE NOVAMENTE.️ ⚠")
				input("Entre com qualquer tecla para continuar... ")
				continue

			menu_options[option]()
	
	
	def _show_create_graph_instance_menu(self):
		run = True
		while run:
			self._clear_and_apply_headers()
			print("** MENU DE CRIAÇÃO DA INSTÂNCIA DO GRAFO **")
			print("Entre com o número da opção p/ dizer se o grafo é direcionado ou não-direcionado:")
			print("1) Grafo direcionado")
			print("2) Grafo não-direcionado")

			option = input(">>> ")
			if option != '1' and option != '2':
				print('⚠️ OPÇÃO INVÁLIDA. TENTE NOVAMENTE ⚠')
				input("Entre com qualquer tecla para continuar... ")
				continue
			
			is_directed = False
			if option == '1':
				is_directed = True

			self.graph = Graph(is_directed)
			print("Grafo criado com sucesso! \U0001F60A")
			input("Entre com qualquer tecla para ser encaminhado(a) ao Menu de Adição de Vértices... ")
			run = False

		self._show_add_vertices_menu()


	def _show_add_vertices_menu(self):
		self._clear_and_apply_headers()

		if self.graph is None:
			print("⚠ O grafo precisa ser criado antes da adição dos vértices. ⚠")
			input("Entre com qualquer tecla para ser encaminhado(a) ao Menu de Criação da Instância do Grafo... ")
			self._show_create_graph_instance_menu()
		else:
			run = True
			while run:
				self._clear_and_apply_headers()
				print("** MENU DE ADIÇÃO DE VÉRTICES **")
				label = input("Entre c/ a label do vértice [digite 'sair' p/ voltar ao Menu Inicial] >>> ")

				if label.lower().strip() == 'sair':
					break

				try:
					self.graph.add_vortex(label)
				except GraphException as e:
					print("⚠ Erro ao adicionar vértice " + str(e))
					input("Entre com qualquer tecla para continuar...")
					continue
				print(f"Vértice de label '{label}' adicionado com sucesso! \U0001F60A")
				print(f"Vértices existentes: {list(self.graph.vertices.keys())}")
				input("Entre com qualquer tecla para continuar adicionando vértices... ")
				

	def _show_add_edges_menu(self):
		self._clear_and_apply_headers()
		num_of_vertices = 0 if self.graph is None else len(self.graph.vertices)
		existent_vertices = [] if self.graph is None else list(self.graph.vertices.keys())

		if self.graph is None or len(self.graph.vertices) < 2:
			print("⚠ O grafo precisa ter pelo menos dois vértices para que uma aresta possa ser inserida. ⚠")
			print(f"⚠ Quantidade de vértices atual: {num_of_vertices}. ⚠")
			input("Entre com qualquer tecla para voltar ao Menu Principal... ")
		else:
			run = True
			while run:
				self._clear_and_apply_headers()
				print("** MENU DE ADIÇÃO DE ARESTAS **")
				label = input("Entre c/ a label da aresta [digite 'sair' p/ concluir] >>> ")

				if label.lower().strip() == 'sair':
					break

				weight = input("Entre com o peso da aresta [Caso não tenha peso, inserir 0] >>> ")

				connected_vertices = None
				if self.graph.is_directed:
					starting_vortex = input(f"Entre c/ a label do vértice de onde a aresta '{label}' sai (vértices existentes: {existent_vertices}) >>> ")
					arrival_vortex = input(f"Entre c/ a label do vértice de onde a aresta '{label}' chega (vértices existentes: {existent_vertices})  >>> ")
					connected_vertices = starting_vortex, arrival_vortex
				else:
					vortex_1 = input(f"Entre c/ a label do primeiro vértice que está conectado a essa aresta (vértices existentes: {existent_vertices}) >>> ")
					vortex_2 = input(f"Entre c/ a label do segundo vértice que está conectado a essa aresta (vértices existentes: {existent_vertices}) >>> ")
					connected_vertices = {vortex_1, vortex_2} 

				try:
					self.graph.add_edge(label, connected_vertices, weight)
				except GraphException as e:
					print("⚠ Erro ao adicionar aresta: " + str(e) + " Tente novamente. ⚠")
					input("Entre com qualquer tecla para continuar...")
					continue

				print(f"Vértice '{label}' inserido com sucesso! \U0001F60A")
				input("Entre com qualquer tecla para continuar adicionando arestas... ")


	def _show_graph_information_menu(self):
		self._clear_and_apply_headers()
		if self.graph is None:
			print("⚠ O grafo ainda não foi inicializado. P/ visualizar informações, crie o grafo e então tente novamente. ⚠")
			input("Entre com qualquer tecla para voltar ao Menu Principal... ")
		else:
			run = True
			while run:
				self._clear_and_apply_headers()
				print("** MENU DE INFORMAÇÕES DO GRAFO **")
				print("Entre com a opção desejada [digite 'sair' para voltar ao Menu Principal]")
				print("1) Ver o grau de um vértice")
				print("2) Ver o menor caminho entre dois vértices")
				print("3) Ver lista de vértices adjacentes de um vértice")
				print("4) Ver se dois vértices são adjacentes ")
				print("5) Visualizar grafo")
				print("6) [Requisito Surpresa] Ver se vértice é pendente")
				print("7) Ver a ordem do grafo")
				print("8) Ver tamanho do grafo")
				option = input(">>> ")
				valid_options = {'1', '2', '3', '4', '5', '6', '7', '8'}

				if option == "sair":
					break
				if option not in valid_options:
					print('⚠️ OPÇÃO INVÁLIDA. TENTE NOVAMENTE ⚠')
					input("Entre com qualquer tecla para continuar... ")
					continue
				
				if option == '1':
					vortex_label = input("Entre com a label do vértice desejado: ")
					try:
						vortex_degree = self.graph.get_vortex_degree(vortex_label)
					except GraphException as ge:
						print("⚠ Erro ao buscar o grau do vértice: " + str(ge) + " ⚠")
						input("Entre com qualquer tecla para continuar... ")
						continue
					if self.graph.is_directed:
						in_degree, out_degree = vortex_degree
						print(f"Grau de entrada do vértice '{vortex_label}': {in_degree}")
						print(f"Grau de saída do vértice '{vortex_label}': {out_degree}")
					else:
						print(f"Grau do vértice '{vortex_label}': {vortex_degree}")
					input("Entre com qualquer tecla para voltar ao Menu de Informações do Grafo... ")

				elif option == '2':
					start_label = input("Entre com a label do vértice de origem: ")
					end_label = input("Entre com a label do vértice de destino: ")
					try:
						path_list, shortest_path_cost = self.graph.get_shortest_path(start_label, end_label)
						path_string = self._convert_path_list_into_string(path_list) if path_list else f"Não há caminho possível partindo de '{start_label}' e chegando em '{end_label}'"
						shortest_path_cost = "infinito" if str(shortest_path_cost) == str(float("inf")) else shortest_path_cost
						print(f"Menor caminho: {path_string}")
						print(f"Custo do menor caminho: {shortest_path_cost}")
						input("Entre com qualquer tecla para voltar ao Menu de Informações do Grafo... ")
					except GraphException as ge:
						print("⚠ Erro ao buscar o menor caminho entre os vértices: " + str(ge) + " ⚠")
						input("Entre com qualquer tecla para continuar... ")

				elif option == '3':
					vortex_label = input("Entre com a label do vértice: ")
					try:
						adjacent_vertices = self.graph.get_adjacent_vertices(vortex_label)
						mensagem = f"Não há vértices adjacentes à '{vortex_label}'" if not adjacent_vertices else f"Lista de vértices adjacentes: {adjacent_vertices}"
						print(mensagem)
						input("Entre com qualquer tecla para voltar ao Menu de Informações do Grafo... ")
					except GraphException as ge:
						print("⚠ Erro ao buscar list de vértices adjacentes: " + str(ge) + " ⚠")
						input("Entre com qualquer tecla para continuar... ")

				elif option == '4':
					vortex_label_1 = input("Entre com a label do primeiro vértice: ")
					vortex_label_2 = input("Entre com a label do segundo vértice: ")
					try:
						are_vertices_adjacent = self.graph.are_vertices_adjacent(vortex_label_1, vortex_label_2)
						mensagem = f"Vértices '{vortex_label_1}' e '{vortex_label_2}' são adjacentes." if are_vertices_adjacent else f"Vértices '{vortex_label_1}' e '{vortex_label_2}' não são adjacentes."
						print(mensagem)
						input("Entre com qualquer tecla para voltar ao Menu de Informações do Grafo... ")
					except GraphException as ge:
						print("⚠ Erro ao ver se vértices são adjacentes: " + str(ge) + " ⚠")
						input("Entre com qualquer tecla para continuar... ")
				
				elif option == '5':
					print(self.graph)
					input("Entre com qualquer tecla para voltar ao Menu de Informações do Grafo... ")

				elif option == '6':
					vortex_label = input("Entre com a label do vértice desejado: ")
					try:
						vortex_degree = self.graph.get_vortex_degree(vortex_label)
					except GraphException as ge:
						print("⚠ Erro ao buscar o grau do vértice: " + str(ge) + " ⚠")
						input("Entre com qualquer tecla para continuar... ")
						continue
					if self.graph.is_directed:
						in_degree, out_degree = vortex_degree
						message = f"O vértice '{vortex_label}' é pendente" if in_degree + out_degree == 1 else f"O vértice '{vortex_label}' não é pendente"
						print(message)
					else:
						message = f"O vértice '{vortex_label}' é pendente" if vortex_degree == 1 else f"O vértice '{vortex_label}' não é pendente"
						print(message)
					input("Entre com qualquer tecla para voltar ao Menu de Informações do Grafo... ")

				elif option == '7':
					try:
						graph_order = self.graph.get_graph_order()
					except GraphException as ge:
						print("⚠ Erro ao buscar o ordem do grafo: " + str(ge) + " ⚠")
						input("Entre com qualquer tecla para continuar... ")
						continue
					except Exception as e:
						print("⚠ Erro ao buscar o ordem do grafo: " + str(ge) + " ⚠")
						input("Entre com qualquer tecla para continuar... ")
						continue
					print(f"Ordem do grafo: {graph_order}")
					input("Entre com qualquer tecla para voltar ao Menu de Informações do Grafo... ")

				elif option == '8':
					try:
						graph_size = self.graph.get_graph_size()
					except GraphException as ge:
						print("⚠ Erro ao buscar o tamanho do grafo: " + str(ge) + " ⚠")
						input("Entre com qualquer tecla para continuar... ")
						continue
					except Exception as e:
						print("⚠ Erro ao buscar o tamanho do grafo: " + str(ge) + " ⚠")
						input("Entre com qualquer tecla para continuar... ")
						continue
					print(f"O tamanho do grafo é: {graph_size}")
					input("Entre com qualquer tecla para voltar ao Menu de Informações do Grafo... ")
					pass



	def _show_import_graph_menu(self):
		run = True
		while run:
			self._clear_and_apply_headers()
			print("** MENU DE IMPORTAÇÃO DO GRAFO **")
			print("Entre com a opção desejada [digite 'sair' para voltar ao Menu Principal]")
			print("1) Importar grafo a partir de arquivo de texto")
			print("2) Ver informações sobre requisitos os para o arquivo de texto")
			option = input(">>> ")

			if option.lower() == "sair":
				break
			if option != '1' and option != '2':
				print('⚠️ OPÇÃO INVÁLIDA. TENTE NOVAMENTE ⚠')
				input("Entre com qualquer tecla para continuar... ")
				continue

			if option == "1": 
				self._clear_and_apply_headers()
				file_path = input("Entre com o path absoluto do arquivo de texto a ser importado: ")
				file_path = file_path.strip()
				self._graph_file_mapper = GraphFileMapper(file_path)
				try:
					graph_values = self._graph_file_mapper.get_graph_values()
					print("Informações importadas com sucesso! \U0001F60A")
					graph = self._convert_file_info_into_graph(graph_values)
					if graph:
						self.graph = graph
						print(f"Grafo gerado a partir de arquivo '{file_path}'! \U0001F60A")
					else:
						print("Não foi possível gerar o grafo a partir do arquivo. Certifique-se que as informações do arquivo estão corretas e tente novamente.")
					input("Entre com qualquer tecla para continuar... ")
				except GraphFileMapperException as gfme:
					print("⚠ Erro ao buscar informações do grafo pelo arquivo: " + str(gfme) + " ⚠")
					input("Entre com qualquer tecla para continuar... ")
					continue
				except Exception as e:
					print("⚠ General Error: " + str(e) + " ⚠")
					input("Entre com qualquer tecla para continuar... ")
					continue

			if option == "2":
				self._clear_and_apply_headers()
				print("Entre com qualquer concluir a visualização dos requisitos...\n\n")
				print(requirements)
				print("\n\n")
				input("Entre com qualquer concluir a visualização dos requisitos... ")
				continue
	
	
	def _convert_file_info_into_graph(self, graph_info: dict) -> Graph:
		is_directed = graph_info['is_directed']
		vertices_labels = graph_info['vertices_values']
		edge_labels = graph_info['edge_label_values']
		connected_vertices = graph_info['connected_vertices']
		weight_values = graph_info['weight_values']
		graph = Graph(is_directed)
		try:
			for label in vertices_labels:
				graph.add_vortex(label)
			print(f"Vértices adicionados com sucesso! \U0001F60A")
		except GraphException as e:
			print("⚠ Erro ao adicionar vértice " + str(e) + " ⚠")
			input("Entre com qualquer tecla para continuar... ")
			return None

		try:
			for i in range(0, len(edge_labels)):
				label = edge_labels[i]
				weight = weight_values[i]
				pair_of_vertices = connected_vertices[i]
				graph.add_edge(label, pair_of_vertices, weight)
			print(f"Arestas adicionadas com sucesso! \U0001F60A")
		except GraphException as e:
			print("⚠ Erro ao adicionar arestas " + str(e) + " ⚠")
			input("Entre com qualquer tecla para continuar... ")
			return None
		
		return graph
	

	def _show_import_from_csv_menu(self):
		self._clear_and_apply_headers()
		print("** MENU DE IMPORTAÇÃO DE CSV DE AEROPORTOS DO BRASIL**")
		file_path = input("Entre com o path absoluto do arquivo .csv: ")

		try:
			graph = parse_csv_into_graph(file_path)
			self.graph = graph
			print("Grafo importado do CSV com sucesso! \U0001F60A")
			input("Entre com qualquer tecla para continuar... ")
		except Exception as e:
			print("⚠ Erro ao fazer o parse do csv: " + str(e) + " ⚠")
			input("Entre com qualquer tecla para voltar ao Menu principal... ")


	def _convert_path_list_into_string(self, path_list: list) -> str:
		return " -> ".join(path_list)
		

	def _clear(self):
		if name == 'nt':
			system('cls')
		else:
			system('clear')


	def _clear_and_apply_headers(self):
		self._clear()
		print(main_header)
		print(subheader)
		print(group_name_header)

