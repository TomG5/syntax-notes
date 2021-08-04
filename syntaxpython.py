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
{'Blue': 'Azul'}    |   Dictionary    # Formato em pares de < Chave: Valor >
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

##  Definição de Funções:
'''
Formato: < def nome_da_funcao(parâmetros): >
Exemplo:

def somar_valores(valor1, valor2):
    *** comandos ***
    return *** resultado ***
'''

##  Funções Padrões:
'''
abs()       |   remover sinal numérico
all()       |   retorna verdadeiro se todo elemento iterado for True
any()       |   retorna verdadeiro se qualquer elemento iterado for True
bin()       |   retorna valor binário de número inteiro
chr()       |   retorna o caracter de um índice do padrão Unicode
dict()      |   transforma variável em dicionário
drop()      |   remove índice, coluna ou valores de uma matriz (adicionando parâmetro 'inplace=True' efetiva a mudança)
filter()    |   filtra registros cujo resultado da função seja True #Sintaxe < filter(*** função ***, *** iteravel ***) >
format()    |   inclui valores de variáveis em strings delimitadas por {} (utilizado após a string)
frozenset() |   transforma variável em set imutável
hash()      |   gera um hash do valor
head()      |   printar primeiros resultados
hex()       |   retorna valor hexadecimal de número inteiro
index()     |   retorna o índice de um dado no objeto
input()     |   recebe entrada de dados pelo usuário
len()       |   conta quantos elementos tem no objeto
list()      |   transforma variável em lista
max()       |   máximo de múltiplos dados
min()       |   mínimo de múltiplos dados
ord()       |   retorna o número de um caracter no padrão Unicode
range()     |   retorna elementos de um dado intervalo (inclusivo, não inclusivo)
round()     |   arredonda valores conforme número de casas decimais delimitadas
set()       |   transforma variável em set (esta função opera de forma iteradora, segregando os elementos a serem adicionados)
sum()       |   soma de valores
tail()      |   printar últimos resultados
tuple()     |   transforma variável em tupla
type()      |   retorna o tipo de dado da variável
unique()    |   printar valores únicos de dada coluna, lista etc.
zip()       |   integra múltiplos objetos iteráveis com base nos índices de seus elementos
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

with open('teste.txt', 'r') as file:
    f_content = f.read()
    print(f_content)
close(file)

with open('teste.txt', 'w+') as file:
    f_newcontent = f.write('Novo Texto')
    print(f_content)
close(file)

    ## Modos:

'r'     |   aberto para leitura
'w'     |   aberto para escrita, truncando o arquivo primeiro
'x'     |   aberto exclusivamente para criação, falhando se o arquivo já existir
'a'     |   aberto para escrita, agregando ao final do arquivo caso exista
'b'     |   modo binário
't'     |   modo textual
'+'     |   aberto para atualizar (leitura e escrita)

    ## Anotações:

Utilizar o parâmetro 'encoding=utf8' para exibir caracteres especiais
Utilizar a função readline/readlines para abrir arquivos muito grandes
Para manipular arquivos multimídia utilizar o modo binário: rb, wb, ab
'''

##  Manipulação de Strings
'''
    ## Método  |   Descrição    |   Sintaxe:

upper()       |     todas as letras maiúsculas                              |   my_string.upper()
lower()       |     todas as letras minúsculas                              |   my_string.lower()
isupper()     |     valida se são letras maiúsculas                         |   my_string.isupper()
islower()     |     valida se são letras minúsculas                         |   my_string.islower()
title()       |     todas as primeiras letras das palavras maiúsculas       |   my_string.title()
strip()       |     remover espaços                                         |   my_string.strip()
join()        |     juntar elementos                                        |   "separador".join(letras)
split()       |     separar palavras da mesma string                        |   my_string.split("separador")
replace()     |     substituir caracter                                     |   my_string.replace("antigo", "novo")
find()        |     retorna o índice do caracter procurado na palavra       |   my_string.find("caracter")
capitalize()  |     mantém apenas a primeira letra da string em maiúsculo   |   my_string.capitalize()

    ## Slicers:

var[0:3]    |   pegar os dígitos das posições 0, 1 e 2 da string
var[:3]     |   pegar os três primeiros dígitos da string
var[3:]     |   pegar do índice 3 ao último da string
var[-3]     |   pegar os últimos três dígitos da string
var[:]      |   pegar todos os dígitos

    ## Escape Sequences:

\b  : remove caracter anterior
\n  : nova linha
\t  : tabulação horizontal
\r  : remove caracteres anteriores
'''

