//// C SYNTAX ////

//  Bibliotecas
'''
#include <stdio.h>  |   Standard Input-Output
'''

//  Tipos de Dados
'''
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
'''

//  Estruturas de Dados
'''
Array   |   Grupo de valores do mesmo tipo na mesma variável  |   int my_var[5]

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

//  Definição de Funções
'''
Formato: < tipo de saída + nome_funcao(argumentos) {comandos} >
Exemplo:

#include <stdio.h>

int main() 
{
    int my_num;
    scanf("%d", &my_num);
    printf("Seu numéro dobrado é %i\n", my_num * 2);
    return 1;
}

OBS: keyword "void" pode ser usada para indicar ausência de saída ou de argumentos 
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

#include <stdio.h>

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

// Notas
'''
- Para sequências de caracteres, utilizar "", para caracteres individuais, apenas ''
'''