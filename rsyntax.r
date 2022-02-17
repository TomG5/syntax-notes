#### R SYNTAX ####

##  Pacotes Relevantes
'''
1) tidyverse          |   Cole��o de pacotes para: Manipula��o, explora��o e visualiza��o de dados
1.1) ggplot2          |   Visualiza��o de dados
1.2) tibble           |   Gera��o de vers�o simplificada de um data frame (denom. tibble)
1.3) tidyr            |   Manipula��o e limpeza de dados
1.4) readr            |   Importa��o de dados
1.5) purrr            |   Programa��o funcional para trabalhar fun��es e vetores
1.6) dplyr            |   Manipula��o de dados
1.7) stringr          |   Manipula��o de strings
1.8) forcats          |   Manipula��o de fatores
1.9) readxl           |   Acessar arquivos Excel
1.10) googlesheets4   |   Acessar Google Sheets
1.11) jsonlite        |   Acessar arquivos JSON
1.12) xml2            |   Acessar arquivos XML
2) lubridate          |   Opera��es com Data/Hora
3) skimr              |   Sum�rios estat�sticos sobre estutruras de dados
4) janitor            |   Limpeza de dados
5) odbc/DBI           |   Conectar a bancos de dados

OBS: Para entender melhor cada pacote, utilizar a fun��o browseVignettes("packagename")
'''

##  Tipos de Dados
'''
Character    |   Cadeia de caracteres
Integer      |   N�mero exclusivamente inteiro (adicionando o sufixo L)
Numeric      |   N�mero inteiro ou decimal
Logical      |   Valor booleano

      # Casting (Mudan�a de tipo)
      as.numeric()      |   Converter valor em num�rico
      as.integer()      |   Converter valor em inteiro
      as.character()    |   Converter valor em caracter
      as.logical()      |   Converter valor em booleano
'''

##  Estruturas de Dados
'''
1) Vector (atomic)  |   Conjunto de dados do mesmo tipo numa sequ�ncia        |   c(x, y, z)
1.1) List           |   Conjunto de dados de qualquer tipo numa sequ�ncia     |   list("abc", 15, TRUE)
2) Data Frame       |   Tabela de dados com �ndices para cada observa��o      |   data.frame(x = c(1, 2, 3) , y = c(1.5, 5.5, 7.5))
3) Matrix           |   Matriz bi-dimensional com dados do mesmo tipo         |   matrix(c(2:7), ncol = 3, nrow = 2)
4) Array            |   Conjunto multidimensional de valores do mesmo tipo    |   array(c(1:24), dim = c(4, 3, 2)) -> 4 col, 3 lin, 2 dims
5) Factor           |   Conjunto de valores categ�ricos                       |   factor(my_vector, levels = listof_levels)

OBS: Vetores permitem nomea��o de elementos via fun��o names(myvar) <- c("Item 1", "Item 2", "Item 3")
'''

##  Defini��o de Vari�veis
'''
Formato: nome_variavel <- valor
Exemplo:

myvar <- 15
myvar2 <- "Hello world"

OBS: Para alterar o valor de uma vari�vel global dentro de uma fun��o, usar o operador de atribui��o <<- ao inv�s de <-
'''

##  Defini��o de Fun��es
'''
Formato: nome_fun��o <- function(par�metro1, par�metro2 = "Valor padr�o" etc.) {comandos}
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
!     |   Nega��o
&     |   E
|     |   Ou
==    |   Igualdade
!=    |   Desigualdade
>=    |   Maior ou igual
<=    |   Menor ou igual
%%    |   M�dulo
^     |   Exponencia��o
:     |   Criar sequ�ncia num�rica entre um e outro
%in%  |   Validar se elemento est� dentro de vetor
%*%   |   Multiplica��o de matrizes
"

##  Operador Pipe (realizar opera��es aninhadas)
"
my_dataset <- ToothGrowth %>%
  filter(dose == 0.5) %>%
  arrange(len)
""

##  Condicionais
'''
Formato: if (condi��o) {c�digo} else if (condi��o) {c�digo} else {c�digo}
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
Formato: while (condi��o) {comandos}
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

OBS: Usar comandos next e break para respectivamente passar � pr�xima itera��o ou parar o loop 
'''

##  Acesso a Elementos em Estruturas
'''
  # Data Frame