##  Manipulação de Listas
'''
    ## Chamada:

my_list[*** índice ***]

    ## Alteração de Elemento:

my_list[índice] = *** valor novo ***

    ## Método  |   Descrição    |   Sintaxe:

append()      |     adiciona um valor ao final da lista                                 |   my_list.append(valor)
extend()      |     adiciona valores de uma lista dentro de outra na sequência          |   my_list.extend(outra_lista)
insert()      |     adiciona dado em lista em dada posição                              |   my_list.insert(índice, valor)
remove()      |     remover item de lista por valor                                     |   my_list.remove(valor)
pop()         |     remover item de lista por índice (caso em branco remove o último)   |   my_list.pop(índice)
clear()       |     limpa toda a lista                                                  |   my_list.clear()
sort()        |     ordena itens de uma lista                                           |   my_list.sort()
count()       |     conta a frequência de dado elemento numa lista                      |   my_list.count(valor)
index()       |     retorna índice de item em lista                                     |   my_list.index(valor)
reverse()     |     reverte a ordem da lista                                            |   my_list.reverse()

del           |     remover item de lista por índice ou slice                                   |   del my_list[índice]
sorted()      |     ordena itens de uma lista                                                   |   sorted(my_list)
zip()         |     integra múltiplos objetos iteráveis com base nos índices de seus elementos  |   my_list = list(zip(obj1, obj2))

    ## Slicers:

var[0:3]    |   pegar os elementos das posições 0, 1 e 2
var[:3]     |   pegar os três primeiros elementos
var[3:]     |   pegar do índice 3 ao último da lista
var[-3]     |   pegar os últimos três elementos
var[:]      |   pegar todos os elementos

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

update()  | atualiza ou adiciona dados a um dicionário conforme chave   |   my_dict.update({chave: valor}) ou my_dict.update(chave = valor)
pop()     | remove item do dicionário                                   |   my_dict.pop(chave)
clear()   | limpa todo o dicionário                                     |   my_dict.clear()
get()     | procura dada chave e retorna valor                          |   my_dict.get(chave)
keys()    | retorna chaves do dicionário                                |   my_dict.keys()
values()  | retorna valores do dicionário                               |   my_dict.values()
items()   | retorna conjuntos de chaves e valores do dicionário         |   my_dict.items()

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

add()       |   adiciona novos valores      |   my_set.add(valor)
update()    |   adiciona um set a outro     |   my_set.update(outro_set)
clear()     |   limpa os elementos do set   |   my_set.clear()

zip()       |   integra múltiplos objetos iteráveis com base nos índices de seus elementos      |   my_set = set(zip(obj1, obj2))

    ## Operadores:

|   :   união
&   :   interseção
–   :   diferença             # Elementos de A que não existem em B e C
^   :   diferença simétrica   # Elementos que não existem em A e B, A e C ou B e C

    ## Set Comprehensions (Criação de conjuntos a partir de objetos iteráveis):

new_set = {x for x in objeto_iterável}

new_set = {x for x in objeto_iterável if *** condição ***}

new_set = {x if *** condição *** for x in objeto_iterável}

old_set = {8, 13, -7, 4, -9, 2, 10}
new_set = {num if num >= 0 else 0 for num in old_set}
'''

## Manipulação de Tuplas
'''
    ## Chamada:

my_tuple[*** índice ***]

    ## Método  |   Descrição    |   Sintaxe:

index() |   retorna o índice de um valor da tupla                   |   my_tuple.index(valor)
count() |   retorna a contagem da ocorrência de um valor na tupla   |   my_tuple.count(valor)

zip()   |   integra múltiplos objetos iteráveis com base nos índices de seus elementos  |   my_tuple = tuple(zip(obj1, obj2))
'''

