### PYTHON 3.9.X

##  Tipos de Dados:
'''
str     |   String    # Cadeia de Caracteres
int     |   Integer   # Número Inteiro
float   |   Float     # Número Decimal
bool    |   Boolean   # Verdadeiro ou Falso
'''

##  Estruturas de Dados:
'''
[A, B, C]           |   List          # Aceita valores únicos, cadeias de valores, outras variáveis etc.
{'Blue': 'Azul'}    |   Dictionary    # Formato em pares de Chave: Valor
{Jan, Fev, Mar}     |   Set           # Valores já adicionados não podem ser alterados, mas pode receber novas entradas / Somente valores únicos
("Operação X")      |   Tuple         # Inalterável após definido
'''

##  Definição de Variáveis:
'''
Formato: < nome_da_variavel = valor >
Exemplos:

idade = 30
cidade = "Barcelona"

    ## Definição múltipla:

x = y = z = 0
minha_idade, sua_idade = 25, 20
'''

##  Escopo de Variáveis:
'''
Variável global     |   Criada na indentação raiz do código
Variável local      |   Criada dentro de uma função

*Transforme uma variável local em global incluindo a keyword 'global' antes de sua inicialização
'''

##  Definição de Funções:
'''
Formato: < def nome_da_funcao(parâmetros): >
Exemplo:

def somar_valores(valor1, valor2):
    *** comandos ***
    return *** resultado ***

    ## Funções Lambda (Função anônima simplificada que pode levar múltiplos argumentos sob uma só expressão)
    
x = lambda a, b : a * b
print(x(5, 6))

pessoas = {"Pessoa1": 30, "Pessoa2": 27}
for pessoa in sorted(pessoas, key=lambda pessoa: pessoas[pessoa]):
    print(pessoa, pessoas[pessoa])

    ## Generator (função que resulta em objeto iterável)

def PowTwoGen(max):
    n = 0
    while n < max:
        yield 2 ** n                # Usar yield ao invés de return
        n += 1

x = PowTwoGen(5)
print(next(x))                      # Iterar sobre elementos do gerador
'''

##  Funções Padrões:
'''
abs()       |   Remover sinal numérico                                                                                          |   abs(número)
all()       |   Retorna verdadeiro se todo elemento iterado for True                                                            |   all(iterável)
any()       |   Retorna verdadeiro se qualquer elemento iterado for True                                                        |   any(iterável)
bin()       |   Retorna valor binário de número inteiro                                                                         |   bin(número)
chr()       |   Retorna o caracter de um índice do padrão Unicode                                                               |   chr(índice)
dict()      |   Transforma variável em dicionário quando em formato compatível                                                  |   dict(objeto)
filter()    |   Filtra registros cujo resultado da função seja True                                                             |   filter(função, iterável)
format()    |   Inclui valores diretor ou de variáveis em strings                                                               |   'm{}_str{}ng'.format(valor1, valor2 etc.)
frozenset() |   Transforma variável em set imutável                                                                             |   frozenset(iterável)
hash()      |   Gera um hash do valor                                                                                           |   hash('valor')
hex()       |   Retorna valor hexadecimal de número inteiro                                                                     |   hex(número)
index()     |   Retorna o índice de um dado no objeto                                                                           |   objeto.index(valor)
input()     |   Recebe entrada de dados pelo usuário                                                                            |   input() OU input('Digite o valor aqui: ')
len()       |   Conta quantos elementos tem no texto/objeto                                                                     |   len(texto ou objeto)
list()      |   Transforma variável em lista                                                                                    |   list([valores] ou objeto)
max()       |   Máximo de múltiplos dados                                                                                       |   max(valores ou objeto)
min()       |   Mínimo de múltiplos dados                                                                                       |   min(valores ou objeto)
ord()       |   Retorna o número de um caracter no padrão Unicode                                                               |   ord('caracter')
range()     |   Retorna elementos de um dado intervalo (Início inclusivo, final não inclusivo, progressão)                      |   range(início, fim, offset)
round()     |   Arredonda valores conforme número de casas decimais delimitadas                                                 |   round(valor, decimais)
set()       |   Transforma variável em set (esta função opera de forma iteradora, segregando os elementos a serem adicionados)  |   set(elementos ou objeto)
sum()       |   Soma de valores                                                                                                 |   sum(iterável)
tuple()     |   Transforma variável em tupla                                                                                    |   tuple(string ou iterável)
type()      |   Retorna o tipo de dado                                                                                          |   type(valor ou variável)
zip()       |   Agrega múltiplos objetos iteráveis com base nos índices de seus elementos em tuplas (ver resultado com list(x)) |   zip(iterável1, iterável2 etc.)
'''

##  Operadores
'''
not     |   Negação
in      |   Em
and     |   E
or      |   Ou
==      |   Igualdade
!=      |   Desigualdade
>=      |   Maior ou igual
<=      |   Menor ou igual
%       |   Módulo
**      |   Exponenciação
//      |   Floor Division
'''

##  Condicionais
'''
Formato: < if *** condição ***: >
Exemplo:

if a > b:
    print("A maior que B")
elif a == b:
    print("A igual a B")
else:
    print("A menor que B")
'''

