# Sistema de Cadastramento de Produtos

Este é um projeto de sistema de cadastramento de produtos desenvolvido em Python, utilizando criptografia para proteger os dados sensíveis e uma conexão com o banco de dados Oracle.

## Funcionalidades

O sistema oferece as seguintes funcionalidades:
1. Cadastrar um novo produto.
2. Alterar dados de um produto existente.
3. Excluir um produto.
4. Listar todos os produtos cadastrados.

## Estrutura do Projeto

### Menu Inicial

O menu inicial apresenta as opções disponíveis ao usuário:
```python
def menuInicial():
    print('DIGITE 1 PARA CADASTRAR UM PRODUTO.')
    print('DIGITE 2 PARA ALTERAR UM PRODUTO.')
    print('DIGITE 3 PARA EXCLUIR UM PRODUTO.')
    print('DIGITE 4 PARA LISTAR OS PRODUTOS.')
    print('DIGITE OUTRO NÚMERO PARA SAIR.')
    menu = int(input('DIGITE O NÚMERO: '))
    return menu
```

### Criptografia e Descriptografia

A função `criptografiaDescriptografia` é responsável por criptografar e descriptografar os nomes e descrições dos produtos:
```python
def criptografiaDescriptografia(palavra, x):
    # Função de criptografia e descriptografia
    # Implementação...
    return texto
```

### Conexão com o Banco de Dados Oracle

A conexão com o banco de dados Oracle é estabelecida utilizando a biblioteca `oracledb`:
```python
import getpass
import oracledb

pw = getpass.getpass("Digite a senha: ")

try:
    conexao = oracledb.connect(
    user="Priscila2",
    password = pw,
    dsn="localhost/xepdb1")
except Exception as erro:
    print("Erro em conexao", erro)
else:
    print("Conectado", conexao.version)
```

### Operações com Produtos

#### Cadastro de Produto
Para cadastrar um novo produto, o sistema coleta os dados e realiza cálculos para determinar o preço de venda, receita bruta, custo fixo, comissão de vendas, impostos e rentabilidade:
```python
if menu == 1:
    # Código para cadastrar um novo produto
    # Implementação...
```

#### Alteração de Produto
Permite alterar os dados de um produto existente:
```python
elif menu == 2:
    # Código para alterar um produto
    # Implementação...
```

#### Exclusão de Produto
Permite excluir um produto do banco de dados:
```python
elif menu == 3:
    # Código para excluir um produto
    # Implementação...
```

#### Listagem de Produtos
Lista todos os produtos cadastrados, exibindo os detalhes e cálculos relacionados:
```python
elif menu == 4:
    # Código para listar produtos
    # Implementação...
```

## Como Executar

1. Certifique-se de ter o Python instalado em seu sistema.
2. Instale a biblioteca `oracledb` com o comando:
    ```bash
    pip install oracledb
    ```
3. Execute o script Python:
    ```bash
    python nome_do_script.py
    ```
4. Siga as instruções exibidas no menu para realizar as operações desejadas.

## Observações

- As funções de criptografia e descriptografia utilizam uma matriz de substituição simples para proteger os nomes e descrições dos produtos.
- Certifique-se de que o banco de dados Oracle esteja configurado corretamente e acessível.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---
