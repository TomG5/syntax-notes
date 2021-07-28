//  Tipos de dados básicos

string          : Dados textuais de tamanho dinâmico / “Olá, mundo”
bytes*          : Dados textuais de tamanho fixo gravados em hexadecimal / "a" => 61
bool            : Verdadeiro ou falso / true ou false
int**           : Número inteiro, positivo ou negativo / -123
uint**          : Número inteiro e positivo / 1462
fixed/ufixed    : Número com decimal / 3,296 (ainda não implementado)
address         : Endereço de carteira de criptoativos / 0xa09f2562ga097o036cv
address payable : Endereço recebível de fundos / 0xa09f2562ga097o036cv
enum            : LIsta de opções representando índices até 256 / {GoStraight, Reverse, Still}

*Varia conforme limitação de 'bytes'
**Varia conforme limitação de 'bits'
***Strings não permitem adição, busca ou mensuração do tamanho de caracteres
****Codificação de caracteres fora do alfabeto ASCII precisa da keyword unicode prévio ao texto

//  Tipos de dados referênciais

"fixed array"   : Lista de dados de um único tipo com quantidade fixa / int[3] = [1, 2, 3];
"dynamic array" : Lista de dados de um único tipo com quantidade variável / int[] = [1, 2, 3, 4];
mapping         : Coleção de pares de chaves e valores (tipo único) / 
    mapping(address => bool) voters;
        voters[msg.sender] = true;

struct          : Coleção de valores de diferentes tipos / 
    struct Car {string Modelo; int16 Ano};
    Car[] public myCars;
    Car memory myCars = Car({Modelo: Modelo, Ano: Ano});

OBS: Alterar o tamanho de textos/números em variáveis dentro de structs pode enconomizar em custo de gas transacional

//  Definição de constante

Tipo de dado + 'constant' + Tipo de Constante (Pública ou Privada) + Nome + Valor

string constant public message = "Hello World";

//  Definição de imutável

Tipo de dado + 'immutable' + Tipo de Imutável (Pública ou Privada) + Nome + Valor (opcional)

address immutable public owner = "0xlar12521l5g21kl5gl12";

*Este tipo de valor uma vez atribuído se torna imutável no deploy do contrato

//  Definição de variável

Tipo de dado + Tipo de Variável (Pública ou Privada) + Nome

string public message;
bool answer;
uint public my_age;

*Variáveis públicas geram automaticamente uma função "Getter" (que retorna seu valor) e podem ser acessadas por qualquer um, ao contrário das privadas

//  Tipos de variáveis

State = Definidas a nível de contrato, são armazenadas permanentemente e custam elevado gas
Local = Definidas a nível de função, sendo utilizadas apenas durante o período de execução sem custo

//  Data Holders

Storage = Mantém dados entre chamadas de funções, armazendo a variável no mesmo espaço que a referência (geralmente usado para variáveis/constantes State)
Memory = Mantém dados temporariamente, armazenando variáveis referenciais como uma cópia independente da referência (geralmente usado para variáveis/constantes Local)

int[] storage sameNumbers = numbers;
int[] memory myNumbers = numbers;

//  Variáveis globais

msg = refere-se "mensageiro" que iniciou o contrato ou operação. Possui funções como: sender, value (wei) e data
gasleft() = refere-se ao gas residual do processamento da transação
address(this) = refere-se ao endereço do contrato e suas propriedades. Possui funções como balance (saldo)
block = refere-se a informações de um dado bloco da blockchain. Possui funções como: number, difficulty, gaslimit, timestamp
tx = refere-se a uma dada transação. Possui funções como: origin (quem iniciou) e gasprice
selfdestruct(address payable recipient) = destrói o contrato e envia seus fundos para um dado endereço

//  Definição de função

Keyword + Nome(opcional / Tipo de Input + Parâmetro) + Tipo de Função (Pública ou Privada) + Tipo de Retorno (opcional / tipo do dado)

function Owner() public {
    manager = msg.sender;  'Registrar carteira de quem iniciou o contrato'
}

    // Função do tipo 'Setter' (modifica dados)

function Owner() public {
    manager = msg.sender;  'Registrar carteira de quem iniciou o contrato'
}

    // Função do tipo 'Getter' (não modifica dados)

function GetName(string Name) public view returns (string) {
		return name; 'Retornar variável inputada pelo usuário'
}

    // Função do tipo 'Pure' (não lê nem modifica dados do contrato)

