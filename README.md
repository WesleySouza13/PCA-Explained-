## PCA - Explicado de forma Simples 

Mesmo explicando o algoritmo de PCA de forma simples, não abrirei mão de fazer menção à parte matemática, ou seja, tratarei sobre o conceito de álgebra linear de autovalores e autovetores

# Autovalores e Autovetores 
Por definição, estamos tratando do conceito algébrico que descreve uma transformação linear de uma matriz sobre um vetor. Um autovalor não é uma matriz, é um escalar que atua sobre o autovetor, tal que existe um vetor não nulo v, basicamente. E um autovetor é justamente o vetor que sofre essa transformação. Um detalhe que diferencia o comportamento de um autovetor e de um vetor transformado normal é a característica de não sofrer mudanças em suas dependências, ou seja, mantém direção e sentido, sendo apenas escalonado.

O teorema que explica esse evento é dado por: 

T(v) = λv 

Sendo λ uma constante ou martriz de transformaçao e v o vetor

O autovalor trabalha com o conceito de matriz de covariancia, onde precisamos ter uma matriz quadrada, que resume a relação entre várias variáveis de uma matriz.

# Definiçao de matriz quadrada: 

Seja uma matriz quadrada aquela que satisfaz a seguinte condição: número de colunas igual ao número de linhas.

Por exemplo: uma matriz 3x3 satisfaz essa condição, porém uma 2x1 não.

# Trabalhando com numeros

sabendo por definiçao que T(v) = λv é o teorema que explica os Autovalores e Autovetores, aplicaremos sobre uma matriz A 2x2:

A * v -  λ * v1 = 0, onde v1 se trata da matriz identidade 2x2

teremos: 

deT (- λ + A * l)v = 0 --> equação caracteristica

# Aplicaçao em PCA

# O que é PCA?

Principal Components Analysis (análise de componentes principais, em português) é um método matemático/estatístico que busca reduzir a dimensionalidade de dados. Geralmente, utilizamos o PCA para tratar dados que possuem forte multicolinearidade.

O algoritmo de PCA trabalha com a matriz de covariância, a partir da qual são calculados os autovalores e autovetores.

Com os autovalores calculados em mãos, é feita a soma de todas as variâncias (representadas pelos próprios autovalores) para, então, calcular o percentual de variância explicada pela soma total ou por cada componente principal calculado.

o Algoritimo seleciona aqueles componentes que melhor explicam a variabilidade dos dados. 

# O que o PCA nos retorna? 

O PCA nos retorna componentes que são ortogonais entre si, ou seja, variáveis transformadas que não possuem correlação umas com as outras.

# Prós e contras em utilizar o PCA

Prós:

- Se estivermos trabalhando com dados que possuem muita multicolinearidade, é um meio de cortar isso pela raiz
- Dados com ruidos podem ser "resumidos" sem componentes calculados com o PCA, dimuindo as incertezas dos dados
- Dados que passam por reduçao de dimensionalidade, constumam ocupar menos espaço, ainda sim nao perdendo informaçoes




       
