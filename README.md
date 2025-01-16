
# BotAPI

Bem-vindo ao BotAPI! Este projeto fornece exemplos práticos de uso da API do Telegram para integrar os dados dos sensores da sensor.log com seus sistemas ou interfaces. Ele é ideal para desenvolvedores que desejam conectar dispositivos IoT e sistemas de monitoramento com o Telegram de maneira simples e eficiente.

## Índice

- [Introdução](#introdução)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
  - [Obtenção do Token do Bot no Telegram](#obtenção-do-token-do-bot-no-telegram)
  - [Adicionando o Bot ao Canal de Log](#adicionando-o-bot-ao-canal-de-log)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Exemplos de Uso](#exemplos-de-uso)
  - [Exemplo Básico](#exemplo-básico)
  - [Exemplo HTTP POST](#exemplo-http-post)
  - [Exemplo de Inserção em Banco de Dados SQLite](#exemplo-de-inserção-em-banco-de-dados-sqlite)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Introdução

O BotAPI permite que você:

- Capture e processe eventos de sensores enviados para um canal do Telegram.
- Integre esses dados com sistemas externos, APIs ou bancos de dados.
- Implemente funcionalidades personalizadas para monitoramento e automação.

## Pré-requisitos

Antes de começar, certifique-se de ter:

- **Python 3.7 ou superior**: [Baixe aqui](https://www.python.org/downloads/).
- **Git**: Para clonar o repositório. [Baixe aqui](https://git-scm.com/).
- **Virtualenv** (opcional): Para criar um ambiente isolado de desenvolvimento.

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/eduautomatiza/botAPI.git
   cd botAPI
   ```

2. **Crie um ambiente virtual:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

## Configuração

### Obtenção do Token do Bot no Telegram

1. **Inicie uma conversa com o BotFather:**
   - No aplicativo do Telegram, procure por `@BotFather` e selecione o bot oficial (verificado com um ícone azul).
   - Toque em "Iniciar" para começar a conversa.

2. **Crie um novo bot:**
   - Envie o comando `/newbot` no chat com o BotFather.
   - Siga as instruções fornecidas para:
     - **Definir um nome para o seu bot**: Por exemplo, `MeuBotLegal`.
     - **Definir um nome de usuário para o bot**: Deve terminar com `bot`, por exemplo, `MeuBotLegal_bot`.

3. **Obtenha o token do bot:**
   - Após configurar o nome e o nome de usuário, o BotFather fornecerá um token de API no formato:
     ```
     123456789:ABCdEfGhIjKlMnOpQrStUvWxYz123456789
     ```
   - Guarde este token em um local seguro, pois ele é essencial para conectar o seu bot à API do Telegram.

4. **Nota de Segurança:**
   - Não compartilhe seu token publicamente.
   - Caso suspeite que ele foi comprometido, use o comando `/revoke` no BotFather para gerar um novo token.

### Adicionando o Bot ao Canal de Log

Adicione seu bot a um canal de LOG de onde deseja receber os dados dos sensores e garanta que ele tenha as permissões necessárias para ler mensagens.

## Estrutura do Projeto

- **`basic.py`**: Processa eventos do Telegram e exibe os dados no console.
- **`http_post.py`**: Envia dados para URLs específicas usando HTTP POST.
- **`SQL_insert.py`**: Insere dados recebidos em um banco de dados SQLite.
- **`Sensorlog/`**: Módulos para processamento dos eventos e valores dos sensores.
- **`requirements.txt`**: Lista de dependências do projeto.

## Exemplos de Uso

### Exemplo Básico

1. Configure o token no arquivo `basic.py`:
   ```python
   TOKEN = "SEU_TOKEN_AQUI"
   ```

2. Execute o script:
   ```bash
   python basic.py
   ```

3. Verifique os logs no console.

### Exemplo HTTP POST

1. Configure o token e as URLs no arquivo `http_post.py`:
   ```python
   TOKEN = "SEU_TOKEN_AQUI"
   EVENT_URL = "http://example.com/event"
   VALUES_URL = "http://example.com/values"
   ```

2. Execute o script:
   ```bash
   python http_post.py
   ```

3. Os dados serão enviados para as URLs configuradas.

### Exemplo de Inserção em Banco de Dados SQLite

1. Configure o token e o banco no arquivo `SQL_insert.py`:
   ```python
   TOKEN = "SEU_TOKEN_AQUI"
   DB_NAME = "sensordata.db"
   ```

2. Configure o banco de dados (**apenas na primeira vez** que for usar SQL_insert.py).
   Execute o script create_db.py para criar a base de dados e as tabelas necessárias:
   ```bash
   python create_db.py
   ```

3. Execute o script:
   ```bash
   python SQL_insert.py
   ```

4. Os dados serão salvos no banco SQLite.