function getResult(uint a, uint b) public pure returns(uint sum) {
      sum = a + b;
}

    // Modificador de função para ser executado sempre que chamado em alguma função, diminuindo repetições

modifier Restriction() {  
    require(msg.sender == manager); 'Limitar função ao "dono" do contrato'
    _;
}

OBS: Modifiers podem receber parâmetros (sendo passados na implementação pelo uso dos inputs da própria função)

//  Visibilidade de funções e variáveis

public = acessível interna e externamente por todos (padrão para funções)
private = restritos ao contrato onde são definidos, acessíveis somente por uma função 'Getter' (padrão para variável state)
internal = limitação de funções ao próprio contrato e seus derivados
external = limitação de funções a outros contratos e endereços externos

//  Operadores

!  : Negação
&& : E
|| : Ou
== : Igualdade
!= : Desigualdade
>= : Maior ou igual
<= : Menor ou igual
%  : Módulo
** : Exponenciação

//  Condicionais

if(condition) {
    code;
} else if(condition2) {
    code2;
} else {
    code3;
}

//  Loops

    // While

Keyword + (condição) + { código }

while (condição) {
    código;
}

    // For

Keyword + (iterador; condição; mudança iterador) + { código }

for (uint i = 0; i < maxcounter; i++) {
    código;
}

//  Manipulação de Arrays

array.length = tamanho
array.push = adição de elemento
array.pop = remover último elemento

// Retorno de valores

function multipleReturns() internal returns(uint a, uint b, uint c) {
  return (1, 2, 3);
}
    // Atribuição múltipla
function processMultipleReturns() external {
  uint a;
  uint b;
  uint c;
  (a, b, c) = multipleReturns();
}

    // Retorno individual
function getLastReturnValue() external {
  uint c;
  (,,c) = multipleReturns();
}

//  Eventos

Eventos registram movimentações do contrato via logs, acessíveis apenas por clientes externos de alguma aplicação

    // Declarador

event Payment(address indexed sender, uint value, string message);

    // Executor

emit Payment(address indexed msg.sender, uint msg.value, string myMessage);

OBS: indexed serve para possibilitar a pesquisa/filtragem de valores específicos nos parâmetros registrados pelo evento no log

//  Implementações Opcionais

    // Herança

contract Base {
    function foo() virtual external view {}
}

contract Middle is Base {}

contract Inherited is Middle {
    function foo() override public pure {}
}

OBS: A keyword virtual permite a alteração da função em contrato derivado via override, podendo substituir a visibilidade por public ou o tipo para pure

    // Contratos abstratos

Contratos abstratos não são implementados na blockchain, servindo apenas de referência para seus derivados contendo ao menos uma função não implementada (sem ações)

abstract contract A {
    function calculator() public view returns(uint) {}
}

contract B is A {
    function calculator() public view returns(uint) {
        uint a = 5;
        uint b = 6;
        return a + b; 
    }
}

OBS: Caso o derivado não implemente a função, deverá ser marcado também como abstrato

    // Interfaces

Interfaces são tipos de contratos sem variáveis e com apenas funções externas não implementadas, devendo sofrer override nos contratos derivados

interface Calculator {
   function getResult() external view returns(uint);
}
contract Test is Calculator {
   function getResult() override external view returns(uint){
      uint a = 1; 
      uint b = 2;
      return a + b;
   }
}

OBS: Funções em interfaces são implicitamente virtual

//  Compilação

A compilação de código Solidity exporta dois tipos de resultados: ABI (Abstract Binary Interface) e Bytecode

ABI = Método de comunicação de outras aplicações/linguagens com o Smart Contract
Bytecode = Código fonte do contrato transformado em formato inteligível pela Ethereum Virtual Machine (Opcodes)

//  Notas

- Para um contrato receber Ether, o mesmo deve possuir as funções receive() e fallback() ou possuir uma função própria para o envio de moedas
- Para evitar ataques de saques em looping, deve-se alterar o estado do contrato antes de enviar os fundos e usar a função transfer
- Em Structs, não é necessário inicializar dados do tipo referencial
- Em Mappings, o tempo de busca é constante, ao contrário de Arrays
- Mappings são sempre salvos em storage;

//  Links úteis

https://docs.soliditylang.org/en/latest/index.html
https://docs.chain.link/docs/get-a-random-number/