GemiScrape

<div align="center"> <a href="https://postimg.cc/87w4SWyk"> <img src="https://i.postimg.cc/Gpn5vxGD/Gemini-Generated-Image-2babaj2babaj2bab.jpg" alt="GemiScrape" width="180"> </a>

<p>CLI em Python para interagir com o Google Gemini diretamente pelo terminal.</p>

<p> <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.10+"> <img src="https://img.shields.io/badge/Playwright-Automation-2EAD33?style=flat-square&logo=playwright&logoColor=white" alt="Playwright"> <img src="https://img.shields.io/badge/Google-Gemini-8E75FF?style=flat-square&logo=googlegemini&logoColor=white" alt="Google Gemini"> <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="MIT License"> </p> </div>

CLI em Python para interagir com o Google Gemini por meio de automação web via Playwright e Chromium, permitindo o uso do modelo diretamente pelo terminal.

🚀 Tecnologias
Python (3.10+)
Playwright (Automação de navegador)
Rich (Formatação de saída no terminal)
🛠️ Instalação e Configuração
1. Clonar o Repositório

Baixe o projeto para a sua máquina utilizando o Git e acesse a pasta gerada:

git clone <URL_DO_REPOSITORIO>
cd GemiScrape
2. Criar e Ativar o Ambiente Virtual (venv)

O uso da venv é obrigatório para isolar as dependências do projeto, evitando conflitos com o Python do sistema e erros de pacotes externos.

Linux / macOS:

python3 -m venv .venv
source .venv/bin/activate

Windows (PowerShell):

py -m venv .venv
.\.venv\Scripts\Activate.ps1

(Com a venv ativa, você verá (.venv) no início da linha do seu terminal).

3. Instalar Dependências Python

Com o ambiente virtual ativado, atualize o gerenciador de pacotes e instale as dependências listadas no projeto:

python -m pip install --upgrade pip
python -m pip install -r requirements.txt
4. Baixar o Navegador Chromium pelo Playwright

O Playwright exige uma versão específica do Chromium para rodar a automação. Mesmo que você já tenha o Chrome ou o Chromium instalado no sistema, é preciso baixar o binário compatível:

python -m playwright install chromium

Nota para Linux: Se o navegador falhar por falta de dependências gráficas ou bibliotecas do sistema, execute: python -m playwright install-deps chromium

🔑 Autenticação (Primeiro Acesso)

Como o GemiScrape acessa o Gemini pela interface web, é necessário entrar na sua conta Google. Utilize o modo com interface gráfica (--headed) na primeira execução:

python main.py --headed

Faça login normalmente na janela do navegador que se abrirá. O projeto utiliza um perfil persistente, salvando sua sessão para que você não precise logar novamente nas próximas vezes.

💻 Como Usar

Lembre-se de ativar a venv sempre que abrir um novo terminal para usar o projeto.

Iniciar a CLI:

python main.py

Executar com o navegador visível (Debug/Login):

python main.py --headed

Enviar um prompt direto:

python main.py "Explique como funciona o Playwright"

Exibir ajuda:

python main.py --help
⚠️ Limitações e Uso Responsável
Não oficial: O projeto interage com a interface web do Gemini e não utiliza uma API oficial.
Manutenção: Mudanças estruturais no layout do Google Gemini podem quebrar os seletores do Playwright, exigindo atualizações no código.
Segurança: Nunca compartilhe a pasta do seu perfil persistente ou diretório de sessão, pois ela pode conter dados de autenticação da sua conta Google.
