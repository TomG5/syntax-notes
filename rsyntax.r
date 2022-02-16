#### R SYNTAX ####

##  Pacotes Relevantes
'''
1) tidyverse          |   Coleção de pacotes para: Manipulação, exploração e visualização de dados
1.1) ggplot2          |   Visualização de dados
1.2) tibble           |   Visualização de data frame limitado a 10 observações e quantas colunas couber na tela
1.3) tidyr            |   Limpeza de dados
1.4) readr            |   Importação de dados
1.5) purrr            |   Programação funcional para trabalhar funções e vetores
1.6) dplyr            |   Manipualação de dados
1.7) stringr          |   Manipulação de strings
1.8) forcats          |   Manipulação de fatores
1.9) readxl           |   Acessar arquivos Excel
1.10) googlesheets4   |   Acessar Google Sheets
1.11) jsonlite        |   Acessar arquivos JSON
1.12) xml2            |   Acessar arquivos XML
2) lubridate          |   Operações com Data/Hora
3) here               |
4) skimr              |
5) janitor            |
6) odbc/DBI           |   Conectar a bancos de dados

OBS: Para entender melhor cada pacote, utilizar a função browseVignettes("packagename")
'''

##  Tipos de Dados
'''
Character    |   Cadeia de caracteres
Integer      |   Número exclusivamente inteiro (adicionando o sufixo L)
Numeric      |   Número inteiro ou decimal
Logical      |   Valor booleano

      # Casting (Mudança de tipo)
      as.numeric()      |   Converter valor em numérico
      as.integer()      |   Converter valor em inteiro
      as.character()    |   Converter valor em caracter
      as.logical()      |   Converter valor em booleano
'''

##  Estruturas de Dados
'''
1) Vector (atomic)  |   Conjunto de dados do mesmo tipo numa sequência        |   c(x, y, z)
1.1) List           |   Conjunto de dados de qualquer tipo numa sequência     |   list("abc", 15, TRUE)
2) Data Frame       |   Tabela de dados com índices para cada observação      |   data.frame(x = c(1, 2, 3) , y = c(1.5, 5.5, 7.5))
3) Matrix           |   Matriz bi-dimensional com dados do mesmo tipo         |   matrix(c(2:7), ncol = 3, nrow = 2)
4) Array            |   Conjunto multidimensional de valores do mesmo tipo    |   array(c(1:24), dim = c(4, 3, 2)) -> 4 col, 3 lin, 2 dims
5) Factor           |   Conjunto de variáveis categóricas                     |   factor(my_vector, levels = listof_levels)

OBS: Vetores permitem nomeação de elementos via função names(myvar) <- c("Item 1", "Item 2", "Item 3")
'''

##  Definição de Variáveis
'''
Formato: nome_variavel <- valor
Exemplo:

myvar <- 15
myvar2 <- "Hello world"

OBS: Para alterar o valor de uma variável global dentro de uma função, usar o operador de atribuição <<- ao invés de <-
'''

##  Definição de Funções
'''
Formato: nome_função <- function(parâmetro1, parâmetro2 = "Valor padrão" etc.) {comandos}
Exemplos:

my_function <- function(fword) {
  print(paste("Hello", fword))
}

my_function("World!")


my_function <- function(x) {
  return (5 * x)
}
'''

##  Operadores
"
!     |   Negação
&     |   E
|     |   Ou
==    |   Igualdade
!=    |   Desigualdade
>=    |   Maior ou igual
<=    |   Menor ou igual
%%    |   Módulo
^     |   Exponenciação
:     |   Criar sequência numérica entre um e outro
%in%  |   Validar se elemento está dentro de vetor
%*%   |   Multiplicação de matrizes
"

##  Operador Pipe (realizar operações aninhadas)
"
my_dataset <- ToothGrowth %>%
  filter(dose == 0.5) %>%
  arrange(len)
""

##  Condicionais
'''
Formato: if (condição) {código} else if (condição) {código} else {código}
Exemplo:

if (x > y & x > z) {
print('X the greatest')
} else if (y > x & y > z) {
print('y the greatest')
} else {
print('z the greatest')
}
'''

##  Loopings
'''
    # While
Formato: while (condição) {comandos}
Exemplo:

i <- 1
while (i < 6) {
  print(i)
  i <- i + 1
}

    # For
Formato: for (intervalo) {comandos} 
Exemplo:

for (x in 1:10) {
  print(x)
}

OBS: Usar comandos next e break para respectivamente passar à próxima iteração ou parar o loop 
'''

