# 🛒 Sistema de Gerenciamento de Produtos

Este é um aplicativo simples de gerenciamento de produtos com interface gráfica, desenvolvido em **Python** usando **Tkinter**. Ele permite **cadastrar**, **editar**, **excluir** e **exportar** produtos para um arquivo `.csv`, além de salvar os dados localmente em um arquivo `.json`.

---

## 📋 Funcionalidades

- ✅ Cadastro de produtos (nome, preço, quantidade)
- ✏️ Edição de produtos existentes
- 🗑️ Exclusão de produtos
- 📥 Salvamento automático em arquivo `produtos.json`
- 📤 Exportação de dados para `produtos.csv`
- 🖥️ Interface gráfica amigável com `Tkinter`

---

## 💻 Requisitos

- Python 3.6 ou superior

As bibliotecas usadas são todas nativas do Python:
- `tkinter`
- `json`
- `csv`
- `os`

---

## 🚀 Como usar

1. Clone ou baixe o repositório.
2. Execute o script Python:

```bash
python main.py

.
├── produtos.json         # Arquivo onde os dados dos produtos são salvos
├── produtos.csv          # Arquivo gerado ao exportar os dados
├── main.py                # Código-fonte principal
└── README.md             # Este arquivo
