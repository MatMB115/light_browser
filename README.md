# Light Browser

**Light Browser** é um navegador web simples desenvolvido com PyQt5, organizado segundo o padrão de arquitetura MVC (Model-View-Controller). Ele suporta navegação básica e inclui um sistema de log para registrar URLs acessadas.

## Funcionalidades

- Navegação básica (voltar, avançar, home, recarregar)
- Barra de endereço para navegar para URLs específicas
- Sistema de log de URLs acessadas (ativado via linha de comando)
- Suporte básico a SSL/TLS (via `QWebEngineView` baseado no Chromium)

## Pré-requisitos

- **Python 3.x**
- **PyQt5**: Para instalar, use `pip install PyQt5 PyQtWebEngine`

## Como Executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/light-browser-mvc.git
   cd light-browser-mvc
2. Instale as depedências:
    ```bash
    pip install -r requirements.txt
2. Execute o programa:
    ```bash
    python main.py
2. Execute com log:
    ```bash
    python main.py --log
    # ou
    python main.py -l