##  Loopings
'''
    ## While:

Formato: < while *** condição ***: >
Exemplo:

counter = 0
while counter < 10:
    *** comandos ***

    ## For:

Formato: < for *** iterador *** in *** objeto iterado *** >
Exemplos:

my_list = [1, 2, 3, 4, 5]
for number in my_list:
    *** comandos ***

my_list = [1, 2, 3, 4, 5]
for index, number in enumerate(my_list):
    *** comandos ***
'''

##  Criar, Abrir e Alterar Arquivos
'''
Formato: < with open('*** arquivo ***', 'modo') >
Exemplos:

with open('teste.txt', 'w+') as file:
    f_newcontent = file.write('Novo Texto')
    print(f_content)

    ## Modos:

'r'     |   Aberto para leitura
'w'     |   Aberto para escrita, truncando o arquivo primeiro
'x'     |   Aberto exclusivamente para criação, falhando se o arquivo já existir
'a'     |   Aberto para escrita, agregando ao final do arquivo caso exista
'b'     |   Modo binário
't'     |   Modo textual
'+'     |   Aberto para atualizar (leitura e escrita)

    ## Anotações:

Utilizar o parâmetro 'encoding=utf8' para exibir caracteres especiais
Utilizar a função readline/readlines para abrir arquivos muito grandes
Para manipular arquivos multimídia utilizar um modo binário: rb, wb, ab
'''

##  Manipulação de Strings
'''
    ## Método  |   Descrição    |   Sintaxe:

upper()       |     Transforma as letras em maiúsculas                      |   my_string.upper()
lower()       |     Transforma as letras em minúsculas                      |   my_string.lower()
isupper()     |     Valida se são letras maiúsculas                         |   my_string.isupper()
islower()     |     Valida se são letras minúsculas                         |   my_string.islower()
startswith()  |     Valida se começa conforme um padrão                     |   my_string.startswith("texto")
endswith()    |     Valida se termina conforme um padrão                    |   my_string.endswith("texto")
title()       |     Capitaliza as primeiras letras das palavras             |   my_string.title()
strip()       |     Remover espaços                                         |   my_string.strip()
lstrip()      |     Remover espaços da esquerda                             |   my_string.lstrip()
rstrip()      |     Remover espaços da direita                              |   my_string.rstrip()
join()        |     Juntar elementos                                        |   "separador".join(elementos)
split()       |     Separar palavras da mesma string                        |   my_string.split("separador")
replace()     |     Substituir caracter                                     |   my_string.replace("antigo", "novo")
find()        |     Retorna o índice do caracter procurado na palavra       |   my_string.find("caracter")
capitalize()  |     Mantém apenas a primeira letra da string em maiúsculo   |   my_string.capitalize()

    ## Slicers:

var[0:3]    |   Pegar os dígitos das posições 0, 1 e 2 da string
var[:3]     |   Pegar os três primeiros dígitos da string
var[3:]     |   Pegar do índice 3 ao último da string
var[-3]     |   Pegar os últimos três dígitos da string
var[:]      |   Pegar todos os dígitos

    ## Escape Sequences:

\b  : Remove caracter anterior
\n  : Nova linha
\t  : Tabulação
\r  : Remove caracteres anteriores

    ## Preenchimento Condicional:

var1 = "Abacaxi"
var2 = 15

myvar = f"A loja comprou {var2} unidades de {var1}"
myvar = "A loja comprou {} unidades de {}".format(var2, var1)
'''

##  Manipulação de Listas
'''
    ## Chamada:

my_list[*** índice ***]

    ## Alteração de Elemento:

my_list[índice] = *** valor novo ***

    ## Método  |   Descrição    |   Sintaxe:

append()      |     Adiciona um valor ao final da lista                                 |   my_list.append(valor)
extend()      |     Adiciona valores de uma lista dentro de outra na sequência          |   my_list.extend(outra_lista)
insert()      |     Adiciona dado em lista em dada posição                              |   my_list.insert(índice, valor)
remove()      |     Remover item de lista por valor                                     |   my_list.remove(valor)
pop()         |     Remover item de lista por índice (caso em branco remove o último)   |   my_list.pop(índice)
clear()       |     Limpa toda a lista                                                  |   my_list.clear()
sort()        |     Ordena itens de uma lista                                           |   my_list.sort()
count()       |     Conta a frequência de dado elemento numa lista                      |   my_list.count(valor)
index()       |     Retorna índice de item em lista                                     |   my_list.index(valor)
reverse()     |     Reverte a ordem da lista                                            |   my_list.reverse()

del           |     Remover item de lista por índice ou slice                                   |   del my_list[índice]
sorted()      |     Ordena itens de uma lista                                                   |   sorted(my_list)
zip()         |     Integra múltiplos objetos iteráveis com base nos índices de seus elementos  |   my_list = list(zip(obj1, obj2))

    ## Slicers:

var[0:3]    |   Pegar os elementos das posições 0, 1 e 2
var[:3]     |   Pegar os três primeiros elementos
var[3:]     |   Pegar do índice 3 ao último da lista
var[-3]     |   Pegar os últimos três elementos
var[:]      |   Pegar todos os elementos

    ## List Comprehensions (Criação de listas a partir de objetos iteráveis):

new_list = [x for x in objeto_iterável]

new_list = [x for x in objeto_iterável if *** condição ***]

new_list = [x if *** condição *** for x in objeto_iterável]

old_list = [8, 13, -7, 4, -9, 2, 10]
new_list = [num if num >= 0 else 0 for num in old_list]
'''
 
