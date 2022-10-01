def menu():
    opcao = 10

    print("1) INSERIR ELEMENTOS SEPARADAMENTE\n2) INSERIR ARQUIVO .TXT\n")

    opcao0 = int(input())

    print("É DIRECIONADO? (S/n)")

    direcionado = input()

    if direcionado != "n":
        direcionado = "s"

    print("É VALORADO? (S/n)")

    valorado = input()

    if valorado != "n":
        valorado = "s"

    if opcao0 == 1:
        graph = create_graph(1, direcionado, valorado)
        opcao = 10
    elif opcao0 == 2:
        graph = create_graph(2, direcionado, valorado)
        opcao = 10

    while opcao != 7:

        print("1) MOSTRAR GRAFO")
        print("2) ORDEM E TAMANHO DO GRAFO")
        print("3) VERTICES ADJACENTES DE UM VERTICE")
        print("4) SE 2 VERTICES SAO ADJECENTES")
        print("5) CAMINHO MAIS CURTO ENTRE OS VERTICES")
        print("6) VÉRTICE COM MAIOR GRAU")
        print("7) SAIR")
        print("\n")

        opcao = int(input())

        if opcao == 1:
            print("1) MOSTRAR GRAFO\n")
            print(str(graph))

        elif opcao == 2:
            print("2) ORDEM E TAMANHO DO GRAFO\n")

            ordem, tamanho = tamanho_ordem(graph, direcionado)

            print("Ordem: {} / Tamanho: {}".format(int(ordem), tamanho))

        elif opcao == 3:
            print("3) VERTICES ADJACENTES DE UM VERTICE")
            print("Escolha 1 vertice\n")

            vert = str(input())

            if direcionado:
                adj_list_in = []
                adj_list_out = []

                for adjVert in graph.get(vert):
                    adj_list_in.append(adjVert)

                graph_keys = graph.keys()

                for key in graph_keys:
                    for adjVert in graph.get(key):
                        if adjVert == vert:
                            adj_list_out.append(key)

                adj_list_in_str, adj_list_out_str = adj_list_str(adj_list_in, adj_list_out)

                print("Adjacentes de entrada: " + adj_list_in_str)
                print("Adjacentes de saida: " + adj_list_out_str)
            else:
                adj_list = []

                for adjVert in graph.get(vert):
                    adj_list.append(adjVert)

                print("Adjacentes: " + str(adj_list))

        elif opcao == 4:
            print("4) SE 2 VERTICES SAO ADJECENTES")
            print("Escolha 2 vertices\n")

            vert1 = str(input())
            vert2 = str(input())

            is_adjacente(graph, vert1, vert2)

        elif opcao == 5:
            print("5) CAMINHO MAIS CURTO ENTRE OS VERTICES\n")

            print("Escolha 2 vertices\n")

            orig = input()
            dest = input()

            print_pathes(graph, orig, dest)

        elif opcao == 6:
            print("6) VÉRTICE COM MAIOR GRAU DO GRAFO\n")

            if direcionado == "n":
                vertices, value = ND_biggest_degree(graph, direcionado)
                print("O(s) vértice(s) com o maior grau é(são): {}, com o grau: {}\n".format(vertices, value))
            else:
                in_v, max_in_v, out_v, max_out_v, general_v, max_general_v = biggest_degree(graph, direcionado)
                print("O(s) vértice(s) com o maior grau de entrada é(são): {}, com o grau: {}".format(in_v, max_in_v))
                print("O(s) vértice(s) com o maior grau de saida é(são): {}, com o grau: {}".format(out_v, max_out_v))
                print("O(s) vértice(s) com o maior grau total é(são): {}, com o grau: {}\n".format(general_v, max_general_v))

        elif opcao == 7:
            print("7) SAIR\n")


def adj_list_str(adj_list_in, adj_list_out):
    adj_list_in_str = "-"
    adj_list_out_str = "-"
    if adj_list_in is not None:
        adj_list_in_str = str(adj_list_in)
    if adj_list_out is not None:
        adj_list_out_str = str(adj_list_out)

    return adj_list_in_str, adj_list_out_str


def is_adjacente(graph, vert1, vert2):
    flag = False
    for adjVert in graph.get(vert1):
        if adjVert == vert2:
            print("Os vertices " + vert1 + " e " + vert2 + " sao adjacentes")
            flag = True
    if flag is not True:
        print("Os vertices " + vert1 + " e " + vert2 + " nao sao adjacentes")


def create_graph(flag, dir, val):
    graph = {}

    if val == 's':
        if flag == 1:
            insert_graph(graph, dir)

        if flag == 2:
            insert_graph_txt(graph, dir)

    elif val == 'n':
        if flag == 1:
            NV_insert_graph(graph, dir)

        if flag == 2:
            NV_insert_graph_txt(graph, dir)

    return graph


