import networkx as nx
import csv
import random


def criar_arestas():
    for i in range(len(lista1)):
        G.add_edge(lista1[i], lista2[i], weight=lista3[i])


def menu(opcao):
    if opcao == 1:
        print("1) MOSTRAR GRAFO\n")
    elif opcao == 2:
        print("2) ORDEM E TAMANHO DO GRAFO\n")
    elif opcao == 3:
        print("3) VERTICES ADJACENTES DE UM VERTICE\n")
    elif opcao == 4:
        print("4) SE 2 VERTICES SAO ADJECENTES\n")
    elif opcao == 5:
        print("5) CAMINHO MAIS CURTO ENTRE OS VERTICES\n")
    elif opcao == 6:
        print("6) SAIR\n")
    else:
        print("1) MOSTRAR GRAFO")
        print("2) ORDEM E TAMANHO DO GRAFO")
        print("3) VERTICES ADJACENTES DE UM VERTICE")
        print("4) SE 2 VERTICES SAO ADJECENTES")
        print("5) CAMINHO MAIS CURTO ENTRE OS VERTICES")
        print("6) SAIR")
        print("\n")



def obter_nos():
    vertices = []
    for i in range(len(lista1)):
        vertices.append(lista1[i])
    for i in range(len(lista2)):
        vertices.append(lista2[i])

    vertices = list(set(vertices))
    vertices.sort()

    return vertices


def criar_pos(lista_nos):
    for no in range(len(lista_nos)):  # listaNos = LISTA DE VERTICES
        G.add_node(lista_nos[no], pos=(random.randint(0, 10), random.randint(0, 10)))


def is_valorado():
    valorado = input("O PARAGRAFO VAI SER VALORADO? (S/n)\n")
    if valorado == 'n':
        valorado = False
    else:
        valorado = True

    return valorado


def is_direcionado():
    direcionado = input("O GRAFO VAI SER DIRECIONAL? (S/n)\n")
    if direcionado == 'n':
        direcionado = False
    else:
        direcionado = True

    return direcionado


# PASSO 1
print("INTRUÇÕES GERAIS PARA USAR O CODIGO\n")

print("1) CRIE UM CSV COM 3 COLUNAS COM OS RESPECTIVOS NOMES: no_1, no_2, peso\n")

print("2) SE O GRAFO FOR DIRECIONADO, ATENTE PARA A ORDEM DOS NÓS NAS COLUNAS\n")

print("3) SE O GRAFO NAO FOR VALORADO PREENCHA A COLUNA peso COM 0 OU 1\n")

aux = input("PRESSIONE ENTER PARA COMECAR\n")

print("ESCOLHA AS CARACTERISTICAS DO GRAFO")

direcionado = is_direcionado()

valorado = is_valorado()

arq = input("DIGITE O NOME DO ARQUIVO EXATAMENTE COMO ELE É, COM O .csv NO FIM\n")  ########

with open(str(arq), encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile)

    lista1 = []
    lista2 = []
    lista3 = []

    for row in reader:
        lista1.append(row['no_1'])
        lista2.append(row['no_2'])
        lista3.append(row['peso'])  # mesmo sem ser direcionado, a lista vai ser preenchida com 0

lista1 = list(map(int, lista1))
lista2 = list(map(int, lista2))
lista3 = list(map(int, lista3))

if direcionado:
    G = nx.DiGraph()
    G.to_directed()
else:
    G = nx.Graph()

listaNos = []
nos = obter_nos()

print("\nnós: " + str(nos) + "\n")

criar_pos(nos)

criar_arestas()

print("GRAFO CRIADO!!\n")

# FUNÇÃO QUE PRINTA O GRAFO
# x.draw(G, with_labels=True,  node_size = 1000)

flag = True
vert = None


def print_graph(G):
    pos = nx.get_node_attributes(G, 'pos')
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw(G, pos, with_labels=True, node_size=800)
    nx.draw_networkx_edge_labels(G, pos, edge_labels, font_size=8)