##  Acesso a Elementos em Estruturas
'''
  # Data Frame
df[1]                     |     Acessar primeira coluna
df['Coluna1']             |     Acessar coluna específica
df$Coluna1                |     Acessar coluna específica
df[1, 2]                  |     Primeira linha e segunda coluna
df[2, ]                   |     Segunda linha inteira
df[, 1]                   |     Primeira coluna inteira
df[1:2]                   |     Primeira a segunda coluna
df[, -1]                  |     Desconsiderar primeira coluna
df[-1, ]                  |     Desconsiderar primeira linha
df[-1, -1]                |     Desconsiderar primeira linha e coluna

  # Vetores / Listas
  
vetor[1]                  |     Primeiro elemento
vetor[1:3]                |     Primeiro ao terceiro elemento
vetor[3:1]                |     Terceiro ao primeiro elemento
vetor[c(1, 3)]            |     Primeiro e terceiro elemento
vetor[length(objeto)]     |     último elemento

  # Matrizes
  
matriz[1, 2]              |     Primeira linha e segunda coluna
matriz[2, ]               |     Segunda linha inteira
matriz[, 1]               |     Primeira coluna inteira
matriz[1:3]               |     Primeiro ao terceiro elemento
matriz[c(1, 2)]           |     Primeiro e segundo elemento
matriz[c(1, 2),]          |     Primeira e segunda linha inteiras
matriz[, c(1, 2)]         |     Primeira e segunda coluna inteiras
matriz[-1, -1]            |     Desconsiderar primeira linha e primeira coluna
matriz[-1, ]              |     Desconsiderar primeira linha
matriz[, -1]              |     Desconsiderar primeira coluna

  # Arrays
array[2,3,2]              |     Segunda linha e terceira coluna em segunda dimensão
array[2,,1]               |     Segunda linha e todas as colunas em primeira dimensão
array[,3,2]               |     Todas as linhas e terceira coluna em segunda dimensão
array[2,3,2]              |     Segunda linha e terceira coluna em segunda dimensão
'''

##  Funções Padrões
'''
    # Matemáticas:

base.min()         |   Retornar o valor mínimo                                                             |   min(atributo)
base.max()         |   Retornar o valor máximo                                                             |   max(atributo)
base.mean()        |   Retornar o valor médio                                                              |   mean(atributo)
stats.median()     |   Retornar o valor mediano                                                            |   median(atributo)
base.sqrt()        |   Retornar a raiz quadrada                                                            |   sqrt(valor)
stats.quantile()   |   Retornar o quantil ou os quartis dos dados (usar parâmetro opcional para quantil)   |   quantile(atributo, 0.75)
base.ceiling()     |   Arredondar valor para baixo                                                         |   ceiling(valor)
base.floor()       |   Arredondar valor para cima                                                          |   floor(valor)
base.abs()         |   Remover sinal                                                                       |   abs(valor)

    # Caracteres:

base.paste()       |   Concatenar valores em uma string                      |   paste('O valor é', 5)
base.cat()         |   Concatenar e printar string sem escape characters     |   cat('Minha string separada', sep=' ')
base.nchar()       |   Retornar número de caracteres                         |   nchar(meu_texto)
base.grepl()       |   Retornar booleano se substring existe em string       |   grepl('X', 'Meu texto sem X')

          # Escape Character
          \   Backslash             |   Habilitar caracter seguinte
          \n	New Line              |   Continuar em nova linha
          \r	Carriage Return       |   Continuar em nova linha
          \t	Tab                   |   Adicionar espaçamento com tab

    # Datas:

lubridate.today()           |   Retornar dia atual
lubridate.now()             |   Retornar dia e hora atual UTC
lubridate.ymd()             |   Gerar data em formato yyyy-mm-dd               | ymd("2021-01-02")
lubridate.mdy()             |   Gerar data em formato yyyy-mm-dd
lubridate.dmy()             |   Gerar data em formato yyyy-mm-dd
lubridate.dmy_hms()         |   Gerar data/hora em formato yyyy-mm-dd hh:mm:ss UTC
lubridate.as_date()         |   Converter data/hora em data
'''

