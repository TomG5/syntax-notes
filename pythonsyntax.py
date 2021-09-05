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
input()     |   Recebe entrada de dados pelo usuário                                                                            |   input() ou input('Digite o valor aqui: ')
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

update()  | Atualiza ou adiciona dados a um dicionário conforme chave   |   my_dict.update({chave: valor}) ou my_dict.update(chave = valor)
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
–   :   Diferença             # Elementos de A que não existem em B e C
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

index() |   Retorna o índice de um valor da tupla                   |   my_tuple.index(valor)
count() |   Retorna a contagem da ocorrência de um valor na tupla   |   my_tuple.count(valor)

zip()   |   Integra múltiplos objetos iteráveis com base nos índices de seus elementos  |   my_tuple = tuple(zip(obj1, obj2))
'''

##  Alguns Módulos:
'''
    ## os (Informações do Sistema)

getcwd       |   Siretório atual                        |   os.getcwd()
chdir        |   Mudar diretório                        |   os.chdir('caminho')
listdir      |   Listar pastas e arquivos do diretório  |   os.listdir()
mkdir        |   Criar pasta                            |   os.mkdir('diretório')
makedirs     |   Criar múltiplos níveis de pastas       |   os.makedirs('diretórios')
rmdir        |   Remover pasta                          |   os.rmdir('diretório')
removedirs   |   Remover múltiplos níveis de pastas     |   os.removedirs('diretórios')
rename       |   Renomear pasta ou arquivo              |   os.rename('nome antigo', 'nome novo')

    ## math (Cálculos)

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

    ## time (Período)

asctime()       |   Data e hora atual em formato textual                                    |   time.asctime()
localtime()     |   Data e hora atual                                                       |   time.localtime()
perf_counter()  |   Retorna o período atual em segundos fracionados - usado para contagens  |   time.perf_counter()
sleep()         |   Suspende determinado processo por x segundos                            |   time.sleep(segundos)

    ## datetime (Datação)

datetime()        |   Retorna datação (YY/MM/DD/HR/MIN/SEC)   |   datetime()
year()            |   Retorna o ano                           |   datetime.year()
month()           |   Retorna o mês                           |   datetime.month()
day()             |   Retorna o dia                           |   datetime.day()
weekday()         |   Retorna o índice do dia da semana       |   datetime.weekday()
now()             |   Retorna a datação atual                 |   datetime.now()

    ## random (Pseudo-Randomizações)

random()        |   Gera número aleatório entre 0.0 e 1.0                           |   random.random()
randint()       |   Gera número aleatório dentro de um range de inteiros            |   random.randint(a, b)
randrange()     |   Gera número aleatório conforme degrau em um range de inteiros   |   random.randrange(a, b, degrau)
choice()        |   Escolhe um elemento qualquer de um objeto                       |   random.choice(objeto iterável)
sample()        |   Gera amostra de itens (vindo de lista ou tupla)                 |   random.sample(pop, k)
seed()          |   Gera números aleatórios com base num código de referência       |   random.seed(valor)
shuffle()       |   Embaralha elementos de um objeto                                |   random.shuffle(objeto iterável)

    ## secret (Randomizações)

choice()        |   Gera valor aleatório dentro de uma sequência    |   secrets.choice(objeto iterável)
randbelow()     |   Gera número aleatório dentro de range           |   secrets.randbelow(valor)

    ## string (Relação de Caracteres)

ascii_letters()       |   Gera uma string com os caracteres em letra minúscula e maiúscula    |   string.ascii_letters
ascii_lowercase()     |   Gera uma string com os caracteres em letra minúscula                |   string.ascii_lowercase
ascii_uppercase()     |   Gera uma string com os caracteres em letra maiúscula                |   string.ascii_uppercase
digits()              |   Gera uma string com os números base de 0 a 9                        |   string.digits
punctuation()         |   Gera uma string com os caracteres especiais de pontuação            |   string.punctuation
'''

##  Algumas Bibliotecas:
'''
    ## matplotlib (Gerar gráficos)

pyplot   |   Gerar gráficos  |   matplotlib.pyplot()

Exemplo:

import matplotlib.pyplot as plt 'ou' from matplotlib import pyplot as plt

valores_x = [5, 4, 3, 2.5, 7]
legenda = ["JAN", "FEV", "MAR", "ABR", "MAI"]

plt.xticks([1,2,3,4,5], legenda)
plt.plot([1,2,3,4,5], valores_x)
plt.show()

    ## numpy (Gerar e gerir arrays/matrizes)

numpy.arange        |   Gerar array com base em dado range
numpy.copy          |   Copiar dados de variável/índice para outro
numpy.reshape       |   Alterar número de linhas/colunas
numpy.linspace      |   Gerar array com n número de linhas com base em range
numpy.unique        |   Retornar relação de valores únicos

    ## pandas (Gerar e gerir datasets)

pandas.DataFrame    |   Criar tabela de dados (dados, índices, colunas)
pandas.read_csv     |   Ler dados de arquivo de texto
pandas.read_excel   |   Ler dados de arquivo Excel

df.head             |   Retornar apenas x primeiras linhas da tabela
df.tail             |   Retornar apenas x últimas linhas da tabela
df.drop             |   Remover índice, coluna ou valores de uma tabela (adicionando parâmetro 'inplace=True' efetiva a mudança)

Exemplo:

import numpy as np
import pandas as pd

np.random.seed(101)

df = pd.DataFrame(np.random.randn(5, 4), index = "01 02 03 04 05".split(), columns = "A B C D".split())

df.drop('05', inplace = True)
df.drop('D', axis = 1, inplace = True)
df.head(2)

print(df)
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
Objeto/Instância = item utilizado no algoritmo composto por código + dados (objetos são chamados de instâncias das classes)
Classe = classificação dos tipos de objetos
Método = Funções / Atributos = Variáveis

There are four basic principles of OOP. They are encapsulation, abstraction, inheritance, and polymorphism.

- Data encapsulation is the mechanism of hiding the internal data of objects from the world. All interaction with the object and its data are performed through its public methods. 
Encapsulation allows programmers to protect the object from inconsistency.

- Data abstraction means that objects should provide the simplified, abstract version of their implementations. 
The details of their internal work usually aren't necessary for the user, so there's no need to represent them. 
Abstraction also means that only the most relevant features of the object will be presented.

- Inheritance is a mechanism for defining parent-child relationships between classes. 
Often objects are very similar, so inheritance allows programmers to reuse common logic and at the same time introduce unique concepts into the classes.

- Polymorphism literally means one name and many forms, and it concerns the inheritance of the classes. Just as the name suggests, it allows programmers to define different logic of the same method. 
So, the name (or interface) stays the same, but the actions performed may be different for each type of object. In practice, it is done with overloading or overriding.

Class attributes are defined within the class but outside of any methods. Their value is the same for all instances of that class so you could consider them as the sort of "default" values for all objects.

As for the instance variables, they store the data unique to each object of the class. They are defined within the class methods, notably, within the __init__ method.

Exemplo:

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
'''

##  Notas
'''
-
-
-
'''

##  Links Úteis
'''
https://docs.python.org/3.9/
'''