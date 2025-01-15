# BotAPI

Este projeto implementa um bot do Telegram utilizando a biblioteca `pyTelegramBotAPI`. O bot é capaz de processar eventos e valores de sensores, enviando notificações conforme configurado.

## Índice

- [Instalação](#instalação)
- [Configuração](#configuração)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Exemplos de Uso](#exemplos-de-uso)

## Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/eduautomatiza/botAPI.git
   cd botAPI
   ```

2. **Crie um ambiente virtual:**

   Certifique-se de ter o `virtualenv` instalado.

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

### Adicione o Bot a um Canal de Log

Adicione seu bot ao canal onde deseja receber as notificações de eventos e valores dos sensores.

## Estrutura do Projeto

- `basic.py`: Exemplo básico que processa eventos e valores de sensores recebidos do canal do Telegram e imprime os detalhes no console.
- `http_post.py`: Exemplo que envia eventos e valores de sensores recebidos do canal do Telegram para uma URL especificada usando solicitações HTTP POST.
- `SQL_insert.py`: Exemplo que insere eventos e valores de sensores recebidos do canal do Telegram em um banco de dados SQLite.
- `Sensorlog`: Pasta que contém módulos para decodificação e processamento de eventos e valores de sensores.
- `requirements.txt`: Lista de dependências necessárias para o projeto.


## Exemplos de Uso

### Exemplo Básico

O arquivo [basic.py](basic.py) processa eventos e valores de sensores recebidos do canal do Telegram e imprime os detalhes no console.

Para usar este exemplo:

1. Configure o token no arquivo `basic.py` substituindo `"SEU_TOKEN_AQUI"` pelo seu token do Telegram.
2. Execute o script:

   ```bash
   python basic.py
   ```

### Exemplo HTTP POST

O arquivo [http_post.py](http_post.py) envia eventos e valores de sensores recebidos do canal do Telegram para uma URL especificada usando solicitações HTTP POST.

Para usar este exemplo:

1. Configure o token no arquivo `http_post.py` substituindo `"SEU_TOKEN_AQUI"` pelo seu token do Telegram.
2. Substitua as URLs de exemplo (`http://example.com/event` e `http://example.com/values`) pelas URLs desejadas.
3. Execute o script:

   ```bash
   python http_post.py
   ```

### Exemplo de Inserção em Banco de Dados SQLite

O arquivo [SQL_insert.py](SQL_insert.py) insere eventos e valores de sensores recebidos do canal do Telegram em um banco de dados SQLite.

Para usar este exemplo:

1. Configure o token no arquivo `SQL_insert.py` substituindo `"SEU_TOKEN_AQUI"` pelo seu token do Telegram.
2. Configure as tabelas `events` e `values` no banco de dados SQLite conforme necessário.
3. Execute o script:


   ```bash
   python SQL_insert.py
   ```

Cada exemplo demonstra diferentes maneiras de processar e utilizar os dados recebidos pelo bot.

2. **Interaja com o bot:**

   O bot estará ativo e pronto para processar eventos e valores de sensores conforme implementado.