df[1]                     |     Acessar primeira coluna
df['Coluna1']             |     Acessar coluna espec�fica
df$Coluna1                |     Acessar coluna espec�fica
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
vetor[length(objeto)]     |     �ltimo elemento

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
array[2,3,2]              |     Segunda linha e terceira coluna em segunda dimens�o
array[2,,1]               |     Segunda linha e todas as colunas em primeira dimens�o
array[,3,2]               |     Todas as linhas e terceira coluna em segunda dimens�o
array[2,3,2]              |     Segunda linha e terceira coluna em segunda dimens�o
'''

##  Fun��es Padr�es
'''
    # Matem�ticas:

base.min()         |   Retornar o valor m�nimo                                                             |   min(atributo)
base.max()         |   Retornar o valor m�ximo                                                             |   max(atributo)
base.mean()        |   Retornar o valor m�dio                                                              |   mean(atributo)
stats.median()     |   Retornar o valor mediano                                                            |   median(atributo)
base.sqrt()        |   Retornar a raiz quadrada                                                            |   sqrt(valor)
stats.quantile()   |   Retornar o quantil ou os quartis dos dados (usar par�metro opcional para quantil)   |   quantile(atributo, 0.75)
base.ceiling()     |   Arredondar valor para baixo                                                         |   ceiling(valor)
base.floor()       |   Arredondar valor para cima                                                          |   floor(valor)
base.abs()         |   Remover sinal                                                                       |   abs(valor)

    # Caracteres:

base.paste()       |   Concatenar valores em uma string                      |   paste('O valor �', 5)
base.cat()         |   Concatenar e printar string sem escape characters     |   cat('Minha string separada', sep=' ')
base.nchar()       |   Retornar n�mero de caracteres                         |   nchar(meu_texto)
base.grepl()       |   Retornar booleano se substring existe em string       |   grepl('X', 'Meu texto sem X')

          # Escape Character
          
          \   Backslash             |   Habilitar caracter seguinte
          \n	New Line              |   Continuar em nova linha
          \r	Carriage Return       |   Continuar em nova linha
          \t	Tab                   |   Adicionar espa�amento com tab

    # Datas:

lubridate.today()           |   Retornar dia atual                                      |   today()
lubridate.now()             |   Retornar dia e hora atual UTC                           |   now()
lubridate.year()            |   Retornar ano de data                                    |   year('2021-01-02')
lubridate.month()           |   Retornar m�s de data                                    |   month('2021-01-02')
lubridate.day()             |   Retornar dia de data                                    |   day('2021-01-02')
lubridate.wday()            |   Retornar dia da semana                                  |   wday(date, locale = 'US', label = TRUE)
lubridate.ymd()             |   Gerar data em formato yyyy-mm-dd                        |   ymd('2021-01-02')
lubridate.mdy()             |   Gerar data em formato yyyy-mm-dd                        |   mdy('04/14/2019')
lubridate.dmy()             |   Gerar data em formato yyyy-mm-dd                        |   dmy('25/02/2021')
lubridate.ymd_hms()         |   Gerar data/hora em formato yyyy-mm-dd hh:mm:ss UTC      |   ymd_hms('2010-12-13 15:30:30')
lubridate.as_date()         |   Converter data/hora em data                             |   as_date('2021-01-02')
'''

##  Fun��es Anal�ticas
'''

    # Importa��o de Dados

utils.data()            |   Acessar lista de data sets contidos na instala��o do R        |   data()
readr.read_csv()        |   Acessar arquivo CSV                                           |   read_csv(arquivo)
readr.read_tsv()        |   Acessar arquivo TSV                                           |   read_tsv(arquivo)
readr.read_delim()      |   Acessar arquivo com delimitador espec�fico                    |   read_delim(arquivo)
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

    # Vis�o Geral dos Dados
    
