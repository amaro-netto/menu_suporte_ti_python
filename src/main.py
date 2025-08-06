import tkinter as tk
from tkinter import messagebox

# Importa todas as funções de ferramentas de sistema
from utils.system_tools import (
    verificar_chkdsk, 
    reparar_sfc, 
    limpar_arquivos_temporarios,
    verificar_erros_de_memoria  # Nova função importada
)

# --- CONFIGURAÇÃO DA JANELA PRINCIPAL ---

def criar_interface():
    janela = tk.Tk()
    janela.title("Menu de Reparo e Ferramentas de TI")
    janela.geometry("400x600")
    janela.configure(bg="#2E2E2E")

    titulo = tk.Label(janela, text="Menu de Reparo e Ferramentas de TI", font=("Helvetica", 16, "bold"), fg="#00FF00", bg="#2E2E2E")
    titulo.pack(pady=20)

    # --- CRIAÇÃO DOS BOTÕES ---

    # Botão 1: CHKDSK
    botao_chkdsk = tk.Button(janela, text="1. Verificar e Reparar Disco (CHKDSK)", command=verificar_chkdsk,
                              bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_chkdsk.pack(pady=5)

    # Botão 2: SFC
    botao_sfc = tk.Button(janela, text="2. Reparar Arquivos de Sistema (SFC)", command=reparar_sfc,
                           bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_sfc.pack(pady=5)
    
    # Botão 3: Limpeza de Arquivos Temporários
    botao_limpar = tk.Button(janela, text="3. Limpar Arquivos Temporários", command=limpar_arquivos_temporarios,
                              bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_limpar.pack(pady=5)

    # Botão 4: Verificar Erros de Memória
    botao_memoria = tk.Button(janela, text="4. Verificar Erros de Memória (Diagnóstico)", command=verificar_erros_de_memoria,
                               bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_memoria.pack(pady=5)

    # ... os outros botões virão aqui ...

    janela.mainloop()

# Inicia a aplicação
if __name__ == "__main__":
    criar_interface()