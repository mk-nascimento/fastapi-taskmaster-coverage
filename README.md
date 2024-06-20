
# FastAPI Taskmaster Coverage

Esta é uma aplicação RESTful API construída com FastAPI, SQLAlchemy, MariaDB e gerenciada pelo Poetry.

## Pré-requisitos

Certifique-se de ter os seguintes itens instalados em sua máquina:

- [![MariaDB 11+](https://img.shields.io/badge/MariaDB-11+-brown.svg?logo=mariadb)](https://mariadb.org/download/?t=mariadb&p=mariadb&r=11.0.0)
- [![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue.svg?logo=python)](https://www.python.org/downloads/release/python-3110/)
- [![Poetry 1.8+](https://img.shields.io/badge/Poetry-1.8+-blue.svg?logo=poetry)](https://python-poetry.org/docs/#installation)

## Configuração do Ambiente

1. Clone o repositório:

    ```sh
    git clone https://github.com/mk-nascimento/fastapi-taskmaster-coverage.git
    cd fastapi-taskmaster-api
    ```

2. Instale as dependências:

    - Poetry
        > Antes de prosseguir com a instalação, é recomendado verificar a versão do Python e Poetry recomendada no topo deste arquivo. Certifique-se de ter a versão correta instalada em seu sistema antes de continuar.
        ```sh
        poetry install
        ```

    - Ou, se você preferir usar pip:
        > Antes de prosseguir com a instalação, é recomendado verificar a versão do Python recomendada no topo deste arquivo. Certifique-se de ter a versão correta instalada em seu sistema antes de continuar.
        ```sh
        pip install -r requirements.txt
        ```

3. Crie e configure o banco de dados PostgreSQL. Em seguida, crie um arquivo `.env` na raiz do projeto baseado no arquivo [.env.example](.env.example):

    - Copie o conteúdo de [.env.example](.env.example) para um novo arquivo `.env` e atualize as credenciais conforme necessário:

        ```sh
        cp .env.example .env
        ```

4. Ative o ambiente virtual:

    - Poetry:

        ```sh
        poetry shell
        ```

    - Ou, caso utilize um ambiente virtual criado com `venv`:

        ```sh
        # Crie um ambiente virtual com o nome desejado, substituindo "<sua_venv>" por um nome escolhido:
        python -m venv <sua_venv>
        ```

        - Sistemas Unix-like "Linux/Mac":
            ```sh
            source <sua_venv>/bin/activate  # Linux/Mac
            ```

        - Sistemas Windows:
            ```PowerShell
            <sua_venv>\Scripts\activate     # Windows
            ```

5. Execute as migrações do banco de dados:

    ```sh
    alembic upgrade head
    ```

## Rodando a Aplicação

Execute a aplicação com o comando:

```sh
uvicorn taskmaster.main:app --reload
```

A API estará disponível em http://127.0.0.1:8000.

## Licença

Este projeto está licenciado sob a licença Apache 2.0 - veja o arquivo [LICENSE](LICENSE) para detalhes.