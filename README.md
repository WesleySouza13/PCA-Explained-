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

sabendo por definiçao que T(v) = λv é o teorema que explica os Autovalores e Autovetores, aplicaremos sobre uma matriz A

{{a11,a12},{a21,a22}}
