# GemiScrape

<p align="center">
  <img src="https://i.postimg.cc/Gpn5vxGD/Gemini-Generated-Image-2babaj2babaj2bab.jpg" alt="GemiScrape Logo" width="180">
</p>

<p align="center">
  <strong>Uma CLI para interagir com o Google Gemini diretamente pelo navegador.</strong>
</p>

<p align="center">
  Python · Playwright · Chromium
</p>

---

## Sobre o projeto

O **GemiScrape** é uma ferramenta de linha de comando que automatiza a interação com o Google Gemini usando um navegador controlado pelo Playwright.

A ideia é permitir que você envie prompts e receba respostas diretamente pelo terminal, sem precisar manter a interface do navegador aberta na tela durante o uso normal.

### Recursos

* Interface de linha de comando (CLI).
* Automação do navegador com Playwright.
* Chromium para executar a automação.
* Perfil persistente para manter a sessão do navegador.
* Modo visível para realizar o login inicial.
* Compatibilidade com Linux, Windows e macOS, dependendo das dependências e da versão do projeto.

> **Aviso:** o GemiScrape automatiza a interface web do Gemini. Ele não é uma API oficial do Google. Alterações no site, autenticação ou mecanismos de proteção podem afetar o funcionamento.

## Requisitos

Antes de começar, você precisa de:

* Python 3.10 ou superior, conforme a compatibilidade das dependências.
* `pip` e suporte a ambientes virtuais (`venv`).
* Git, caso queira clonar o repositório.
* Chromium instalado pelo Playwright.
* Uma conta Google com acesso ao Gemini.

---

## Instalação

### 1. Clonar o repositório

Se o projeto estiver hospedado no Git:

```bash
git clone URL_DO_REPOSITORIO
cd GemiScrape
```

Se você já baixou o projeto, entre diretamente na pasta dele.

### 2. Instalar o Python

#### Debian e Ubuntu

```bash
sudo apt update
sudo apt install python3 python3-full python3-venv
```

Verifique a instalação:

```bash
python3 --version
```

No Debian, o comando `python` pode não existir por padrão. Isso é normal: use `python3` antes de ativar o ambiente virtual.

#### Windows

Baixe o Python no site oficial:

https://www.python.org/downloads/

Durante a instalação, marque a opção **Add Python to PATH**.

Verifique:

```powershell
py --version
```

#### macOS

Instale o Python pelo site oficial:

https://www.python.org/downloads/macos/

Verifique:

```bash
python3 --version
```

---

## Configurando o ambiente virtual (`venv`)

O ambiente virtual mantém as dependências do GemiScrape isoladas do Python do sistema.

Isso evita conflitos com pacotes do sistema operacional e problemas como o erro `externally-managed-environment` do PEP 668.

### Linux e macOS

Na pasta do projeto, execute:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows — PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Se o PowerShell bloquear a ativação por causa da política de execução, você pode usar o Prompt de Comando:

```bat
.venv\Scripts\activate.bat
```

Quando o ambiente estiver ativo, o terminal normalmente mostrará `(.venv)` no início da linha.

### Atualizar o pip

Com a `venv` ativada:

```bash
python -m pip install --upgrade pip
```

**Importante:** ative a `venv` antes de instalar as dependências ou executar o projeto.

---

## Instalando as dependências

O projeto utiliza um arquivo `requirements.txt` para listar as bibliotecas Python necessárias.

Com a `venv` ativada, execute:

```bash
python -m pip install -r requirements.txt
```

Se o arquivo ainda não existir, verifique quais dependências o projeto utiliza antes de criá-lo. Por exemplo, uma versão que usa Playwright e Rich pode ter:

```text
playwright
rich
```

Instale apenas as dependências realmente utilizadas pela versão do código que você está executando.

---

## Instalando o Chromium

O Playwright precisa de um navegador compatível para automatizar o Gemini.

Instalar a biblioteca Python não instala necessariamente o navegador. Por isso, execute:

```bash
python -m playwright install chromium
```

Esse comando baixa a versão do Chromium gerenciada pelo Playwright.

### Linux: dependências do navegador

Em algumas distribuições Linux, podem faltar bibliotecas do sistema necessárias para iniciar o Chromium.

Se aparecerem erros sobre bibliotecas compartilhadas ou dependências ausentes, tente:

```bash
python -m playwright install-deps chromium
```

Esse comando pode solicitar privilégios administrativos. Se necessário, siga as instruções apresentadas pelo próprio Playwright para sua distribuição.

### Chromium do sistema versus Chromium do Playwright

O Playwright normalmente utiliza uma versão própria e compatível do Chromium, baixada com o comando acima.

