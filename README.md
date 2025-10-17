# 🔍 Google Scraper - High Performance Template

Este projeto foi desenvolvido com foco em **alta performance**, **eficiência técnica** e **escalabilidade**. Ele oferece uma estrutura robusta e flexível para realizar scraping de resultados de busca do Google (excluindo anúncios), utilizando duas abordagens complementares:

- **Selenium**: para interações reais com navegador (emulação de cliques, rolagem, etc.)
- **Requests + Parsing**: para scraping leve e rápido via requisições HTTP.

---

## 📌 Objetivo

Fornecer um **template base altamente eficiente** para scraping de resultados do Google, que pode ser facilmente adaptado para diferentes propósitos de coleta de dados na web.

---

## ✨ Funcionalidades

- 🔧 Arquitetura modular e extensível
- 🌐 Suporte a scraping dinâmico via Selenium (com interface visível ou headless)
- ⚡ Scraping leve via `requests` e `BeautifulSoup`
- 🚫 Filtro automático para excluir anúncios dos resultados
- 🧪 Estrutura pronta para testes e validações
- 📁 Organização limpa de diretórios e código

---

## 🛠️ Tecnologias Utilizadas

- Python 3.10+
- [Selenium](https://www.selenium.dev/)
- [BeautifulSoup (bs4)](https://www.crummy.com/software/BeautifulSoup/)
- [requests](https://docs.python-requests.org/en/latest/)
- [fake-useragent](https://pypi.org/project/fake-useragent/) (para simular navegação real)
- WebDriver (Chrome ou Firefox)

---

## 📂 Estrutura do Projeto

```

template_scrap/
├── scraping/
│   ├── **init**.py
│   ├── selenium_scraper.py     # Scraping com Selenium
│   ├── requests_scraper.py     # Scraping com requests + BeautifulSoup
│
├── utils/
│   ├── **init**.py
│   ├── logger.py               # Logger customizado
│   └── config.py               # Configurações globais
│
├── tests/
│   └── test_scrapers.py        # Testes automatizados
│
├── main.py                     # Ponto de entrada principal
├── requirements.txt
└── README.md

````

---

## 🚀 Como Usar

### 1. Clone o repositório
```bash
git clone https://github.com/luizpontesesquivel/template_scrap.git
cd google-scraper-template
````

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o scraper

```bash
python main.py
```

> Por padrão, o script faz uma busca simples e exibe os links não patrocinados (orgânicos) retornados pelo Google.

---

## 🧪 Testes

Os testes automatizados garantem que os scrapers estejam funcionando corretamente e retornem os dados esperados.

```bash
pytest tests/
```

---

## ⚠️ Avisos Legais

Este projeto é destinado **exclusivamente para fins educacionais e de pesquisa**. Raspar resultados do Google pode violar os Termos de Serviço da plataforma. **Use com responsabilidade e ética.**

---

## 👨‍💻 Autor

Desenvolvido por **Luiz Eduardo Pontes Esquivel**
📧 [luiz.esquivel@tcees.tc.br]
🔗 [[Seu LinkedIn ou GitHub opcional](https://github.com/luizpontesesquivel)]

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---