##  Funções Analíticas
'''

    # Importação de Dados

utils.data()            |   Acessar lista de data sets contidos na instalação do R        |   data()
readr.read_csv()        |   Acessar arquivo CSV                                           |   read_csv(arquivo)
readr.read_tsv()        |   Acessar arquivo TSV                                           |   read_tsv(arquivo)
readr.read_delim()      |   Acessar arquivo com delimitador específico                    |   read_delim(arquivo)
readr.read_log()        |   Acessar arquivo LOG                                           |   read_log(arquivo)
readxl.read_excel()     |   Acessar arquivos Excel                                        |   read_excel(arquivo, sheet = 'abc') sheet opcional
gs4.read_sheet()        |   Acessar Google Sheets                                         |   read_sheet('caminho online')
jsonlite.fromJSON()     |   Acessar arquivo JSON                                          |   fromJSON(arquivo)
xml2.read_xml()         |   Acessar XML                                                   |   read_xml()

          # Bancos de Dados

          library(DBI)
          con <- dbConnect(odbc::odbc(),
            driver = 'My Driver',
            database = 'test_db',
            uid = 'userid',
            pwd = 'password',
            host = 'localhost',
            port = 5432)
          odbc_result <- dbReadTable(odbc, 'tablename')
          dbGetQuery(con, 'SELECT speed, dist FROM cars')
          
          OBS: Drivers -> ODBC Driver 17 for SQL Server / PostgreSQL Unicode(x64) / RMariaDB / bigrquery / 

    # Visão Geral dos Dados
    
base.class()            |   Retornar classe de dado/estrutura                         |   class(objeto)
base.typeof()           |   Retornar tipo de dado/estrutura                           |   typeof(objeto)
utils.str()             |   Retornar resumo da(s) classe(s) do dado/estrutura         |   str(objeto)
base.summary()          |   Sumarizar algumas métricas estatísticas básicas           |   summary(objeto)
dplyr.glimpse()         |   Obter breve resumo horizontal do data frame               |   glimpse(df)
base.rownames()         |   Obter lista de nomes das observações do data frame        |   rownames(df)
base.colnames()         |   Obter lista de nomes das colunas do data frame            |   colnames(df)
utils.head()            |   Acessar primeiros n elementos                             |   head(objeto, n = 1)
utils.tail()            |   Acessar últimos n elementos                               |   tail(objeto, n = 1)
base.length()           |   Retornar quantidade de elementos na estrutura             |   length(objeto)
base.ncol()             |   Retornar quantidade de colunas                            |   ncol(objeto)
base.nrow()             |   Retornar quantidade de linhas                             |   nrow(objeto)
base.dim()              |   Retornar dimensões de uma estrutura (lin, col, dim)       |   dim(objeto)

    # Tratamento de Dados

dplyr.mutate()          |   Adicionar coluna a um data frame                                                  |   mutate(col2 = col1 * 2)
tidyr.separate()        |   Separar caracteres de uma coluna em múltiplas colunas                             |   separate(col1, c('col2', 'col3'),  sep='/' )
tidyr.unite()           |   Unir colunas em uma só (com separador de valores)                                 |   unite(new_col, c('col1', 'col2'), sep = "-")
dplyr.rename_with()     |   Renomear colunas conforme função                                                  |   rename_with(df, toupper ou tolower)
dplyr.rename()          |   Renomear coluna                                                                   |   rename(df, new = old)
tidyr.drop_na()         |   Remover observações que tenham valores em branco                                  |   drop_na(df, col1)
tidyr.fill()            |   Substituir valores faltantes com o valor anterior e/ou próximo                    |   fill(df, col1, .direction = 'updown')
tidyr.replace_na()      |   Substituir valores faltantes com um determinado valor                             |   replace_na(df, list(x = 0, y = 'abc'))
base.rep()              |   Repetir elementos da estrutura, de forma ordenada (each) ou consecutiva (times)   |   rep(c(1,2,3), times = 3)
base.seq()              |   Criar sequência numérica com step                                                 |   seq(0, 100, by = 20)
base.append()           |   Adicionar item ao final de uma lista                                              |   append(minha_lista, 123)
base.rbind()            |   Adicionar linha à dataframe/matriz                                                |   rbind(objeto, c(1, 2, 3))
base.cbind()            |   Adicionar coluna à dataframe/matriz                                               |   cbind(objeto, c(2, 3, 3))

    # Análise de Dados

base.sort()             |   Ordenar os elementos de vetor ou fator (padrão é crescente)                       |   sort(objeto, decreasing = TRUE)
dplyr.arrange()         |   Ordenar os elementos de data frame (padrão é ascendente)                          |   arrange(df, desc(col1))

which()       |   Retornar índices das observações que atendem condição                             |   which(df['Coluna1'] > 250)
which.min()   |   Retornar índice da observação com menor valor                                     |   which.min(df['Coluna1'])
which.max()   |   Retornar índice da observação com maior valor                                     |   which.max(df['Coluna1'])
arrange()         |   Ordenar resultados
select()          |   Selecionar colunas do dataframe
filter()          |   Filtrar valores conforme condição no data frame                                     |   filter(df, df$col1 == 'Valor')
group_by()        |   Agrupar valores conforme coluna                                                     |   group_by(col1)
summarize()       |   Gerar data frame com o resultado de sumarizações                                    |   summarize(new_col = mean(col1))
pivot_longer()    |   Pivotar colunas em linhas
pivot_wider()     |   Pivotar linhas em colunas
dplyr.slice_sample()    |   Extrair amostra de data frame ('n' casos ou 'prop' proporção %)       |   slice_sample(df, n = 5, replace = TRUE)
'''

##  Manipulação de diretórios/arquivos
'''
dir.create('minha-pasta')                       |   Criar diretório
file.create('meu-arquivo.csv')                  |   Criar arquivo
file.copy('meu-arquivo.csv', 'minha-pasta')     |   Copiar arquivo
unlink('meu-arquivo.csv')                       |   Deletar arquivo
'''

##  Notas
'''
- R é case-sensitive, portanto, nomes de variáveis, funções e pacotes devem seguir o padrão definido
- Índices começam em 1
'''

##  Links
https://www.rdocumentation.org/
https://www.tidyverse.org/packages/
