
# Configurando um Ambiente para Rodar um Bot do Telegram

## Pré-requisitos

1. **Instale o `virtualenv`**  
   Para criar ambientes Python isolados, instale o pacote `virtualenv` (caso ainda não tenha instalado):
   ```bash
   sudo apt install python3-virtualenv
   ```

2. **Crie uma pasta para o ambiente virtual**  
   Dentro do diretório do repositório, crie a pasta onde o ambiente virtual será configurado:
   ```bash
   mkdir venv
   ```

3. **Crie o ambiente virtual**  
   Crie o ambiente virtual usando a versão instalada do Python:
   ```bash
   virtualenv venv -p python3
   ```

4. **Ative o ambiente virtual**  
   Sempre que for trabalhar no projeto, ative o ambiente virtual:
   ```bash
   source venv/bin/activate
   ```

5. **Instale as dependências**  
   Na primeira vez, será necessário instalar os pacotes listados no arquivo `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

6. **Desative o ambiente virtual**  
   Quando terminar, você pode desativar o ambiente virtual com o comando:
   ```bash
   deactivate
   ```
