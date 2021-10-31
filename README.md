# Busca por ciclos em grafos

Nesse projeto são exploradas duas maneiras diferentes de se enumerar todos os ciclos de um grafo, sendo elas:

- Busca por profundidade
- Permutação de vértices

## Como rodar o projeto?

Primeiramente, é necessário clonar o repositório. Isso pode ser feito com o comando a seguir:

```bash
  # via HTTPS
  $ git clone https://github.com/thallesnct/graph-cycles.git
  # via SSH
  $ git clone git@github.com:thallesnct/graph-cycles.git
```

Antes de rodar o projeto, é necessário estabelecer o ambiente virtual do python. Para isso execute o seguinte comando na pasta contendo o projeto:

```bash
  $ python3 -m venv env
```

Após isso você já poderá executar os arquivos do projeto!

Você poderá executar o arquivo `main.py` que rodará os 2 algoritmos para um mesmo grafo de testes, demonstrando se há alguma divergência encontrada entre os dois métodos e também denotando o tempo de execução de cada um.

Para isso, o comando a ser executado é:

```bash
  $ python3 main.py
```