D) Alguns Módulos:

D1) os = informações do sistema
os.getcwd -> diretório atual / os.chdir -> mudar diretório
os.listdir -> listar pastas e arquivos do diretório
os.mkdir -> criar pasta / os.makedirs -> criar múltiplos níveis de pastas
os.rmdir -> remover pasta / os.removedirs -> remover múltiplos níveis de pastas
os.rename -> renomear pasta ou arquivo
os.stat -> informações da pasta/arquivo

D2) math = cálculos matemáticos
math.ceil -> arredondar para cima / math.floor -> arredondar para baixo
math.sum -> somar lista / math.sqrt -> raiz quadrada

D3) time = período atual (para comparações)
time.localtime() -> data e hora atual
time.perf_counter() -> horário atual para contagens

D4) datetime = período atual (para registros)
datetime -> retorna datação (YY/MM/DD/HR/MIN/SEC) / year -> retorna o ano / month -> retorna o mês / day -> retorna o dia / weekday -> retorna o índice do dia da semana
datetime.now -> retorna a datação atual

D5) random = randomizar
random.randint -> gerar número aleatório dentro de um range / random.choice -> escolhe um dado de uma determinada lista / random.seed -> gera números aleatórios com base num código de referência (Ex: 101)
random.shuffle

D6) pickle = salvar cópia do script em determinado estado de execução
*variável = open(file_Name,'rb') -> para ler / *variável = open(file_Name,'wb') -> para editar / *variável = pickle.load(arquivo) -> para passar dados para nova variável 
pickle.dump("entrada",*variável) -> insere informação no arquivo / *variável.close() -> fechar o arquivo / 

E) Bibliotecas:

E1) matplotlib
matplotlib.pyplot -> gerar gráficos

E2) numpy = gerar arrays/matrizes
numpy.arange -> gerar array com base em dado range / numpy.copy -> copiar dados de variável/índice para outro / numpy.reshape -> alterar número de linhas/colunas de um array
numpy.linspace -> gerar array com n número de linhas com base em range

E3) pandas
pandas.DataFrame -> criar tabela de dados (dados, índices, colunas) / pandas.read_csv -> ler dados de arquivo CSV

E) hashlib