##  Manipulação de Dicionários
'''
    ## Chamada:

my_dict[*** chave ***]

    ## Alteração de Elemento:

my_dict[chave] = *** valor novo ***

    ## Método  |   Descrição    |   Sintaxe:

update()  | Atualiza ou adiciona dados a um dicionário conforme chave   |   my_dict.update({chave: valor}) OU my_dict.update(chave = valor)
pop()     | Remove item do dicionário                                   |   my_dict.pop(chave)
clear()   | Limpa todo o dicionário                                     |   my_dict.clear()
get()     | Procura dada chave e retorna valor                          |   my_dict.get(chave)
keys()    | Retorna chaves do dicionário                                |   my_dict.keys()
values()  | Retorna valores do dicionário                               |   my_dict.values()
items()   | Retorna conjuntos de chaves e valores do dicionário         |   my_dict.items()

zip()     | integra múltiplos objetos iteráveis com base nos índices de seus elementos  |   my_dict = dict(zip(chaves, valores))

* Para pesquisar por índice transforme o dicionário em lista

    ## Dictionary Comprehensions (Criação de dicionários a partir de objetos iteráveis):

my_dict = {chave: valor for x in objeto_iterável}

my_dict = {chave: valor for x in objeto_iterável if *** condição ***}

my_dict = {key: value if *** condição *** for element in objeto_iterável}

my_dict = {chave: valor if *** condição *** else valor for x in objeto_iterável}
'''

##  Manipulação de Sets
'''
    ## Chamada:

my_set[*** índice ***]

    ## Método  |   Descrição    |   Sintaxe:

add()       |   Adiciona novos valores      |   my_set.add(valor)
update()    |   Adiciona um set a outro     |   my_set.update(outro_set)
clear()     |   Limpa os elementos do set   |   my_set.clear()

zip()       |   Integra múltiplos objetos iteráveis com base nos índices de seus elementos      |   my_set = set(zip(obj1, obj2))

    ## Operadores:

|   :   União
&   :   Interseção
-   :   Diferença             # Elementos de A que não existem em B e C
^   :   Diferença Simétrica   # Elementos que não existem em A e B, A e C ou B e C

    ## Set Comprehensions (Criação de conjuntos a partir de objetos iteráveis):

new_set = {x for x in objeto_iterável}

new_set = {x for x in objeto_iterável if *** condição ***}

new_set = {x if *** condição *** for x in objeto_iterável}

old_set = {8, 13, -7, 4, -9, 2, 10}
new_set = {num if num >= 0 else 0 for num in old_set}
'''

##  Manipulação de Tuplas
'''
    ## Chamada:

my_tuple[*** índice ***]

    ## Método  |   Descrição    |   Sintaxe:

index() |   Retorna o índice de um valor da tupla                                       |   my_tuple.index(valor)
count() |   Retorna a contagem da ocorrência de um valor na tupla                       |   my_tuple.count(valor)
zip()   |   Integra múltiplos objetos iteráveis com base nos índices de seus elementos  |   my_tuple = tuple(zip(obj1, obj2))
'''

## Regular Expressions
'''
Módulo re
Formato: re + Função + "Expressão"

Funções:
findall     |   Retorna todas as ocorrências                |   re.findall("valor", txt)
search      |   Retorna a posição da primeira ocorrência    |   re.search("\d", txt)
split       |   Separa o texto conforme padrão              |   re.split("\s", txt)
sub         |   Substitui trecho do texto                   |   re.sub("\s", "9", txt)

Expressões comuns:

Range                                   |   [ABC] ou [A-Z] ou [a-zA-Z] ou [0-9]
Qualquer caracter, dígito, símbolo      |   .
Operador OR                             |   A|B
Operador NOT                            |   ^AB
Zero ou mais                            |   A*
Zero ou um                              |   A?
Um ou mais                              |   A+
Contagem específica                     |   A{1}
Ao menos x vezes                        |   A{2,}
Entre x e y vezes                       |   A{2,4}
Backreference (Repetição do anterior)   |   (A)\1(B)\2(C)\3
Espaço(s)                               |   \s
Qualquer caracter menos espaço          |   \S
Qualquer dígito                         |   \d
Qualquer não digito                     |   \D
Caracter alfabético                     |   \w
Qualquer caracter não alfabético        |   \W
Agrupamento                             |   (ABC)
Ignorar agrupamento                     |   (?:Abcd)    
Borda de palavras (início ou fim)       |   \b
Não é borda de palavras                 |   \B
Nova linha                              |   \n
Carriage Return                         |   \r
Tabulação                               |   \t
Nulo                                    |   \0
'''

