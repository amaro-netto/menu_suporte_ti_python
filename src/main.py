import tkinter as tk
from tkinter import messagebox
import os
import subprocess

# --- FUNÇÕES PARA AS TAREFAS ---

def limpar_arquivos_temporarios():
    try:
        # Comando para limpar arquivos temporários no Windows
        os.system('del /q /f /s %TEMP%\\*')
        messagebox.showinfo("Sucesso", "Arquivos temporários limpos com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {e}")

def reparar_sfc():
    try:
        messagebox.showinfo("Reparo SFC", "Executando reparo de arquivos de sistema. Isso pode levar algum tempo. Por favor, aguarde.")
        # O comando sfc /scannow precisa de permissões de administrador.
        subprocess.run(['sfc', '/scannow'], shell=True, check=True)
        messagebox.showinfo("Reparo SFC", "Reparo de arquivos de sistema concluído!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Erro no SFC", f"Ocorreu um erro ao executar o SFC. Código de retorno: {e.returncode}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro inesperado: {e}")


# --- CONFIGURAÇÃO DA JANELA PRINCIPAL ---
def criar_interface():
    janela = tk.Tk()
    janela.title("Menu de Reparo e Ferramentas de TI")
    janela.geometry("400x600")
    janela.configure(bg="#2E2E2E")

    # Título
    titulo = tk.Label(janela, text="Menu de Reparo e Ferramentas de TI", font=("Helvetica", 16, "bold"), fg="#00FF00", bg="#2E2E2E")
    titulo.pack(pady=20)

    # Botões
    botao_limpar = tk.Button(janela, text="3. Limpar Arquivos Temporários", command=limpar_arquivos_temporarios,
                              bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_limpar.pack(pady=5)

    botao_sfc = tk.Button(janela, text="2. Reparar Arquivos de Sistema (SFC)", command=reparar_sfc,
                           bg="#3A3A3A", fg="#00FF00", font=("Helvetica", 12), width=40)
    botao_sfc.pack(pady=5)
    
    # ... adicione os outros botões aqui ...

    janela.mainloop()

# Inicia a aplicação
if __name__ == "__main__":
    criar_interface()
