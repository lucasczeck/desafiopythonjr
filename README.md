# Avaliação técnica | Desenvolvedor Python

Avaliação técnica contendo 3 problemas que devem ser resolvidos utilizando a linguagem Python, ficando a utilização de 
bibliotecas, frameworks, etc ao criterio do avaliado

**Os desafios são:**

* Escreva uma função que recebe duas strings como entrada, `s1` e `s2`, e retorna quantas vezes `s2`ocorre em `s1`.


* Dois caracteres são considerados um par se o caracter de abertura (i.e. `(`, `{`, `[`) ocorre à esquerda do 
respectivo caracter de fechamento (`)`, `}`, `]`). São três tipos de pares de caracteres: `()`, `{}`, `[]`.
Um par de caracteres é válido se os caracteres que este cerca também forem pares. Caso contrário, o par não é válido.


* Desenvolva um programa que recebe como entrada uma lista de textos. Cada texto deve ser separado em sentenças e, para 
cada início de sentença, deve ser verificada a presença de alguma das expressões definidas numa lista.

------------------------------------------------

# Orientações para execução:

### Problema 1 - Identificação de substrings

* Abra a pasta onde está o projeto no terminal (você pode usar o comando CD para navegar até a pasta).
* Execute o comando **"Python"**
* Importe a função **start** usando o comando **"from Problema1 import start"**
* Execute a função de start utilizando o comando **"start()"**
* Siga os passos descritos no console

------------------------------------------------

### Problema 2 - Validação de sequência de caracteres

* Abra a pasta onde está o projeto no terminal (você pode usar o comando CD para navegar até a pasta).
* Execute o comando **"Python"**
* Importe a classe **ValidateSequence** utilizando o comando **"from Problema2 import ValidateSequence"**
* Execute a função de start utilizando o comando **"ValidateSequence().start()"**
* Siga os passos descritos no console

------------------------------------------------

### Problema 3 - Verificação de expressões em sentenças

* Abra a pasta onde está o projeto no terminal (você pode usar o comando CD para navegar até a pasta).
* Execute o comando **"Python"**
* Importe a classe **Execute** utilizando o comando **"from Problema3 import Execute"**
* É necessário ter dentro a pasta o arquivo **.txt** com a expressões desejadas no mesmo padrão do arquivo 
**expressoes.txt** que está no projeto e o arquivo **.json** com os textos no mesmo padrão do arquivo **textos.json**
que está no projeto.
* Execute a classe de execução com o comando **"Execute('textos.json', 'expressoes.txt')"**
* O arquivo **output.json** será criado dentro da pasta do projeto

------------------------------------------------

Observações e requisitos:

* É necessário possuir o Python instalado na versão 3.8.8, caso não possua siga os passos:
  * Baixe o instalador do Python para Windows a partir do site oficial do Python. Você pode acessar o link 
  diretamente aqui: https://www.python.org/downloads
  * Abra o arquivo de instalação que você acabou de baixar. Você pode encontrá-lo na pasta de downloads do seu 
  computador ou em outro local que você especificou.
  * Na tela de instalação, marque a opção "Add Python 3.8 to PATH" e clique em "Install Now".
  * Aguarde enquanto a instalação é concluída. Isso pode levar alguns minutos, dependendo do seu computador.
  * Depois que a instalação for concluída, abra o prompt de comando digitando "cmd" na barra de pesquisa do Windows e 
  clicando em "Prompt de Comando" ou "Command Prompt"
* output.json é um arquivo de exemplo de saída.

------------------------------------------------

**As soluções para os problemas foram desenvolvidas por Lucas Humberto Czeck em Março de 2023**