F) Coloração de mensagens no Python (terminal)
Padrão ANSI -> Começa com: \033[ + código estilo + código cor + código cor de fundo + m -> Ex: \033[0:33:44m
Estilos = 0 Normal / 1 Negrito / 2 Sublinhado / 3 Negativo
Cores = 30 Branco / 31 Vermelho / 32 Verde / 33 Amarelo / 34 Azul / 35 Roxo / 36 Azul Piscina / 37 Cinza
Cores de Fundo = Código Cor + 10

## Uso do módulo matplotlib para gerar gráfico

import matplotlib.pyplot as plt

valores_x = [5, 4, 3, 2.5, 7]
legenda = ["JAN", "FEV", "MAR", "ABR", "MAI"]

plt.xticks([1,2,3,4,5], legenda)
plt.plot([1,2,3,4,5], valores_x)
plt.show()

## Uso dos módulos numpy e pandas para geração de tabela randômica

import numpy as np
import pandas as pd

np.random.seed(101)

df = pd.DataFrame(np.random.randn(5, 4), index = "01 02 03 04 05".split(), columns = "A B C D".split())

df.drop('05', inplace = True)
df.drop('D', axis = 1, inplace = True)

print(df)

## Salvando tabela da internet

import requests
import pandas as pd

web_page = requests.get("https://www.infoplease.com/state-abbreviations-and-state-postal-codes")

dfs = pd.read_html(web_page.text)

state_abbv = dfs[0]

state_abbv.to_csv("c:/Users/Thomas/Documents/Python_Files/Datasets/state_abbv.csv")

## Programação Orientada a Objetos

# Objeto/Instância = item utilizado no algoritmo composto por código + dados (objetos são chamados de instâncias das classes) / Classe = classificação dos tipos de objetos
# Método = Funções / Atributos = Variáveis
'''
There are four basic principles of OOP. They are encapsulation, abstraction, inheritance, and polymorphism.

- Data encapsulation is the mechanism of hiding the internal data of objects from the world. All interaction with the object and its data are performed through its public methods. 
Encapsulation allows programmers to protect the object from inconsistency.

- Data abstraction means that objects should provide the simplified, abstract version of their implementations. 
The details of their internal work usually aren't necessary for the user, so there's no need to represent them. 
Abstraction also means that only the most relevant features of the object will be presented.

- Inheritance is a mechanism for defining parent-child relationships between classes. 
Often objects are very similar, so inheritance allows programmers to reuse common logic and at the same time introduce unique concepts into the classes.

- Polymorphism literally means one name and many forms, and it concerns the inheritance of the classes. Just as the name suggests, it allows programmers to define different logic of the same method. 
So, the name (or interface) stays the same, but the actions performed may be different. In practice, it is done with overloading or overriding.

Class attributes are defined within the class but outside of any methods. Their value is the same for all instances of that class so you could consider them as the sort of "default" values for all objects.

As for the instance variables, they store the data unique to each object of the class. They are defined within the class methods, notably, within the __init__ method.
'''

class funcionario:

    num_fun = 0
    aumento = 1.04

    def __init__(self, nome, sobrenome, salario):               # Primeira instância/objeto
        self.nome = nome                                        # Atributos
        self.sobrenome = sobrenome
        self.salario = salario
        funcionario.num_fun += 1

    @property                                                   # Decodador Getter
    def email(self):
        return '{}.{}@email.com'.format(self.nome, self.sobrenome)

    @property
    def nome_completo(self):                                    # Segunda instância/objeto
        return '{} {}'.format(self.nome, self.sobrenome)        # Atributos

    @nome_completo.setter                                       # Decodador Setter
    def nome_completo(self, name):
        nome, sobrenome = name.split(' ')
        self.nome = nome
        self.sobrenome = sobrenome

    @nome_completo.deleter                                      # Decorador Deleter
    def nome_completo(self):
        self.nome = None
        self.sobrenome = None
        print("Nome deletado.")

    def aplicar_aumento(self):
        self.salario = (self.salario * self.aumento)

    @classmethod
    def aplicar_novo_aumento(cls, valor):
        cls.aumento = valor

    @classmethod
    def from_string(cls, texto):
        nome, sobrenome, salario = texto.split('-')

    @staticmethod
    def dia_util(dia):
        if dia.weekday() == 5 or dia.weekday() == 6:
            return False
        return True

class desenvolvedor(funcionario):                               # Nova classe com herança

    aumento = 1.10

    def __init__(self, nome, sobrenome, salario, ling_prog):
        super().__init__(nome, sobrenome, salario)
        self.ling_prog = ling_prog

class gerente(funcionario):                                     # Nova classe com herança

    def __init__(self, nome, sobrenome, salario, equipe = None):
        super().__init__(nome, sobrenome, salario)
        if equipe is None:
            self.equipe = []
        else:
            self.equipe = equipe

    def add_func(self, func):
        if func not in self.equipe:
            self.equipe.append(func)

    def remover_func(self, func):
        if func in self.equipe:
            self.equipe.remove(func)

    def print_funcs(self):
        for func in self.equipe:
            print('-->', func.nome_completo())

fun_1 = funcionario('Alberto', 'Silva', 7000)
fun_2 = gerente('Carla', 'Souza', 4500, [fun_1])
fun_string_1 = 'Jairo-Costa-3200-Python'
fun_string_2 = 'Marina-Velez-6400-C++'

fun_3 = desenvolvedor.from_string(fun_string_1)
fun_4 = desenvolvedor.from_string(fun_string_2)

# print(fun_1.nome_completo()) ou print(funcionario.nome_completo(fun_1)) para extrair o resultado do nome completo

import datetime

data_atual = datetime.date(2019, 5, 31)

# print(funcionario.dia_util(data_atual)) para verificar resultado da função estática

##  Notas
'''
-
-
-
'''

##  Links Úteis

https://docs.python.org/3.9/