##  Alguns Módulos:
'''
    ## os (Informações do Sistema):

getcwd()       |   Siretório atual                        |   os.getcwd()
chdir()        |   Mudar diretório                        |   os.chdir('caminho')
listdir()      |   Listar pastas e arquivos do diretório  |   os.listdir()
mkdir()        |   Criar pasta                            |   os.mkdir('diretório')
makedirs()     |   Criar múltiplos níveis de pastas       |   os.makedirs('diretórios')
rmdir()        |   Remover pasta                          |   os.rmdir('diretório')
removedirs()   |   Remover múltiplos níveis de pastas     |   os.removedirs('diretórios')
rename()       |   Renomear pasta ou arquivo              |   os.rename('nome antigo', 'nome novo')

    ## math (Cálculos):

ceil()          |   Arredondar para cima                                |   math.ceil(valor)
dist()          |   Calcular a distância euclidiana                     |   math.dist(ponto1, ponto2)
factorial()     |   Fatorizar um número inteiro                         |   math.factorial(valor)
floor()         |   Arredondar para baixo                               |   math.floor(valor)
fsum()          |   Somar valores com maior precisão                    |   math.fsum(valor) ou math.sum(objeto iterável)
lcm()           |   Mínimo múltiplo comum                               |   math.lcm(valor1, valor2, valorN)
log()           |   Calcular o logaritmo                                |   math.log(valor, base)
log10()         |   Calcular o logaritmo com base 10                    |   math.log10(valor)
modf()          |   Retornar em separado os decimais e inteiros         |   math.modf(valor)
pi()            |   Retornar o valor de pi                              |   math.pi
prod()          |   Retornar o produto de todos os valores do objeto    |   math.prod(objeto iterável)
sqrt()          |   Calcular raiz quadrada                              |   math.sqrt(valor)

    ## time (Período):

asctime()       |   Data e hora atual em formato textual                                    |   time.asctime()
localtime()     |   Data e hora atual                                                       |   time.localtime()
perf_counter()  |   Retorna o período atual em segundos fracionados - usado para contagens  |   time.perf_counter()
sleep()         |   Suspende determinado processo por x segundos                            |   time.sleep(segundos)

    ## datetime (Datação):

datetime()        |   Retorna datação (YY/MM/DD/HR/MIN/SEC)   |   datetime()
year()            |   Retorna o ano                           |   datetime.year()
month()           |   Retorna o mês                           |   datetime.month()
day()             |   Retorna o dia                           |   datetime.day()
weekday()         |   Retorna o índice do dia da semana       |   datetime.weekday()
now()             |   Retorna a datação atual                 |   datetime.now()

    ## random (Pseudo-Randomizações):

random()        |   Gera número aleatório entre 0.0 e 1.0                           |   random.random()
randint()       |   Gera número aleatório dentro de um range de inteiros            |   random.randint(a, b)
randrange()     |   Gera número aleatório conforme degrau em um range de inteiros   |   random.randrange(a, b, degrau)
choice()        |   Escolhe um elemento qualquer de um objeto                       |   random.choice(objeto iterável)
sample()        |   Gera amostra de itens (vindo de lista ou tupla)                 |   random.sample(pop, k)
seed()          |   Gera números aleatórios com base num código de referência       |   random.seed(valor)
shuffle()       |   Embaralha elementos de um objeto                                |   random.shuffle(objeto iterável)

    ## secret (Randomizações):

choice()        |   Gera valor aleatório dentro de uma sequência    |   secrets.choice(objeto iterável)
randbelow()     |   Gera número aleatório dentro de range           |   secrets.randbelow(valor)

    ## string (Relação de Caracteres):

ascii_letters()       |   Gera uma string com os caracteres em letra minúscula e maiúscula    |   string.ascii_letters
ascii_lowercase()     |   Gera uma string com os caracteres em letra minúscula                |   string.ascii_lowercase
ascii_uppercase()     |   Gera uma string com os caracteres em letra maiúscula                |   string.ascii_uppercase
digits()              |   Gera uma string com os números base de 0 a 9                        |   string.digits
punctuation()         |   Gera uma string com os caracteres especiais de pontuação            |   string.punctuation
'''

