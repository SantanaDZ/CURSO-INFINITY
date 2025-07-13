import tkinter as tk
from tkinter import messagebox
import sqlite3

# === BANCO DE DADOS ===
conn = sqlite3.connect("empregados.db")
cursor = conn.cursor()

# Cria tabela se não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS empregados (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL,
    salario_bruto REAL NOT NULL,
    salario_liquido REAL NOT NULL,
    tipo TEXT NOT NULL,
    setor TEXT
)
""")
conn.commit()

# === CLASSES ===
class Funcionario:
    def __init__(self, nome, cpf, salario_bruto):
        self.nome = nome
        self.cpf = cpf
        self.salario_bruto = salario_bruto

    def calcular_salario_liquido(self):
        return self.salario_bruto - (self.salario_bruto * 0.03)

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario_bruto, setor):
        super().__init__(nome, cpf, salario_bruto)
        self.setor = setor

    def calcular_salario_liquido(self):
        return self.salario_bruto - (self.salario_bruto * 0.07)

# === FUNÇÕES ===
def cadastrar():
    nome = entry_nome.get()
    cpf = entry_cpf.get()
    salario = entry_salario.get()
    tipo = tipo_var.get()
    setor = entry_setor.get()

    if not (nome and cpf and salario):
        messagebox.showerror("Erro", "Preencha todos os campos obrigatórios.")
        return

    try:
        salario = float(salario)
    except ValueError:
        messagebox.showerror("Erro", "Salário inválido.")
        return

    if tipo == "Funcionário":
        emp = Funcionario(nome, cpf, salario)
        salario_liquido = emp.calcular_salario_liquido()
        setor_final = None
    elif tipo == "Gerente":
        if not setor:
            messagebox.showerror("Erro", "Informe o setor do gerente.")
            return
        emp = Gerente(nome, cpf, salario, setor)
        salario_liquido = emp.calcular_salario_liquido()
        setor_final = setor
    else:
        messagebox.showerror("Erro", "Tipo inválido.")
        return

    # Inserir no banco
    cursor.execute("""
        INSERT INTO empregados (nome, cpf, salario_bruto, salario_liquido, tipo, setor)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, cpf, salario, salario_liquido, tipo, setor_final))
    conn.commit()

    atualizar_lista()
    limpar_campos()

def atualizar_lista():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT nome, cpf, salario_bruto, salario_liquido, tipo, setor FROM empregados")
    registros = cursor.fetchall()

    for r in registros:
        nome, cpf, sb, sl, tipo, setor = r
        texto = f"{tipo}: {nome}\nCPF: {cpf}\nSalário Bruto: {sb:.2f}\nSalário Líquido: {sl:.2f}"
        if tipo == "Gerente":
            texto += f"\nSetor: {setor}"
        listbox.insert(tk.END, texto)
        listbox.insert(tk.END, "-"*40)

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_cpf.delete(0, tk.END)
    entry_salario.delete(0, tk.END)
    entry_setor.delete(0, tk.END)

# === INTERFACE TKINTER ===
root = tk.Tk()
root.title("Cadastro de Empregados")
root.geometry("500x600")

tk.Label(root, text="Nome:").pack()
entry_nome = tk.Entry(root, width=50)
entry_nome.pack()

tk.Label(root, text="CPF:").pack()
entry_cpf = tk.Entry(root, width=50)
entry_cpf.pack()

tk.Label(root, text="Salário Bruto:").pack()
entry_salario = tk.Entry(root, width=50)
entry_salario.pack()

tk.Label(root, text="Tipo de Empregado:").pack()
tipo_var = tk.StringVar(value="Funcionário")
tk.Radiobutton(root, text="Funcionário", variable=tipo_var, value="Funcionário").pack()
tk.Radiobutton(root, text="Gerente", variable=tipo_var, value="Gerente").pack()

tk.Label(root, text="Setor (apenas para Gerente):").pack()
entry_setor = tk.Entry(root, width=50)
entry_setor.pack()

tk.Button(root, text="Cadastrar", command=cadastrar).pack(pady=10)

tk.Label(root, text="Empregados cadastrados:").pack()
listbox = tk.Listbox(root, width=70, height=15)
listbox.pack()

atualizar_lista()
root.mainloop()

# Fecha o banco ao encerrar
conn.close()
