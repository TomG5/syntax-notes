//// C SYNTAX ////

//  Bibliotecas
'''
#include <stdio.h>      |   Standard Input-Output
#include <stdlib.h>     |   String conversion, Memory Allocation and Pseudo Random
#include <string.h>     |   Manipulation of Character Arrays
#include <ctype.h>      |   Testing and Mapping Characters
#include <stdbool.h>    |   Utilize boolean values
'''

//  Tipos de Dados
'''
bool                |   1 byte      |   true or false
char	            |   1 byte	    |   -128 to 127 or 0 to 255
unsigned char	    |   1 byte	    |   0 to 255
signed char	        |   1 byte	    |   -128 to 127
int	                |   2/4 bytes	|   -32,768 to 32,767 or -2,147,483,648 to 2,147,483,647
unsigned int	    |   2/4 bytes	|   0 to 65,535 or 0 to 4,294,967,295
short               |   2 bytes     |   -32,768 to 32,767
unsigned short      |   2 bytes     |   0 to 65,535
long	            |   4/8 bytes   |   -9223372036854775808 to 9223372036854775807
unsigned long	    |   8 bytes     |	0 to 18446744073709551615

float	            |   4 bytes     |   6 decimal places
double	            |   8 bytes     |   15 decimal places
long double         |   10 bytes    |   19 decimal places

    // Casting (Mudança de tipo)

sum_var = (float) x + (float) y;

    // Formatos de Saída (Mais comuns)

%c      |   Char
%f      |   Float
%lf     |   Double
%i      |   Integer
%li     |   Long Integer
%x      |   Hexadecimal
%s      |   String
%p      |   Address
'''

//  Estruturas de Dados
'''
Array       |   Grupo de n valores do mesmo tipo na mesma variável                                    |   int my_var[n] = {1, 2, 3, n};
Linked List |   Grupo de valores do mesmo tipo na mesma variável sem uma ordenação lógica na memória  |   Exemplo abaixo*

#include <stdio.h>
#include <stdlib.h>
 
// Representação de um nó

typedef struct node
{
    int number;
    struct node *next;
}
node;
 
int main(void)
{
    // Iniciação de lista com tamanho 0

    node *list = NULL;
 
    // Adicionar item na lista

    node *n = malloc(sizeof(node));
    if (n == NULL)
    {
        return 1;
    }
    n->number = 1;
    n->next = NULL;
    list = n;
 
    // Adicionar item na lista
    
    n = malloc(sizeof(node));
    if (n == NULL)
    {
        free(list);
        return 1;
    }
    n->number = 2;
    n->next = NULL;
    list->next = n;
 
    // Adicionar item na lista

    n = malloc(sizeof(node));
    if (n == NULL)
    {
        free(list->next);
        free(list);
        return 1;
    }
    n->number = 3;
    n->next = NULL;
    list->next->next = n;
 
    // Printar lista

    for (node *tmp = list; tmp != NULL; tmp = tmp->next)
    {
        printf("%i\n", tmp->number);
    }
 
    // Limpar lista
    
    while (list != NULL)
    {
        node *tmp = list->next;
        free(list);
        list = tmp;
    }
    return 0;
}
'''

//  Definição de Variáveis
'''
Formato: < tipo de dado + nome_variavel >
Exemplo:

int idade;
char letra = 'A';
unsigned long id = 91249102471209;
float my_var, that_var;
'''

//  Definição de Constantes
'''
Formato: < const + tipo de dado + nome_variavel >
Exemplo:

const int total = 5;
'''

//  Definição de Funções
'''
Formato: < tipo de saída + nome_funcao(argumentos) {comandos} >
Exemplo:

#include <stdio.h>

int main(void) 
{
    int my_num;
    scanf("%d", &my_num);
    printf("Seu numéro dobrado é %i\n", my_num * 2);
    return 1;
}

----
int main() 
{
    char* name = "Joe";
    for (int c = 0, n = strlen(name); c < n; c++)
    {
        printf("%c\n", name[c]);
    }
}
-----

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{   
    int result = atoi(argv[1]) * atoi(argv[2]);
    printf("%i\n", result);
    return result;
}
----
#include <stdio.h>

int main(void)
{
    int n = 50;
    int *x = &n;        // Pointer
    printf("%p\n", x);
    printf("%i\n", *x)
}


OBS: keyword "void" pode ser usada para indicar ausência de saída ou de argumentos 
'''

// Definição de Novos Tipos de Dados (Structs)
'''
Formato: < typedef + struct {tipo de dado + nome do dado} nome_novotipo >
Exemplo:

typedef struct 
{
    char* name;
    float height;
} 
person;

person people[2];

people[0].name = "Joe";
people[0].number = 1.85;
'''


//  Operadores
'''
!       |   Negação
&&      |   E
||      |   Ou
==      |   Igualdade
!=      |   Desigualdade
>=      |   Maior ou igual
<=      |   Menor ou igual
%       |   Módulo
**      |   Exponenciação

&       |   Retornar endereço na memória
*       |   Acessar endereço na memória
'''

//  Condicionais
'''
Formato 1: < if (condição) {comandos} >
Exemplo:

if (x < y)
{
    printf("X is smaller than Y\n");
}
else if (x == y)
{
    printf("X is equal to Y\n");
}
else
{
    printf("X is greater than Y\n");
}

Formato 2: < switch(x) {case {valor}: {comandos}} >
Exemplo:

switch(my_guess)
{
    case 1:
        printf("You are right!\n");
        break;
    case 2:
        printf("You are wrong!\n");
        break;
    default:
        printf("Not a valid guess.\n");
}

Formato 3: < var = (condição) ? {comandos se verdadeiro} : {comandos se falso} >
Exemplo:

int main() 
{
    char* x = (15 > 5) ? "Yes" : "No";
    printf("True or false: %s \n", x);
}
'''

//  Loopings
'''
    // While:

Formato: < while (condição) {comandos} >
Exemplo:

int counter = 0;

while (counter < 10)
{
    *** comandos ***
}

    // Do While:

Formato: < do {comandos} while (condição) >
Exemplo:

int counter = 0;

do
{
    counter += 1;
}

while (counter < 10);

    // For:

Formato: < for (iterador; condição; incrementador) {comandos} >
Exemplo:

for (int i = 0; i < 10; i++)
{
    *** comandos ***
}
'''

// Alocação de Memória
'''
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    // Usar malloc para alocar espaço suficiente para um array com 3 inteiros

    int *list = malloc(3 * sizeof(int));
    if (list == NULL)
    {
        return 1;
    }

    // Definir os valores do array
    
    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    // Para salvar um valor adicional, é necessário alocar mais memória
    
    int *tmp = malloc(4 * sizeof(int));
    if (tmp == NULL)
    {
        free(list);
        return 1;
    }

    // Copiar a lista de tamanho 3 para a de 4
    
    for (int i = 0; i < 3; i++)
    {
        tmp[i] = list[i];
    }

    // Adicionar novo valor à lista
    tmp[3] = 4;

    // Liberar memória da lista original
    free(list);

    // Reatribuir valores à lista original

    list = tmp;

    // Printar lista

    for (int i = 0; i < 4; i++)
    {
        printf("%i\n", list[i]);
    }

    // Liberar memória da nova lista
    free(list);
}
'''

// Notas
'''
- Para sequências de caracteres, utilizar "", para caracteres individuais, apenas ''
- Strings são encerradas na leitura da memória com o caracter nulo ''\0''
- Um Pointer é uma variável que carrega o endereço de um dado valor
'''

// Links

https://manual.cs50.io/