##  Bibliotecas de Análise de Dados:
'''
    ## pandas (Operações com dados estruturados / Importação, criação de dataframes, preparação de dados etc.):

        # Importação:

read_csv()     |   Ler dados de arquivo CSV (adicionando parâmetro 'header=None' indica ausência de cabeçalho)                         |     pandas.read_csv(file)
read_excel()   |   Ler dados de arquivo Excel                                                                                          |     pandas.read_excel(file)
read_json()    |   Ler dados de arquivo JSON                                                                                           |     pandas.read_json(file)

        # Criação de Series ou Data Frame:

Series()       |   Gerar array uni-dimensional com qualquer tipo de dado                                                               |     pandas.Series(objeto OU coluna do df)
DataFrame()    |   Gerar array bi-dimensional de dados, com índices indicando cada observação                                          |     pandas.DataFrame(dados, index=[índices], columns=[colunas])

        # Visão Geral do Data Frame:

head()             |   Retornar apenas x primeiras linhas da tabela (padrão de 5)                                                          |     df.head(x)
tail()             |   Retornar apenas x últimas linhas da tabela (padrão de 5)                                                            |     df.tail(x)
loc[]              |   Retornar a linha n da tabela                                                                                        |     df.loc[n]
to_string()        |   Retornar a tabela inteira                                                                                           |     df.to_string()
columns            |   Retornar lista de colunas da tabela                                                                                 |     df.columns
dtypes             |   Retornar tipos de dados das colunas da tabela                                                                       |     df.dtypes  
shape              |   Retornar quantidade de linhas e colunas da tabela                                                                   |     df.shape
describe()         |   Retornar estatísticas sobre as colunas (adicionando parâmetro 'include=all' para mostrar colunas não numéricas)     |     df.describe()
info()             |   Retornar sumário de informações da tabela                                                                           |     df.info()

        # Preparação de Dados:

rename()           |   Renomear eixos da tabela conforme par de 'chave: valor'                                                             |     df.rename(mapper={'A': 'a', 'B', 'b'}, axis=1, inplace=True)
replace()          |   Substituir valores específicos em tabela (Ex.: desconhecidos '?')                                                   |     df.replace('?', numpy.NaN) # Not a Number
loc[]              |   Substituir valores em tabela (possibilita usar loop para substituição em massa)                                     |     df.loc[n, "col1"] = 12345
fillna()           |   Substituir valores nulos em tabela                                                                                  |     df.fillna(novovalor) OU df['col1'].fillna(novovalor)
dropna()           |   Remove linhas (0) ou colunas (1) com registros faltantes da tabela                                                  |     df.dropna(subset=["coluna1"], axis=0)
drop()             |   Remover índice, coluna ou valores de uma tabela (adicionando parâmetro 'inplace=True' efetiva a mudança na origem)  |     df.drop(item, inplace=True)
drop_duplicates()  |   Remover linhas duplicadas ou apenas valores de dadas colunas da tabela                                              |     df.drop_duplicates() OU df.drop_duplicates(subset=['col1', 'col2'])
duplicated()       |   Sinalizar se linha é duplicada                                                                                      |     df.duplicated()
join()             |   Combinar tabelas com coluna/índice (chave) em comum                                                                 |     df1.join(df2, on='colx', how='left', rsuffix='sufixo')
merge()            |   Combinar tabelas com colunas/índices em comum                                                                       |     pandas.merge(df1, df2, on='colx', how='left', sort=False)
concat()           |   Unir índices ou colunas de tabelas                                                                                  |     pandas.concat([df1, df2], axis=1, ignore_index=True)
groupby()          |   Retornar resultados agrupados por coluna                                                                            |     df.groupby('coluna')
agg()              |   Retornar resultados de função agregadora (Ex.: sum, count, min, max, mean, median, mode, std, var etc.)             |     df.agg(['mean', 'std']) OU df.agg({'coluna': ['sum', 'min']})
sort_values()      |   Retornar resultados ordenados por critério ascendente ou decrescente                                                |     df.sort_values('coluna1', ascending=True)
explode()          |   Segregar elementos de lista em coluna para múltiplas linhas                                                         |     df.explode('col1')
pivot()            |   Pivotar estrutura e dados de tabela                                                                                 |     df.pivot(index='col1', columns='col2', values='col3')
mean()             |   Retornar média de coluna (parâmetro opcional numeric_only=True)                                                     |     df.mean()
median()           |   Retornar mediana de coluna (parâmetro opcional numeric_only=True)                                                   |     df.median()
mode()             |   Retornar moda de coluna (parâmetro opcional numeric_only=True)                                                      |     df.mode(numeric_only=True) ou df['col1'].mode()[0]
sample()           |   Gerar amostra da tabela                                                                                             |     df.sample(n = 15, replace=True) OU df.sample(frac = 0.1)
to_datetime()      |   Converter campo em formato de data                                                                                  |     pandas.to_datetime(df['col1'])

        # Análise:

corr()             |   Retornar tabela com índices de correlação entre duas colunas                                                        |     df.corr()
plot()             |   Construir representação gráfica da tabela                                                                           |     df.plot(kind = 'tipografico', x = 'col1', y = 'col2')
Kinds: scatter, bar, hist etc.

        # Exportação de Dados:

to_csv()           |   Salvar tabela em arquivo CSV (sem índices)                                                                          |     df.to_csv("diretórioearquivo", index=False)
to_excel()         |   Salvar tabela em arquivo XLSX (sem índices)                                                                         |     df.to_excel("diretórioearquivo", index=False)
to_json()          |   Salvar tabela em arquivo JSON (sem índices)                                                                         |     df.to_json("diretórioearquivo", index=False)

    ## numpy (Operações com arrays - Funcionamento semelhante a estrutura padrão de Listas):

array()         |   Gerar array a partir de valores                                                                             |       numpy.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], dtype='i')
arange()        |   Gerar array com base em determinado intervalo numérico                                                      |       numpy.arange(início, fim)

view()          |   Visualizar array                                                                                            |       array.view()
copy()          |   Copiar dados de array para um novo independente                                                             |       array.copy()
dtype()         |   Retornar tipo de dados do array                                                                             |       array.dtype()
astype()        |   Copiar array para novo com mudança de tipos de dados                                                        |       array.astype('S')
shape()         |   Retornar quantidade de dimensões e quantos elementos possuem cada uma                                       |       array.shape
reshape()       |   Alterar número de dimensões                                                                                 |       array.reshape(dimensões, qtd.elementos)
flatten()       |   Reduzir para array uni-dimensional                                                                          |       array.flatten()

nditer()        |   Retornar objeto iterável dos elementos de arrays n-dimensionais                                             |       numpy.nditer(array)
ndenumerate()   |   Retornar objeto iterável do índice das dimensões e dos elementos de arrays                                  |       numpy.ndenumerate(array)
concatenate()   |   Concatenar arrays em um novo                                                                                |       numpy.concatenate(array1, array2)
stack()         |   Empilhar arrays em um novo                                                                                  |       numpy.stack(array1, array2)
hstack()        |   Empilhar arrays com dimensões na mesma linha                                                                |       numpy.hstack(array1, array2)
vstack()        |   Empilhar arrays com dimensões na mesma coluna                                                               |       numpy.vstack(array1, array2)
array_split()   |   Separar array em n múltiplos arrays                                                                         |       numpy.array_split(array, n)
select()        |   Selecionar valores para coluna com base em condições do mesmo índice                                        |       numpy.select([condições], [valores])
where()         |   Retornar relação de índices de elementos que seguem condição                                                |       numpy.where(array == 14)
sort()          |   Retornar array ordenado                                                                                     |       numpy.sort(array)
searchsorted()  |   Retornar o índice adequado onde o elemento n seria inserido no array já ordenado                            |       numpy.searchsorted(array, n) OU numpy.searchsorted(array, n, side='right')
unique()        |   Retornar relação única de elementos presentes                                                               |       numpy.unique(array)
union1d()       |   Retornar união entre conjuntos de elementos                                                                 |       numpy.union1d(array1, array2)
intersect1d()   |   Retornar intersecção entre conjuntos de elementos                                                           |       numpy.intersect1d(array1, array2, assume_unique=True)
setdiff1d()     |   Retornar elementos exclusivos do primeiro conjunto                                                          |       numpy.setdiff1d(array1, array2, assume_unique=True)
setxor1d()      |   Retornar diferença simétrica (elementos que não se repetem entre os conjuntos)                              |       numpy.setxor1d(array1, array2, assume_unique=True)
percentile()    |   Retornar valor que engloba determinado percentual de valores do conjunto de dados                           |       numpy.percentile(array, 75) 

frompyfunc()    |   Criar função universal                                                                                      |       numpy.frompyfunc(função, qtd_inputs, qtd_outputs)
sum()           |   Retornar soma dos elementos de dois arrays, combinados ou separados                                         |       numpy.sum([array1, array2]) OU numpy.sum([array1, array2], axis=1)
cumsum()        |   Retornar soma cumulativa dos elementos de um array                                                          |       numpy.cumsum(array1)
prod()          |   Retornar produto dos elementos de dois arrays                                                               |       numpy.prod([array1, array2])
add()           |   Retornar vetor da soma entre elementos correspondentes de dois arrays                                       |       numpy.add(array1, array2)
subtract()      |   Retornar vetor da subtração entre elementos correspondentes de dois arrays                                  |       numpy.subtract(array1, array2)
multiply()      |   Retornar vetor da multiplicação entre elementos correspondentes de dois arrays                              |       numpy.multiply(array1, array2)
divide()        |   Retornar vetor da divisão entre elementos correspondentes de dois arrays                                    |       numpy.divide(array1, array2)
power()         |   Retornar vetor da potenciação entre elementos correspondentes de dois arrays                                |       numpy.power(array1, array2)
mod()           |   Retornar vetor do módulo entre elementos correspondentes de dois arrays                                     |       numpy.mod(array1, array2)
divmod()        |   Retornar vetores do quociente e módulo entre elementos correspondentes de dois arrays                       |       numpy.divmode(array1, array2)
absolute()      |   Retornar vetor dos valores absolutos de elementos em array                                                  |       numpy.absolute(array)
trunc()         |   Retornar vetor dos valores truncados (sem decimais) de elementos em array                                   |       numpy.trunc(array)
log2()          |   Retornar array com logs de base 2 dos elementos                                                             |       numpy.log2(array)
log10()         |   Retornar array com logs de base 10 dos elementos                                                            |       numpy.log10(array)
log()           |   Retornar array com logs de base 'e' dos elementos                                                           |       numpy.log(array)
lcm.reduce()    |   Retornar mínimo múltiplo comum entre elementos de array                                                     |       numpy.lcm.reduce(array)
gcd.reduce()    |   Retornar máximo divisor comum entre elementos de array                                                      |       numpy.gcd.reduce(array)
sin()           |   Retornar seno de elementos radianos de array                                                                |       numpy.sin(array)
cos()           |   Retornar cosseno de elementos radianos de array                                                             |       numpy.cos(array)
tan()           |   Retornar tangente de elementos radianos de array                                                            |       numpy.tan(array)
deg2rad()       |   Retornar conversão de valores em graus para radianos                                                        |       numpy.deg2rad(array)
rad2deg()       |   Retornar conversão de valores em radianos para graus                                                        |       numpy.rad2deg(array)
hypot()         |   Retornar valor da hipotenusa de triangulo                                                                   |       numpy.hypot(base, lado)

randint()       |   Retornar n valores pseudo-randômicos inteiros dentro de range                                               |       numpy.random.randint(range, size=(n))
rand()          |   Retornar n valores pseudo-randômicos decimais float entre 0 e 1                                             |       numpy.random.rand(n)
choice()        |   Retornar seleção pseudo-randômica de valores conforme lista de valores e suas probabilidades                |       numpy.random.choice([valores], p=[probabilidades], size=(quantidade))
shuffle()       |   Permutação (embaralhamento) de valores alterando o array original                                           |       numpy.random.shuffle(array)
permutation()   |   Permutação de valores gerando novo array                                                                    |       numpy.random.permutation(array)
normal()        |   Gerar array de distribuição normal (Contínua)                                                               |       numpy.random.normal(loc=média, scale=desviopadrão, size=(x, y))
binomial()      |   Gerar array de distribuição binomial (Discreta)                                                             |       numpy.random.binomial(n=tentativas, p=probabilidades, size=n)
poisson()       |   Gerar array de distribuição Poisson (Discreta)                                                              |       numpy.random.poisson(lam=ocorrencias, size=n)
uniform()       |   Gerar array de distribuição uniforme                                                                        |       numpy.random.uniform(size=(x, y))
logistic()      |   Gerar array de distribuição logística                                                                       |       numpy.random.logistic(loc=média, scale=desviopadrão, size=(x, y))
multinomial()   |   Gerar array de distribuição multinomial                                                                     |       numpy.random.multinomial(n=possibilidades, pvals=[probabilidades], size(x, y))
exponential()   |   Gerar array de distribuição exponencial                                                                     |       numpy.random.exponential(scale=n, size=(x, y))
chisquare()     |   Gerar array de distribuição Chi Square                                                                      |       numpy.random.chisquare(df=degrauliberdade, size=(x, y))
pareto()        |   Gerar array de distribuição Pareto                                                                          |       numpy.random.pareto(a=formato, size=(x, y))

        # Tipos de Dados Numpy:

i | integer
b | boolean
u | unsigned integer
f | float
c | complex float
m | timedelta
M | datetime
O | object
S | string
U | unicode string
V | fixed chunk of memory for other type (void)

    ## scipy (Operações científicas)

dir(constants)  |   Listar valores constantes utilizados em fórmulas científicas                                           |       dir(scipy.constants)
ttest_ind()     |   Retornar t-statistic e p-value da significância entre as médias de duas variáveis                      |       scipy.stats.ttest_ind(var1, var2)
describe()      |   Retornar um sumário estatístico dos valores em array                                                   |       scipy.stats.describe(array)

    ## matplotlib (Gerar visualizações):

plot()      |   Gerar diagrama dos dados para póstuma visualização                                          |       matplotlib.pyplot.plot(eixox, eixoy, marker = 'o', ls = ':')
subplot()   |   Organizar posicionamento dos diagramas dos dados para póstuma visualização                  |       matplotlib.pyplot.subplot(linhas, colunas, posiçãoatual)
show()      |   Visualizar gráficos dos dados                                                               |       matplotlib.pyplot.show()
title()     |   Adicionar título do gráfico                                                                 |       matplotlib.pyplot.title("texto", loc = 'center')
xlabel()    |   Adicionar título do eixo x                                                                  |       matplotlib.pyplot.xlabel("texto")
ylabel()    |   Adicionar título do eixo y                                                                  |       matplotlib.pyplot.ylabel("texto")
xticks()    |   Adicionar todos os valores no eixo x                                                        |       matplotlib.pyplot.xticks(x)
yticks()    |   Adicionar todos os valores no eixo y                                                        |       matplotlib.pyplot.yticks(y)
grid()      |   Adicionar linhas de grade                                                                   |       matplotlib.pyplot.grid(axis = 'y')

hist()      |   Gerar histograma                                                                            |       matplotlib.pyplot.hist(array)
scatter()   |   Gerar gráfico de dispersão                                                                  |       matplotlib.pyplot.scatter(x, y, c=array_cores, s=array_tamanhos, cmap='RdYlGn', alpha=0.5)
bar()       |   Gerar gráfico de barras verticais                                                           |       matplotlib.pyplot.bar(x, y, color='red', width=0.1)
hbar()      |   Gerar gráfico de barras horizontais                                                         |       matplotlib.pyplot.bar(x, y, color='green', height=0.1)
pie()       |   Gerar gráfico de pizza                                                                      |       matplotlib.pyplot.pie(array, labels=array_legendas, explode=array_distancias, shadow=True)
legend()    |   Mostrar barra de legenda de valores                                                         |       matplotlib.pyplot.legend(title='texto')
colorbar()  |   Mostrar barra de legenda de cores                                                           |       matplotlib.pyplot.colorbar()

        # Marcadores

'o'  = Círculo
'*'  = Estrela

OBS: Usar parâmetro 'ms' para o tamanho do marcador | 'mec' para a cor da borda do marcador | 'mfc' para a cor interna do marcador

        # Linhas

'-'  = Linha sólida
':'  = Linha Pontilhada
'--' = Linha Tracejada
'-.' = Linha Pontilhada e Tracejada

OBS: Usar parâmetro 'ls' para o estilo de linha | 'c' para a cor | 'lw' para a espessura da linha

        # Cores

'r' = Red     /   'g' = Green    /   'b' = Blue    /   'c' = Cyan   /   'y' = Yellow    /   'k' = Black

    ## seaborn (Gerar diagramas para plot - visualização):

barplot()       |   Gerar diagrama de barras                                                                   |       seaborn.barplot(x=var1, y=var2, data=dados)
scatterplot()   |   Gerar diagrama de dispersão                                                                |       seaborn.scatterplot(x=var1, y=var2, data=dados)
boxplot()       |   Gerar diagrama de caixa                                                                    |       seaborn.boxplot(x=var1, y=var2, data=dados)
distplot()      |   Gerar diagrama de distribuição de valores                                                  |       seaborn.distplot(valores, hist=False)

'''