while flag:
    menu(0)

    opcao = int(input("OPÇÃO: \n"))

    if opcao == 1:
        menu(opcao)
        print_graph(G)

    if opcao == 2:
        menu(opcao)
        print("ORDEM DO GRAFO: " + str(nx.number_of_nodes(G)) + "\n")
        print("TAMANHO DO GRAFO: " + str(nx.number_of_edges(G)) + "\n")

    if opcao == 3:
        menu(opcao)
        vert = input("ESCOLHA O VERTICE A SER ESCOLHIDO\n")
        if direcionado:
            listaE = []
            listaS = []
            for i in range(len(lista1)):
                if lista1[i] == vert:
                    listaS.append(lista2[i])

            for i in range(len(lista1)):
                if lista2[i] == vert:
                    listaE.append(lista1[i])
            print("LISTA DE ENTRADA DO VERTICE" + vert + ": " + str(listaE) + "\n")
            print("LISTA DE SAIDADO VERTICE" + vert + ": " + str(listaS) + "\n")
        if direcionado:
            listaAdj = []
            for i in range(len(lista1)):
                if lista1[i] == vert:
                    listaAdj.append(lista2[i])

            for i in range(len(lista1)):
                if lista2[i] == vert:
                    listaAdj.append(lista1[i])
            # remover duplicadas
            listaAdj.append(5)
            listaAdjFinal = []
            for i in listaAdj:
                if i not in listaAdjFinal:
                    listaAdjFinal.append(i)
            listaAdjFinal.sort()
            print("LISTA DE ADJACENCIA DO VERTICE " + vert + ": " + str(listaAdjFinal) + "\n")

    if opcao == 4:
        menu(opcao)
        vert1 = input("ESCOLHA O VERTICE 1 A SER ESCOLHIDO\n")
        vert2 = input("ESCOLHA O VERTICE 2 A SER ESCOLHIDO\n")
        flag1 = False
        flag2 = False
        if direcionado:
            # TRANSFORMAR ISSO EM FUNCAO
            listaE = []
            listaS = []
            if vert is not None:
                for i in range(len(lista1)):
                    if lista1[i] == vert:
                        listaS.append(lista2[i])
                for i in range(len(lista1)):
                    if lista2[i] == vert:
                        listaE.append(lista1[i])

                for i in range(len(listaE)):  # SENDO DIRECIONADO USAR listaE
                    if listaE[i] == vert1:
                        flag1 = True
                for i in range(len(listaS)):  # SENDO DIRECIONADO USAR listaS
                    if listaS[i] == vert2:
                        flag2 = True

        if direcionado:
            listaAdj1 = []
            for i in range(len(lista1)):
                if lista1[i] == vert1:
                    listaAdj1.append(lista2[i])

            for i in range(len(lista1)):
                if lista2[i] == vert1:
                    listaAdj1.append(lista1[i])
            # remover duplicadas
            listaAdj1.append(5)
            listaAdj1Final = []
            for i in listaAdj1:
                if i not in listaAdj1Final:
                    listaAdj1Final.append(i)
            ###################################################
            listaAdj2 = []
            for i in range(len(lista1)):
                if lista1[i] == vert2:
                    listaAdj2.append(lista2[i])

            for i in range(len(lista1)):
                if lista2[i] == vert2:
                    listaAdj2.append(lista1[i])
            # remover duplicadas
            listaAdj2.append(5)
            listaAdj2Final = []
            for i in listaAdj2:
                if i not in listaAdj2Final:
                    listaAdj2Final.append(i)
            ###################################################
            for i in range(len(listaAdj1)):
                if listaAdj1[i] == 2:
                    flag1 = True
            for i in range(len(listaAdj2)):
                if listaAdj2[i] == 1:
                    flag2 = True
        ###################################################
        if flag1 and flag2:
            print("SAO ADJACENTES\n")
        else:
            print("NAO ADJACENTES\n")

    if opcao == 5:
        menu(opcao)
        vert1 = input("ESCOLHA O VERTICE 1 A SER ESCOLHIDO\n")
        vert2 = input("ESCOLHA O VERTICE 2 A SER ESCOLHIDO\n")
        print("CAMINHO MAIS CURTO ENTRE OS VERTICES ESCOLHIDOS: \n" + str(nx.shortest_path(G, vert1, vert2, 'weight')) +
              "\n")
        print("CUSTO PARA PERCORRER O CAMINHO: " + str(nx.shortest_path_length(G, 1, 6, 'weight')) + "\n")

    if opcao == 6:
        menu(opcao)
        flag = False