utils.View()            |   Visualizar data frame                                     |   View(df)
base.class()            |   Retornar classe de dado/estrutura                         |   class(objeto)
base.typeof()           |   Retornar tipo de dado/estrutura                           |   typeof(objeto)
utils.str()             |   Retornar resumo da(s) classe(s) do dado/estrutura         |   str(objeto)
base.summary()          |   Sumarizar algumas m�tricas estat�sticas b�sicas           |   summary(objeto)
skimr.skim()            |   Sum�rio estat�stico sobre estrutura de dados              |   skim(objeto)
dplyr.glimpse()         |   Obter breve resumo horizontal do data frame               |   glimpse(df)
base.rownames()         |   Obter lista de nomes das observa��es do data frame        |   rownames(df)
base.colnames()         |   Obter lista de nomes das colunas do data frame            |   colnames(df)
utils.head()            |   Acessar primeiros n elementos                             |   head(objeto, n = 1)
utils.tail()            |   Acessar �ltimos n elementos                               |   tail(objeto, n = 1)
base.length()           |   Retornar quantidade de elementos na estrutura             |   length(objeto)
base.ncol()             |   Retornar quantidade de colunas                            |   ncol(objeto)
base.nrow()             |   Retornar quantidade de linhas                             |   nrow(objeto)
base.dim()              |   Retornar dimens�es de uma estrutura (lin, col, dim)       |   dim(objeto)
janitor.tabyl()         |   Gerar tabela de frequ�ncias sobre vetor                   |   tabyl(df, col1)

    # Tratamento de Dados

tibble.as_tibble()      |   Convers�o de data frame para tibble, possibilitando print simplificado            |   as_tibble(df)
dplyr.case_when()       |   Retornar valor conforme condicional                                               |   case_when(x > y ~ 'Case1', y > z ~ 'Case2', TRUE ~ 'Other')
dplyr.mutate()          |   Adicionar coluna a um data frame                                                  |   mutate(col2 = col1 * 2)
tidyr.separate()        |   Separar caracteres de uma coluna em m�ltiplas colunas                             |   separate(col1, c('col2', 'col3'),  sep='/' )
tidyr.extract()         |   Separar caracteres de uma coluna em m�ltiplas colunas via regex                   |   extract(df, col1, c('c2', 'c3'),  regex = '([abc])')
tidyr.unite()           |   Unir colunas em uma s� (com separador de valores)                                 |   unite(new_col, c('col1', 'col2'), sep = "-")
dplyr.rename_with()     |   Renomear colunas conforme fun��o                                                  |   rename_with(df, toupper ou tolower)
dplyr.rename()          |   Renomear coluna                                                                   |   rename(df, new = old)
janitor.clean_names()   |   Padronizar nomes das colunas em formato universal                                 |   clean_names(df)
janitor.remove_empty()  |   Remover linhas ou colunas sem valores                                             |   remove_empty(df, which = 'rows' / 'cols')
tidyr.drop_na()         |   Remover observa��es que tenham valores em branco                                  |   drop_na(df, col1)
tidyr.fill()            |   Substituir valores faltantes com o valor anterior e/ou pr�ximo                    |   fill(df, col1, .direction = 'updown')
tidyr.replace_na()      |   Substituir valores faltantes com um determinado valor                             |   replace_na(df, list(x = 0, y = 'abc'))
janitor.get_dupes()     |   Retornar valores duplicados em coluna                                             |   get_dupes(df, col1)
base.rep()              |   Repetir elementos da estrutura, de forma ordenada (each) ou consecutiva (times)   |   rep(c(1,2,3), times = 3)
base.seq()              |   Criar sequ�ncia num�rica com step                                                 |   seq(0, 100, by = 20)
base.append()           |   Adicionar item ao final de uma lista                                              |   append(minha_lista, 123)
base.rbind()            |   Adicionar linha � dataframe/matriz                                                |   rbind(objeto, c(1, 2, 3))
base.cbind()            |   Adicionar coluna � dataframe/matriz                                               |   cbind(objeto, c(2, 3, 3))
stringr.str_detect()    |   Retornar booleano sobre exist�ncia de substring em string/elementos               |   str_detect(objeto, coll('abc'))
stringr.str_count()     |   Retornar contagem de substring em string ou elementos de estrutura                |   str_count(objeto, coll('a'))
stringr.str_subset()    |   Retornar rela��o de elementos que possuem substring                               |   str_subset(objeto, coll('A'))
stringr.str_locate()    |   Retornar posi��o de substring em cada string                                      |   str_locate(objeto, coll('im'))
stringr.str_replace()   |   Substituir substring em cada string                                               |   str_replace(objeto, coll('antigo'), 'novo')
stringr.str_split()     |   Dividir string conforme separador                                                 |   str_split(objeto, coll('x'))

    # An�lise de Dados

