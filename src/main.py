import tkinter as tk
from tkinter import messagebox

# Importa a função específica do módulo system_tools
from utils.system_tools import verificar_chkdsk

# --- CONFIGURAÇÃO DA JANELA PRINCIPAL ---

def criar_interface():
    janela = tk.Tk()
    janela.title("Menu de Reparo e Ferramentas de TI")
    janela.geometry("400x600")
    janela.configure(bg="#2E2E2E")

    titulo = tk.Label(janela, text="Menu de Reparo e Ferramentas de TI", font=("Helvetica", 16, "bold"), fg="#00FF00", bg="#2E2E2E")
    titulo.pack(pady=20)

    # Botão para "Verificar e Reparar Disco (CHKDSK)"
    botao_chkdsk = tk.Button(janela, text="1. Verificar e Reparar Disco (CHKDSK)", command=verificar_chkdsk,
                              bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_chkdsk.pack(pady=5)

    janela.mainloop()

# Inicia a aplicação
if __name__ == "__main__":
    criar_interface()