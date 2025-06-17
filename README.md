# 🌊 Hidro Telemetria Automation

> **Automação inteligente para download e organização de dados hidrotelemetria da ANA (SNIRH)**

Uma solução robusta e escalável que automatiza a coleta diária de dados hidrológicos diretamente da Agência Nacional de Águas e Saneamento Básico (ANA). O sistema realiza todo o processo: acesso ao site, aplicação de filtros, download dos arquivos e organização automática das pastas.

---

## 🚀 Visão Geral

Este projeto foi desenvolvido com o objetivo de otimizar o processo de coleta de dados hidrológicos de estações localizadas em Rondônia. Utilizando **Python e Selenium WebDriver**, o sistema acessa o site oficial do SNIRH (Sistema Nacional de Informações sobre Recursos Hídricos), aplica filtros personalizados, realiza o download dos arquivos e organiza automaticamente os dados em pastas específicas por estação.

Essa automação elimina atividades manuais repetitivas, garante padronização, minimiza erros humanos e acelera significativamente o processo de coleta e organização dos dados.

---

## 🎯 Funcionalidades

✅ Acesso automatizado ao portal do SNIRH  
✅ Navegação inteligente entre menus e submenus  
✅ Filtro dinâmico por estação e data (de ontem até hoje)  
✅ Download automático dos arquivos hidrológicos  
✅ Criação automática da estrutura de pastas organizadas por estação  
✅ Compatível com múltiplos sistemas operacionais (Windows, Mac, Linux)  
✅ Configuração zero – basta executar  

---

## 📊 Estações Monitoradas

| 🏢 Estação    | 🔢 Código  | 📍 Localização |
|---------------|-----------|----------------|
| **Jiparana**  | 15560000  | Rondônia       |
| **Ariquemes** | 15430000  | Rondônia       |
| **Porto Velho** | 15400000 | Rondônia       |
| **Guajará**   | 15250000  | Rondônia       |

---

## 📁 Estrutura de Pastas Criada

O sistema cria automaticamente a seguinte organização:

```
📥 hidro-telemetria-data/
├── 📂 Jiparana/      # Dados da estação 15560000
├── 📂 Ariquemes/     # Dados da estação 15430000
├── 📂 Portovelho/    # Dados da estação 15400000
└── 📂 Guajara/       # Dados da estação 15250000
```

---

## 💻 Tecnologias e Habilidades Demonstradas

- 🐍 **Python** – Programação e automação
- 🤖 **Selenium WebDriver** – Automação de navegação web
- 🌐 **ChromeOptions** – Configuração para download automático
- ⏳ **WebDriverWait & Expected Conditions** – Esperas dinâmicas e sincronização precisa
- 🖱️ **ActionChains** – Interação avançada com elementos web
- 🛠️ **Manipulação de arquivos e datas** – Organização eficiente das pastas e controle de períodos
- ✅ Código modular, organizado, de fácil manutenção e expansão

---

## 🛠️ Pré-requisitos

- Python 3.6 ou superior
- Google Chrome instalado
- ChromeDriver (incluído no projeto)

### Instalação das Dependências

```bash
pip install selenium
```

Ou, com o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## 🎯 Como Executar

### 1️⃣ Clone ou baixe o projeto

```bash
git clone [seu-repositorio]
cd hidro-telemetria-automation
```

### 2️⃣ Execute o programa

```bash
python main.py
```

### 3️⃣ A automação fará tudo por você:

- Configura as pastas automaticamente
- Acessa o site da ANA
- Filtra cada estação pelo código
- Define o período de coleta (ontem até hoje)
- Realiza o download
- Organiza os arquivos
- Fecha o navegador ao finalizar

---

## 🔍 O que o Programa Faz

1. Acessa o portal oficial da ANA
2. Navega automaticamente entre menus e submenus
3. Filtra estações hidrológicas pelo código
4. Define o intervalo de coleta (ontem até hoje)
5. Realiza download automático dos dados
6. Organiza os arquivos em pastas separadas por estação
7. Repete o processo para todas as estações configuradas

---

## 🔧 Personalização

Para adicionar novas estações, basta editar o dicionário no código:

```python
stationCodeDict = {
    "nova_estacao": {
        "code": "CODIGO_ESTACAO",
        "directory": "CAMINHO_DIRETORIO"
    }
}
```

---

## 🐛 Solução de Problemas

| Problema                      | Solução                              |
|--------------------------------|--------------------------------------|
| ChromeDriver incompatível      | Verifique a versão do Chrome         |
| Erro de permissão              | Execute como administrador           |
| Site fora do ar                | Verifique conexão ou tente mais tarde|
| Download não inicia            | Verifique permissões da pasta destino|

---

## 🎨 Ferramentas Utilizadas

- 🐍 Python – Linguagem base
- 🤖 Selenium WebDriver – Automação web
- 🌐 Google Chrome – Navegador controlado
- 🗂️ OS & Pathlib – Manipulação de arquivos e diretórios
- ⏳ WebDriverWait – Controle de sincronização


## 🤝 Contribua!

Contribuições são bem-vindas!  
Participe enviando:

- 🐛 Reporte de bugs
- 💡 Sugestões de melhorias
- 🔧 Pull requests com novas funcionalidades

---

## 📢 Dica

Execute este projeto periodicamente para manter seus dados hidrológicos sempre atualizados.

---

**Criado com 💙 para facilitar e acelerar a coleta de dados ambientais.**
