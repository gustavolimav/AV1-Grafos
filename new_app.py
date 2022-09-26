def menu():

    opcao = 10

    while opcao != 6:

        print("\n0) INSERIR GRAFO")
        print("1) MOSTRAR GRAFO")
        print("2) ORDEM E TAMANHO DO GRAFO")
        print("3) VERTICES ADJACENTES DE UM VERTICE")
        print("4) SE 2 VERTICES SAO ADJECENTES")
        print("5) CAMINHO MAIS CURTO ENTRE OS VERTICES")
        print("6) SAIR")
        print("\n")

        opcao = int(input())

        if opcao == 0:

            print("1) INSERIR ELEMENTOS SEPARADAMENTE\n2) INSERIR ARQUIVO .TXT\n")

            opcao0 = int(input())

            print("É DIRECIONADO? (s/n)")

            direcionado = input()

            print("É VALORADO? (s/n)")

            valorado = input()

            if opcao0 == 1:
                graph = main(1, direcionado, valorado)
                opcao = 10
            elif opcao0 == 2:
                graph = main(2, direcionado, valorado)
                opcao = 10
            
        if opcao == 1:
            print("1) MOSTRAR GRAFO\n")
            print(graph)

        elif opcao == 2:
            print("2) ORDEM E TAMANHO DO GRAFO\n")
            ordem, tamanho = tamanho_ordem(graph, direcionado)
            print("Ordem: {} / Tamanho: {}".format(int(ordem), tamanho))

        elif opcao == 3:
            print("3) VERTICES ADJACENTES DE UM VERTICE\n")
        elif opcao == 4:
            print("4) SE 2 VERTICES SAO ADJECENTES\n")
        elif opcao == 5:
            print("5) CAMINHO MAIS CURTO ENTRE OS VERTICES\n")

            print("Escolha 2 vertices\n")
            orig, dest = input().split()
            print_pathes(graph, orig, dest)

        elif opcao == 6:
            print("6) SAIR\n")


def main(flag, dir, val):
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

    print(graph)

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

    with open('input.txt') as f:
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
        visiting = {node: distances[node]\
                    for node in [node for node in\
                    nodes_to_visit if node not in visited]}

        next_to = min(visiting, key = distances.get)

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


menu()