Você não precisa instalar o Chromium manualmente pelo gerenciador de pacotes apenas para executar o Playwright. O navegador baixado pelo Playwright é a opção recomendada para este projeto.

---

## Primeiro acesso ao Gemini

Se o GemiScrape usa um perfil persistente do navegador, é necessário realizar o login inicial.

Na versão que disponibiliza a opção `--headed`, execute:

```bash
python main.py --headed
```

Isso abre o navegador em modo visível.

1. Aguarde o Gemini carregar.
2. Entre na sua conta Google.
3. Conclua eventuais verificações de segurança.
4. Confirme que o Gemini está acessível.
5. Feche o programa normalmente.

A sessão poderá ser reutilizada nas próximas execuções, desde que o perfil persistente seja mantido e a sessão continue válida.

**Segurança:** nunca compartilhe ou publique o perfil do navegador. Ele pode conter cookies e outros dados de autenticação.

---

## Executando o GemiScrape

### Modo normal

Com a `venv` ativada:

```bash
python main.py
```

### Enviar um prompt diretamente

Se a versão instalada aceitar prompts como argumentos:

```bash
python main.py "Oi Gemini, tudo bem?"
```

### Modo com navegador visível

Para depurar problemas de login ou carregamento:

```bash
python main.py --headed
```

O comportamento exato desses comandos depende das opções implementadas no `main.py` da versão utilizada.

---

## Usando novamente depois

Sempre que abrir um novo terminal, entre na pasta do projeto e ative o ambiente virtual.

### Linux e macOS

```bash
cd ~/Documentos/GemiScrape
source .venv/bin/activate
python main.py
```

### Windows — PowerShell

```powershell
cd CAMINHO\PARA\GemiScrape
.\.venv\Scripts\Activate.ps1
python main.py
```

Para sair do ambiente virtual:

```bash
deactivate
```

---

## Solução de problemas

### `python: command not found`

No Linux, utilize `python3` para criar a `venv`:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Depois da ativação, o comando `python` normalmente estará disponível dentro do ambiente.

### `externally-managed-environment`

Esse erro é comum em distribuições Debian e outras que protegem o Python do sistema.

Não force a instalação global com `sudo pip`. Crie e ative um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

Se a criação da `venv` falhar no Debian:

```bash
sudo apt install python3-full python3-venv
```

### `ModuleNotFoundError: No module named 'playwright'`

O Playwright não está instalado no ambiente Python que está executando o programa.

```bash
source .venv/bin/activate
python -m pip install -r requirements.txt
```

### Chromium não encontrado

Instale o navegador usando o próprio Playwright:

```bash
python -m playwright install chromium
```

### Chromium não inicia no Linux

Instale as dependências do navegador:

```bash
python -m playwright install-deps chromium
```

### O Gemini solicita login novamente

Abra o navegador em modo visível:

```bash
python main.py --headed
```

Verifique se a sessão continua válida e se o perfil persistente não foi removido.

### O Gemini não responde ou os seletores falham

O site pode ter alterado sua interface. Verifique os seletores usados pelo código e teste o modo visível para identificar o que está acontecendo.

O modo headless também pode apresentar diferenças de comportamento em relação ao navegador visível.

### `apt update` apresenta erro de sintaxe em uma source

Verifique o arquivo de repositório indicado na mensagem de erro. Um arquivo `.list` malformado pode impedir o APT de atualizar os índices ou instalar dependências.

Corrija ou desative apenas a entrada que está causando o problema.

---

## Estrutura do projeto

A estrutura pode variar de acordo com a versão, mas uma organização comum seria:

```text
GemiScrape/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
└── .venv/
```

O diretório `.venv/` é criado localmente e não deve ser enviado ao Git.

### `.gitignore` recomendado

```gitignore
# Python
__pycache__/
*.py[cod]
*.egg-info/

# Virtual environment
.venv/
venv/

# Environment variables and secrets
.env

# Local browser profiles
browser/
```

Se o perfil persistente do navegador estiver fora do projeto, como em `~/.gemiscrape/browser`, não o adicione ao repositório nem compartilhe seus arquivos.

---

## Privacidade e uso responsável

* Proteja os dados de autenticação armazenados no perfil do navegador.
* Não publique cookies, tokens, senhas ou arquivos de sessão.
* Respeite os termos de uso e as políticas aplicáveis do Google.
* Evite automações abusivas ou que sobrecarreguem o serviço.
* Lembre-se de que o acesso pode mudar conforme a conta, a região e as atualizações do Gemini.

## Licença

Adicione aqui a licença escolhida para o projeto, por exemplo, MIT, caso seja essa a licença efetivamente adotada.

---

<p align="center">
  Feito para quem curte Python, automação e ferramentas de terminal.
</p>