def tamanho_ordem(graph, dir):
    o = 0

    for node in graph.keys():
        o = o + len(graph[node])

    if dir == 'n':
        o = o / 2

    t = len(graph.keys())

    return o, t


def insert_graph(graph, dir):
    n, e = input("Insira o número de nós e arestas\n").split()

    for i in range(1, int(n) + 1):
        graph[str(i)] = {}

    for i in range(int(e)):
        u, v, d = input("Insira a aresta no formato origem/destino/distancia\n").split()
        graph[u][v] = int(d)
        if dir == "n":
            graph[v][u] = int(d)


def insert_graph_txt(graph, dir):
    arq = str(input("Insira o nome do arquivo txt"))

    with open(arq) as f:
        lines = f.readlines()

    n = int(lines[0].split()[0])
    e = int(lines[0].split()[1])

    for i in range(1, n + 1):
        graph[str(i)] = {}

    for i in range(1, e + 1):
        u = lines[i].split()[0]
        v = lines[i].split()[1]
        d = int(lines[i].split()[2])
        graph[u][v] = d
        if dir == "n":
            graph[v][u] = d


def NV_insert_graph(graph, dir):
    n, e = input("Insira o número de nós e arestas\n").split()

    for i in range(1, int(n) + 1):
        graph[str(i)] = {}

    for i in range(int(e)):
        u, v, d = input("Insira a aresta no formato origem/destino\n").split()
        graph[u][v] = 0
        if dir == "n":
            graph[v][u] = 0


def NV_insert_graph_txt(graph, dir):
    with open('input.txt') as f:
        lines = f.readlines()

    n = int(lines[0].split()[0])
    e = int(lines[0].split()[1])

    for i in range(1, n + 1):
        graph[str(i)] = {}

    for i in range(1, e + 1):
        u = lines[i].split()[0]
        v = lines[i].split()[1]
        graph[u][v] = 0
        if dir == "n":
            graph[v][u] = 0


def print_pathes(graph, orig, dest):
    p, d = busca(graph, orig, dest)

    print("Menor path do vertice {} para o vertice {}: {} / Distancia: {}".format(orig, p[-1], ' -> '.join(p[0:]), d))


def is_in_path(o, p, parent):
    while o not in p:
        p.append(parent[p[-1]])


def visit(graph, distances, parent, nodes_to_visit):
    visited = []

    while len(visited) < len(nodes_to_visit):
        visiting = {node: distances[node] \
                    for node in [node for node in \
                                 nodes_to_visit if node not in visited]}

        next_to = min(visiting, key=distances.get)

        visited.append(next_to)

        for node in graph[next_to]:
            if distances[node] > distances[next_to] + graph[next_to][node]:
                distances[node] = distances[next_to] + graph[next_to][node]
                parent[node] = next_to


def busca(graph, orig, dest):
    distances = {}
    parent = {}

    nodes_to_visit = graph.keys()

    for node in graph:
        distances[node] = float('inf')
        parent[node] = None

    distances[orig] = 0

    visit(graph, distances, parent, nodes_to_visit)

    path = [dest]

    is_in_path(orig, path, parent)

    return path[::-1], distances[dest]

def ND_biggest_degree(graph, direcionado):

    degree = {}
    degree_v = []

    for i in graph.keys():
        degree[i] = len(graph.get(i))

    for key in graph.keys():
        if degree[key] == max(degree.values()):
            degree_v.append(key)

    return degree_v, max(degree.values())

def biggest_degree(graph, direcionado):

    graph_keys = graph.keys()

    list_values = []

    degree_in = {}
    degree_in_v = []
    degree_out = {}
    degree_out_v = []
    degree = {}
    degree_v = []

    for i in graph_keys:
        for j in graph.get(i):
            list_values.append(j)
        degree_in[i] = len(list_values)
        list_values = []

    list_values = []

    for i in graph_keys:
        for key in graph_keys:
            for j in graph.get(key):
                if j == i:
                    list_values.append(key)
        degree_out[i] = len(list_values)
        list_values = []

    for key in graph_keys:
        degree[key] = degree_in.get(key) + degree_out.get(key)

    for key in graph_keys:
        if degree_in.get(key) == max(degree_in.values()):
            degree_in_v.append(key)
        if degree_out.get(key) == max(degree_out.values()):
            degree_out_v.append(key)
        if degree.get(key) == max(degree.values()):
            degree_v.append(key)

    return degree_in_v, max(degree_in.values()), degree_out_v, max(degree_out.values()), degree_v, max(degree.values())

menu()