dplyr.summarize()       |   Gerar data frame com o resultado de sumariza��es                                  |   summarize(new_col = mean(col1))
base.sort()             |   Ordenar os elementos de vetor ou fator (padr�o � crescente)                       |   sort(objeto, decreasing = TRUE)
dplyr.arrange()         |   Ordenar os elementos de data frame (padr�o � ascendente)                          |   arrange(df, desc(col1))
base.which()            |   Retornar �ndices das observa��es que atendem condi��o                             |   which(df['Coluna1'] > 250)
base.which.min()        |   Retornar �ndice da observa��o com menor valor                                     |   which.min(df['Coluna1'])
base.which.max()        |   Retornar �ndice da observa��o com maior valor                                     |   which.max(df['Coluna1'])
dplyr.select()          |   Selecionar colunas do dataframe                                                   |   select(df, col1, col2, col3)
dplyr.filter()          |   Filtrar valores conforme condi��o no data frame                                   |   filter(df, df$col1 == 'Valor')
dplyr.group_by()        |   Agrupar valores conforme coluna                                                   |   group_by(col1)
tidyr.pivot_longer()    |   Pivotar colunas em linhas                                                         |   pivot_longer(df, cols = starts_with('Abc'), names_to = 'category_col', values_to = 'values_col')
tidyr.pivot_wider()     |   Pivotar linhas em colunas                                                         |   pivot_wider(df,   names_from = col1, values_from = col2, values_fill = 0)
dplyr.slice_sample()    |   Extrair amostra de data frame ('n' casos ou 'prop' propor��o %)                   |   slice_sample(df, n = 5, replace = TRUE)

          # Visualiza��o de Dados (ggplot2)
          
          Componentes: Dados + Aesthetic (estrutura e est�tica) + Geom (forma usada)

          ggplot(data = df) +
            geom_point(mapping = aes(x = col1, y = col2), size = 5) +                 |   Gr�fico de dispers�o
            geom_jitter(mapping = aes(x = col1, y = col2))                            |   Gr�fico de dispers�o com 'ru�do' entre pontos para melhor visualiza��o
            geom_bar(mapping = aes(x = col1),  fill = col2) +                         |   Gr�fico de barra
            geom_histogram(mapping = aes(x = col1), binwidth = 0.5) +                 |   Histograma em barras
            geom_freqpoly(mapping = aes(x = col1, colour = col2), binwidth = 0.1) +   |   Histograma em linhas
            geom_boxplot(mapping = aes(x = col1, y = col2)) +                         |   Box plot
            geom_count(mapping = aes(x = col1, y = col2)) +                           |   Rela��o entre duas vari�veis categ�ricas, por contagem
            geom_tile(mapping = aes(x = col1, y = col2, fill = col3)) +               |   Mapa de calor em teclas
            geom_density(kernel = 'gaussian', aes(col1)) +                            |   Gr�fico de distribui��o
            labs(title = 'Abc', subtitle = 'Bcd', caption = 'Cde') +                  |   Adicionar r�tulos ao gr�fico
            
              facet_wrap(~colx)                                                       |   Dividir em gr�ficos por classifica��es em coluna                 
              coord_cartesian(xlim/ylim = c(0, 50))                                   |   Focar gr�fico em intervalo de pontos nos eixos X ou Y
              coord_flip()                                                            |   Inverter eixos

    # Extra��o de Dados
    
readr.write_csv()       |   Exportar arquivo em formato CSV (separador em ,)                                  |   write_csv(df, 'dfnovo.csv')
readr.write_csv2()      |   Exportar arquivo em formato CSV (separador em ;)                                  |   write_csv2(df, 'dfnovo.csv')
utils.write.table()     |   Exportar tabela em txt (definindo separador)                                      |   write.table(df, 'dfnovo2.txt', sep = ";")
ggplot2.ggsave()        |   Exportar gr�fico em imagem                                                        |   ggsave('chart.png')
'''

##  Manipula��o de diret�rios/arquivos
'''
dir.create('minha-pasta')                       |   Criar diret�rio
file.create('meu-arquivo.csv')                  |   Criar arquivo
file.copy('meu-arquivo.csv', 'minha-pasta')     |   Copiar arquivo
unlink('meu-arquivo.csv')                       |   Deletar arquivo
'''

##  Notas
'''
- R � case-sensitive, portanto, nomes de vari�veis, fun��es e pacotes devem seguir o padr�o definido
- �ndices come�am em 1
'''

##  Links
https://www.rdocumentation.org/
https://www.tidyverse.org/packages/
