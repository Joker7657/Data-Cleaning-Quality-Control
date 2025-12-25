# 🧹 Data Cleaning & Quality Control

Sistema robusto para **limpeza profunda, validação automatizada e estruturação de dados** para análise com dashboard interativo de visualização.

## ✨ Funcionalidades

✔️ **Limpeza Automatizada** - Remove espaços, caracteres inválidos e valores nulos  
✔️ **Normalização de Dados** - Padroniza formatos (CPF, e-mail, telefone, moeda)  
✔️ **Validação Inteligente** - Aplica regras de validação automática  
✔️ **Separação de Dados** - Separa registros válidos e rejeitados  
✔️ **Relatórios Detalhados** - Gera relatório completo de qualidade dos dados  
✔️ **Dashboard Interativo** - Visualização em tempo real com Streamlit  

---

## 🚀 Tecnologias

- **Python 3.12+**
- **Pandas** - Manipulação de dados
- **Streamlit** - Dashboard interativo
- **Regex (re)** - Validação de padrões
- **OpenPyXL** - Suporte para Excel

---

## 📁 Estrutura do Projeto

```
Data-Cleaning-Quality-Control/
├── main.py                      # Script principal do pipeline
├── README.md                    # Documentação
├── dashboard/
│   └── app.py                  # Dashboard Streamlit
├── src/
│   ├── cleaner.py              # Módulo de limpeza
│   ├── loader.py               # Carregador de dados
│   ├── normalizer.py           # Normalizador de formatos
│   ├── pipeline.py             # Pipeline principal
│   └── validator.py            # Validador de dados
└── data/
    ├── raw/                    # Dados brutos
    │   └── clientes.csv
    ├── processed/              # Dados processados
    │   ├── validos.csv
    │   └── rejeitados.csv
    └── reports/                # Relatórios
        └── validation_report.txt
```

---

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/Joker7657/Data-Cleaning-Quality-Control.git
cd Data-Cleaning-Quality-Control
```

### 2. Instale as dependências

```bash
pip install pandas streamlit openpyxl
```

---

## 🎯 Como Usar

### 1. Execute o Pipeline de Limpeza

Processa os dados brutos, aplica limpeza, normalização e validação:

```bash
python main.py
```

**Saída:**
- `data/processed/validos.csv` - Registros validados
- `data/processed/rejeitados.csv` - Registros com problemas
- `data/reports/validation_report.txt` - Relatório de qualidade

### 2. Visualize no Dashboard

Inicie o dashboard interativo para visualizar os resultados:

```bash
streamlit run dashboard/app.py
```

Acesse: **http://localhost:8501**

---

## 📊 Formato dos Dados

### Arquivo de Entrada (CSV/Excel)

O arquivo deve conter as seguintes colunas:

| Coluna    | Descrição                    | Exemplo                |
|-----------|------------------------------|------------------------|
| nome      | Nome completo                | João Silva             |
| cpf       | CPF (formatado ou não)       | 123.456.789-00         |
| email     | Endereço de e-mail           | joao@email.com         |
| telefone  | Telefone (formatado ou não)  | (11) 98765-4321        |
| renda     | Renda (formatado ou não)     | R$ 5.000,00            |

### Exemplo de Dados

```csv
nome,cpf,email,telefone,renda
João Silva,123.456.789-00,joao@email.com,(11) 98765-4321,R$ 5.000,00
Maria Santos,987.654.321-11,maria@email.com,(21) 987654321,R$ 3.500,50
```

---

## 🔧 Módulos

### 📥 DataLoader (`loader.py`)
Carrega dados de arquivos CSV ou Excel mantendo tipos como string para processamento.

### 🧼 DataCleaner (`cleaner.py`)
Remove espaços em branco, substitui valores nulos e limpa caracteres inválidos.

### 🔄 Normalizer (`normalizer.py`)
- **CPF**: Remove formatação e valida 11 dígitos
- **E-mail**: Converte para minúsculas e valida formato
- **Telefone**: Remove formatação e valida mínimo 10 dígitos
- **Moeda**: Converte formato brasileiro (R$ 1.000,00) para float

### ✅ Validator (`validator.py`)
Gera relatório com:
- Nomes ausentes
- E-mails inválidos
- CPFs inválidos
- Telefones inválidos

### 🔗 Pipeline (`pipeline.py`)
Orquestra todo o fluxo de processamento integrando todos os módulos.

---

## 📈 Dashboard

O dashboard Streamlit exibe:

1. **Métricas Principais**
   - Total de registros válidos
   - Total de registros rejeitados

2. **Relatório de Validação**
   - Estatísticas de qualidade dos dados
   - Problemas identificados por tipo

3. **Tabelas Interativas**
   - Visualização dos dados validados
   - Visualização dos dados rejeitados

---
