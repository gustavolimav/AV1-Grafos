# Manual do Usuário

## `Alunos:`
- Gustavo Lima 
- Pedro Almeida
- Rafael Malheiros
- Rafael Ghinato 
- Maria Carolina

## `Requisitos:`
- Intepretador Python 3
- Editor de Texto

## `Como Utilizar:`

- Rodando o código temos a possibilidade de escolher a forma de input de dados:

- Separadamente:

    Ex:
    <br>
    `3 3`
    <br>
    `1 2 2`
    <br>
    `2 2 3`
    <br>
    `3 1 5`
    <br>
    Sendo os primeiros 2 valores a quantidade de vértices e arestas.
    Os valores abaixo são a ligação entre os vértices e seu valor de custo (Apenas necessitando esse ultimo valor se o grafo for valorado).

- Inserindo o TXT da pasta "Inputs":
    Ex: input_v_d (o "v" significa "valorado" e o "d" significa "direcionado")


- Aeroportos do Brasil:
    Só seguir o fluxo.

- Após isso, basta seguir o fluxo com opções auto-explicativas

## `Funcionalidades do Sistema`

### Grafo Direcionado ou Não direcionado:
- Direcionado:
    Grafo que vai de um vértice a outro
    ![alt text](/Images/direcionado.png)

- Não Direcionado:
    Grafo que não tem direção entre os vértices (todos vão e voltam)
    ![alt text](/Images/naoDirecionado.png)

### Grafo Valorado:
- Possui o valor de custo em suas arestas
    ![alt text](/Images/valorado.png)

## Exemplo com um grafo direcionado e valorado (Inputs/input_v_d):
![alt text](/Images/inputVD.png)

### Ordem e tamanho do grafo:
- Verifica o tamanho (quantidade de vértices) e Ordem (quantidade de arestas)
    ![alt text](/Images/ordemTamanho.png)

### Vertices adjacentes de um vertice (Vértice: 3):
- Identiica os vértices adjacentes ao escolhido (ligado por arestas)
    ![alt text](/Images/adjacenteVertice3.png)

### Verificar se 2 vértices são adjacentes:

- Vértices: 3 e 4
    <br>
    ![alt text](/Images/verificarVertices.png)
    
- Vértices: 3 e 5
    <br>
    ![alt text](/Images/verificaVertices2.png)

### Caminho mais curto entre os vértices (Vértices: 3 e 8):
- Atravéz de um algorítimo de busca, verifica o caminho mais curto para o vertice A chegar até o vértice B
    ![alt text](/Images/caminhoVertices.png)

### Vértice com maior grau:
- Grau de Entrada: Vértice com maior número de conexões de entrada
- Grau de Saída: Vértice com maior número de conexões de saída
    ![alt text](/Images/verticeMaiorGrau.png)