##  Coloração de mensagens no Python (terminal)
'''
Padrão ANSI -> Começa com: \033[ + código estilo + código cor + código cor de fundo + m -> Ex: \033[0:33:44m
Estilos = 0 Normal / 1 Negrito / 2 Sublinhado / 3 Negativo
Cores = 30 Branco / 31 Vermelho / 32 Verde / 33 Amarelo / 34 Azul / 35 Roxo / 36 Azul Piscina / 37 Cinza
Cores de Fundo = Código Cor + 10
'''

## Salvando tabela da internet
'''
import requests
import pandas as pd

web_page = requests.get("https://www.infoplease.com/state-abbreviations-and-state-postal-codes")

dfs = pd.read_html(web_page.text)

state_abbv = dfs[0]

state_abbv.to_csv("c:/Users/User/Python_Files/Datasets/state_abbv.csv")
'''

## Acessar banco de dados (Exemplo via SQL Server)
'''
import pyodbc
import pandas as pd

server = 'myserver'
database = 'mydb' 
username = 'myuser'
password = 'mypwd'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)

df = pd.read_sql_query('SELECT * FROM myschema.mytable', cnxn)
print(df)

cnxn.close()
'''

##  Programação Orientada a Objetos
'''
Classe = classificação dos tipos de objetos
Objeto/Instância = item membro de uma classe, sendo composto por métodos e atributos (objetos são chamados de instâncias das classes)
Método = Funções / Atributos = Variáveis

Atributos de classe são definidos dentro da classe mas fora de quaisquer métodos. Seus valores serão os mesmos para todas as instâncias
Atributos de instâncias são definidos dentro de métodos, normalmente no __init__, definindo as propriedades a serem definidas para cada instância com seus próprios valores

O parâmetro 'self' deve ser sempre o primeiro do método, pois refere-se à instância do objeto manipulado

Existem quatro princípios básicos da Programação Orientada a Objetos (OOP): Encapsulation, Abstraction, Inheritance, Polymorphism

Encapsulation: Mecanismo de proteção contra alterações diretas dos atributos da classe, restringindo estas operações somente aos métodos públicos do estilo 'setter' (modificadores)
Para isto, é necessário nomear o atributo com o prefixo '_' ou '__', tornando-o assim privado

Abstraction: Mecanismo de simplificação da herança entre classes, onde uma classe abstrata fornece as diretrizes para a criação de suas derivadas, provendo forma mas não implementação de instâncias
Para sua utilização, deve-se utilizar o módulo 'abc', carregando a classe 'ABC', a ser usada como Parent para a classe abstrata

Inheritance: Mecanismo para definir o relacionamento entre classes 'parent-child', onde as derivadas herdam as propriedades das originais e permitem assim os complementos necessários, economizando código
Para isto, utiliza-se durante a criação da nova classe o formato 'class Child(Parent)'
Caso deseje-se executar o método do Parent dentro do Child, utiliza-se a função super() seguida do método desejado

Polymorphism: Mecanismo de criação de interface única entre métodos semelhantes de classes, retornando como resposta a função respectiva de cada classe do objeto 

        ## Exemplo:

class Carro:                                                    # Classe Parent

    num_veiculos = 0                                            # Atributos de classe

    def __init__(self, modelo, ano, fabricante):                # Método fundamental da classe, executada cada vez que um objeto é gerado para atribuí-lo de valores
        self.modelo = modelo                                    # Atributos das instâncias
        self.ano = ano
        self.fabricante = fabricante
        self.__status = "Disponível"
        Carro.num_veiculos += 1                                 # Manipulação de atributo da classe

    def vender_carro(self):                                     # Método de instâncias
        self.__status = "Vendido"

    def qtd_rodas(self):
        print("Carro tem 4 rodas")

carro1 = Car("Fusca", 1970, "Volkswagen")                       # Criação de objeto
carro1.vender_carro()                                           # Utilização de método

class Moto(Carro):                                              # Classe Child

    def __init__(self, modelo, ano, fabricante):
        super().__init__(modelo, ano, fabricante)               # Execução do método do Parent
        print("Moto adicionada ao inventário")

    def vender_moto(self):
        self.__status = "Vendida"

    def qtd_rodas(self):
        print("Moto tem 2 rodas")

    @staticmethod                                               # Método estático, sem acesso nem possibilidade de alteração do estado da classe
    def alguma_coisa(valor):
        return valor * 1.05

moto1 = Moto("Panigale", 2020, "Ducati")

def verif_rodas(self):                                          # Interface de métodos de classes
    self.qtd_rodas()

verif_rodas(carro1)
verif_rodas(carro2)

        ## Exemplo 2:

from abc import ABC

class Vehicle(ABC):
    def __init__(self, speed, year):
        self.speed = speed
        self.year = year

    def start(self):
        print("Starting engine")

    def stop(self):
        print("Stopping engine")

    @abstractmethod                                             # Decorador indicando um método abstrato
    def drive(self):                                            # Método abstrato que deve ser implementado pelas classes Child
        pass


class Car(Vehicle):
    def __init__(self, speed, year):
        Vehicle.__init__(speed, year)

    def drive(self):                                            # Implementação do método abstrato herdado
        print("Car is in drive mode")

        ## Métodos Especiais

__str__     |   Possibilita uma representação textual do objeto ao ser printado
__rep__     |   Possibilita uma representação textual do objeto ao ser printado
__hash__    |   Retorna o hash de um valor
__bool__    |   Retorna valor booleano
'''

##  Notas
'''
- Python é case sensitive, tanto para keywords quanto para o reconhecimento de objetos
- PEP8 é a convenção de boas práticas de programação em Python para melhor legibilidade do código
-
'''

##  Links Úteis
'''
https://docs.python.org/3.9/
'''