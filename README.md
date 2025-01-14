# BotAPI

Este projeto implementa um bot do Telegram utilizando a biblioteca `pyTelegramBotAPI`. O bot é capaz de processar eventos e valores de sensores, enviando notificações conforme configurado.

## Índice

- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)

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

### Configure o Token

No arquivo `mainTelegramBot.py`, substitua a variável `TELEGRAM_TOKEN` pelo token obtido:

```python
TELEGRAM_TOKEN = "SEU_TOKEN_AQUI"
```

### Adicione o Bot a um Canal de Log

Adicione seu bot ao canal onde deseja receber as notificações de eventos e valores dos sensores.

## Uso

1. **Execute o bot:**

   Após configurar o token e adicionar o bot ao canal desejado, inicie o bot:

   ```bash
   python main.py
   ```

2. **Interaja com o bot:**

   O bot estará ativo e pronto para processar eventos e valores de sensores conforme implementado.

## Estrutura do Projeto

- `main.py`: Script principal que inicializa o bot e define os manipuladores de eventos.
- `Post.py`: Módulo que contém classes e funções para decodificar e processar eventos e valores recebidos.
- `requirements.txt`: Lista de dependências necessárias para o projeto.
