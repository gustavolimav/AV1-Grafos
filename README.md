<h1 align="center"style="font-size:30px">Avaliação 1 - Teoria dos Grafos</h1>
<br>
<h2 align="center"style="font-size:15px">Grupo: Carolina Vasconcelos, Ewerton Luna, Mariana Coutinho</h2>
<br>
<body>
    <h1 align="center"style="font-size:30px">Manual do Usuário Meraki</h1>
    <p> O sistema  tem como objetivo criar grafos simples utilizando informações fornecidas  pelo usuário . Para utilizar o sistema tem que fornecer: informação se é direcionado ou não, um nome para cada vértice, um nome para cada   aresta, o peso de cada aresta. Não é possível colocar valores negativos nos pesos. É possível colocar qualquer nome ou número as vértices  e as arestas também. Como também verificar as vértices que estão conectadas, e o menor caminho para  percorrer as vértices escolhidas, através do algoritmo de Dijkstra.</p>
    <h2 align="left"style="font-size:25px">Requisitos:</h2>
    <ul>
        <li>Interpretador Pyhton3</li>
        <li>Editor de texto</li>
    </ul>
    <br>
    <h3 align="left"style="font-size:25px">Como executar:</h3>
    <h4  align="left"style="font-size:15px">A partir do diretório raiz do projeto, entre com o comando <pre>python3 app.py</pre></h4>
    <br>
    <h3 align="left"style="font-size:25px">Como utilizar:</h3>
    <p>A cada informação que entrar no sistema, o programa irá dar um feedback de sucesso ou erro para orientar o usuário durante a interação</p>
    <ul>
        <li><h3 align="left"style="font-size:20px">Inserção por itens:</li>
    </ul>
    <ol>
        <li>No menu inicial, digite '1' para adicionar um vértice.</li>
        <img src="imagens/Captura de Tela 2022-04-13 às 20.13.28.png">
        <li>Em seguida determine se o grafo é direcionado (digite '1') ou não direcionado (digite '2').</li>
        <li>Agora crie todos os vértices do seu grafo inserindo uma label por vez. Quando finalizar, digite 'sair'.</li>
        <li>De volta ao menu incial digite '2' para inserir as arestas do grafo.</li>
        <li>Digite a label da aresta, em seguida seu peso, caso não tenha, digite '0'. Agora determine o vértice de saída e o de entrada dessa aresta. Ao inserir todas as arestas, digite 'sair' para voltar ao menu principal.</li>
        <li>Pronto! Grafo criado, para visualizar informações como grau e o menor caminho entre dois pontos, digite '3'.</li>
    </ol>
    <br>
    <ul>
        <li><h3 align="left"style="font-size:20px">Inserção por lote através de arquivo padronizado:</li>
    </ul>
    <ol>
        <li>No menu inicial, digite '4'.</li>
        <li>Leia os requisitos e formatação correta do arquivo antes de importar o grafo digitando '2'.</li>
        <li>Agora digite '1' para e insira o path absoluto da localização do arquivo contendo o grafo.</li>
        <img src="imagens\Captura de Tela 2022-04-13 às 20.13.43.png">
        <li>Caso o arquivo não esteja na formatação correta, a aplicação informará a linha que ocorreu o erro. Caso contrário seu grafo foi adicionado com sucesso!</li>
    </ol>
    <ul>
        <li><h3 align="left"style="font-size:20px">Inserção por lote usando o arquivo CSV dos aeroportos:</li>
    </ul>
    <ol>
        <li>No menu inicial, digite '5'.</li>
        <li>Entre com "./aeroportos-do-brasil.csv" para usar o arquivo CSV contido dentro do diretório raiz do projeto</li>
        <li>Caso não tenha havido erro no input, o CSV será importado e transformado em grafo com sucesso!</li>
    </ol>
    <br>
    <h3 align="left"style="font-size:25px">Visualização do grafo:</h3>
    <p>Para iniciar, digite '3' no menu principal.</p>
    <br>
    <img src="imagens\Captura de Tela 2022-04-13 às 20.13.59.png">
    <ul>
        <li><h3 align="left"style="font-size:15px">Grau de um vértice:</li>
        <p>Digite '1' e em seguida a label do vértice que deseja saber o grau.</p>
        <li><h3 align="left"style="font-size:15px">Menor caminho entre dois pontos:</li>
        <p>Digite '2', em seguida a label do vértice de partida e logo após o de chegada. Será impresso o menor caminho como também seu custo calculado a partir do algoritmo de Dijkstra.</p>
        <li><h3 align="left"style="font-size:15px">Lista de vértices adjacentes:</li>
        <p>Digite '3', em seguida a label do vértice que deseja visualizar a lista de adjacências.</p>
        <li><h3 align="left"style="font-size:15px">Verificar se dois vértices são adjacentes:</li>
        <p>Digite '4', insira um vértice seguido por outro. A informação é impressa em seguida.</p>
        <li><h3 align="left"style="font-size:15px">Visualizar o grafo:</li>
        <p>Digite '5', não há necessidade de inserir nada, já serão impressas as seguintes informações: se é direcionado ou não como também os vértices com suas labels e os vértices adjacentes, além das arestas com sua label, peso e os vértices que conecta.</p>
        <li><h3 align="left"style="font-size:15px">(Requisito surpresa) Verificar se um vértice é pendente:</li>
        <p>Digite '6', em seguida o vértice que deseja checar e a informação já será impressa .</p>
        <li><h3 align="left"style="font-size:15px">Ver ordem do grafo:</li>
        <p>Digite '7' e a informação já será impressa .</p>
        <li><h3 align="left"style="font-size:15px"> Ver tamanho do grafo:</li>
        <p>Digite '8' e a informação já será impressa.</p>
    </ul>
</body>